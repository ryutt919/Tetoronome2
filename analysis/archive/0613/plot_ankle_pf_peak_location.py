"""
Ankle PF Peak Location Visualization — Improved Stride Detection
- 적응형 full-stride 검출: 초기 탐지 후 inter-peak interval로 양 발 감지 여부 판단,
  양 발 감지 중이면 1.6x interval로 재탐지하여 동일 발 full stride만 추출
- toe-off 추정 없음 — PF peak 위치만 표시
- analysis/0613/fig01–fig05 저장
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks
import warnings
warnings.filterwarnings('ignore')

DATA_ROOT  = r"c:\Users\kimt9\OneDrive\Desktop\Gal4_PM\ryutt\tetoronome\data"
OUTPUT_DIR = r"c:\Users\kimt9\OneDrive\Desktop\Gal4_PM\ryutt\tetoronome\analysis\0613"
FS = 60

SUBJECTS   = ['박민규', '안승진', '오승민', '이상희', '진현준', '한상윤']
CONDITIONS = ['control', 'metro', 'tape', 'tape_metro']
COND_LABELS  = {'control': 'Control', 'metro': 'Metro',
                'tape': 'Tape', 'tape_metro': 'Tape+Metro'}
COND_COLORS  = {'control': '#2196F3', 'metro': '#F44336',
                'tape': '#4CAF50',  'tape_metro': '#FF9800'}

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'figure.dpi': 150,
})


# ── 유틸 ─────────────────────────────────────────────────────────────────────

def butter_lp(data, cutoff=15, fs=60, order=4):
    b, a = butter(order, cutoff / (fs / 2), btype='low')
    return filtfilt(b, a, data)


def _iqr_filter_peaks(acc, peaks):
    if len(peaks) < 4:
        return peaks
    v = acc[peaks]
    q1, q3 = np.percentile(v, 25), np.percentile(v, 75)
    iqr = q3 - q1
    return peaks[(v >= q1 - 1.5 * iqr) & (v <= q3 + 1.5 * iqr)]


def detect_all_steps(acc, fs=60):
    """200 ms min_dist로 모든 step peak 탐지 (양 발 포함 가능)."""
    p, _ = find_peaks(acc, distance=int(0.200 * fs), prominence=1.962)
    return _iqr_filter_peaks(acc, p)


def detect_full_stride_impacts(acc, fs=60):
    """
    적응형 full-stride 검출.
    Step 1: 200 ms min_dist로 모든 step 탐지
    Step 2: 중앙값 inter-peak interval로 양 발 감지 여부 판단
    Step 3: 양 발 감지 중(median < 400 ms)이면 1.6x interval로 재탐지
    """
    p0 = detect_all_steps(acc, fs)
    if len(p0) < 4:
        return p0

    med = np.median(np.diff(p0))           # frames

    if med < 0.40 * fs:                    # < 400 ms → 양 발 혼재
        new_dist = int(med * 1.6)
    else:                                   # 이미 full stride 수준
        new_dist = int(med * 0.80)

    p1, _ = find_peaks(acc, distance=new_dist, prominence=1.962)
    p1 = _iqr_filter_peaks(acc, p1)
    return p1 if len(p1) >= 4 else p0


def load_data(subject, condition):
    path = os.path.join(DATA_ROOT, subject, f"{subject}_{condition}.csv")
    if not os.path.exists(path):
        return None
    df = pd.read_csv(path)
    return df[df['source_segment'] == 'foot'].copy().reset_index(drop=True)


def extract_strides(foot_df, n_interp=101):
    """full-stride 분리 + PF peak 위치 반환."""
    ankle_col = 'ankle_dorsiflexion_plantarflexion_deg'
    acc_col   = 'shank_free_acceleration_resultant_m_s2'
    if ankle_col not in foot_df.columns or acc_col not in foot_df.columns:
        return None, None, None

    ankle   = butter_lp(foot_df[ankle_col].values)
    acc     = butter_lp(foot_df[acc_col].values)
    impacts = detect_full_stride_impacts(acc, fs=FS)
    if len(impacts) < 4:
        return None, None, None

    strides_norm, pf_locs, durations_ms = [], [], []
    xnew = np.linspace(0, 100, n_interp)

    for i in range(len(impacts) - 1):
        s, e = impacts[i], impacts[i + 1]
        seg  = ankle[s:e]
        n    = len(seg)
        if n < 20:          # full stride은 최소 ~330 ms = 20 samples
            continue
        pf_locs.append(np.argmin(seg) / n)
        strides_norm.append(np.interp(xnew, np.linspace(0, 100, n), seg))
        durations_ms.append(n / FS * 1000)

    if not strides_norm:
        return None, None, None
    return np.array(strides_norm), np.array(pf_locs), np.array(durations_ms)


# ── FIGURE 1: Control vs Metro 전체 피험자 앙상블 ─────────────────────────

fig1, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True)
fig1.suptitle(
    'Ankle Angle (DF/PF) Across Full Stride — Control vs Metro\n'
    'Red dot = PF peak per stride  |  +: Dorsiflexion,  −: Plantarflexion',
    fontsize=12, fontweight='bold'
)

cond_pf_data  = {}
cond_dur_data = {}

for ax, cond in zip(axes, ['control', 'metro']):
    all_strides, all_pf, all_dur = [], [], []

    for subj in SUBJECTS:
        fd = load_data(subj, cond)
        if fd is None:
            continue
        sn, pfl, dur = extract_strides(fd)
        if sn is None:
            continue
        all_strides.append(sn)
        all_pf.extend(pfl.tolist())
        all_dur.extend(dur.tolist())

    if not all_strides:
        ax.set_title(f'{COND_LABELS[cond]}\n(데이터 없음)')
        continue

    strides_arr = np.vstack(all_strides)
    pf_arr      = np.array(all_pf)
    dur_arr     = np.array(all_dur)
    cond_pf_data[cond]  = pf_arr
    cond_dur_data[cond] = dur_arr
    x = np.linspace(0, 100, 101)

    for s in strides_arr[::4]:
        ax.plot(x, s, color='lightgray', lw=0.5, alpha=0.35, zorder=1)
    for s, p in zip(strides_arr[::4], pf_arr[::4]):
        ax.scatter([p * 100], [s[int(p * 100)]],
                   color='crimson', s=15, alpha=0.30, zorder=4, edgecolors='none')

    mean_a = np.mean(strides_arr, axis=0)
    std_a  = np.std(strides_arr,  axis=0)
    ax.plot(x, mean_a, color=COND_COLORS[cond], lw=2.5, label='Mean', zorder=5)
    ax.fill_between(x, mean_a - std_a, mean_a + std_a,
                    alpha=0.18, color=COND_COLORS[cond], label='±1 SD', zorder=3)

    mean_pf_pct = np.mean(pf_arr) * 100
    std_pf_pct  = np.std(pf_arr)  * 100
    pf_on_mean  = mean_a[int(mean_pf_pct)]
    ax.scatter([mean_pf_pct], [pf_on_mean], color='crimson', s=130, zorder=7,
               label=f'PF peak mean: {mean_pf_pct:.1f}% (±{std_pf_pct:.1f}%)')
    ax.axvline(mean_pf_pct, color='crimson', lw=1.2, ls=':', alpha=0.85, zorder=6)
    ax.text(mean_pf_pct + 1.5, pf_on_mean,
            f'{mean_pf_pct:.1f}%', fontsize=9, color='crimson', va='center', fontweight='bold')

    ax.axhline(0, color='black', lw=0.7, alpha=0.45)
    ax.set_title(
        f'{COND_LABELS[cond]}  (n = {len(strides_arr)} strides)\n'
        f'stride duration: {np.mean(dur_arr):.0f} ± {np.std(dur_arr):.0f} ms',
        fontsize=10
    )
    ax.set_xlabel('Stride (%)', fontsize=11)
    if ax is axes[0]:
        ax.set_ylabel('Ankle angle (°)\n← PF    DF →', fontsize=11)
    ax.legend(loc='upper right', fontsize=8.5, framealpha=0.9)
    ax.set_xlim(0, 100)
    ax.grid(True, alpha=0.22)

plt.tight_layout()
fig1.savefig(os.path.join(OUTPUT_DIR, 'fig01_ankle_pf_peak_location_control_vs_metro.png'),
             dpi=150, bbox_inches='tight')
plt.close(fig1)
print('Saved: fig01')


# ── FIGURE 2: 4조건 PF peak timing boxplot ───────────────────────────────────

for cond in CONDITIONS:
    if cond in cond_pf_data:
        continue
    pf_all, dur_all = [], []
    for subj in SUBJECTS:
        fd = load_data(subj, cond)
        if fd is None:
            continue
        sn, pfl, dur = extract_strides(fd)
        if sn is None:
            continue
        pf_all.extend(pfl.tolist())
        dur_all.extend(dur.tolist())
    cond_pf_data[cond]  = np.array(pf_all)
    cond_dur_data[cond] = np.array(dur_all)

fig2, ax2 = plt.subplots(figsize=(8, 5))
fig2.suptitle('PF Peak Timing Distribution by Condition (full-stride corrected)\n% of stride',
              fontsize=12, fontweight='bold')

bp_data   = [cond_pf_data[c] * 100 for c in CONDITIONS]
bp_labels = [COND_LABELS[c]        for c in CONDITIONS]
bp_colors = [COND_COLORS[c]        for c in CONDITIONS]

bp = ax2.boxplot(bp_data, patch_artist=True,
                 medianprops={'color': 'black', 'lw': 2},
                 whiskerprops={'lw': 1.2},
                 flierprops={'marker': 'o', 'markersize': 3, 'alpha': 0.25})
for patch, color in zip(bp['boxes'], bp_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.70)

for i, (cond, color) in enumerate(zip(CONDITIONS, bp_colors), 1):
    d = cond_pf_data[cond] * 100
    if len(d):
        ax2.text(i, np.percentile(d, 75) + 2,
                 f'{np.mean(d):.1f}%', ha='center', va='bottom',
                 fontsize=9, color=color, fontweight='bold')

ax2.set_xticklabels(bp_labels, fontsize=10)
ax2.set_ylabel('PF Peak Timing (% of stride)', fontsize=11)
ax2.set_xlabel('Condition', fontsize=11)
ax2.set_ylim(0, 100)
ax2.grid(True, alpha=0.22, axis='y')

plt.tight_layout()
fig2.savefig(os.path.join(OUTPUT_DIR, 'fig02_ankle_pf_peak_timing_distribution.png'),
             dpi=150, bbox_inches='tight')
plt.close(fig2)
print('Saved: fig02')


# ── FIGURE 3: 안승진 Control 개별 stride 8개 ─────────────────────────────────

rep_subj = '안승진'
fd = load_data(rep_subj, 'control')

if fd is not None:
    ankle   = butter_lp(fd['ankle_dorsiflexion_plantarflexion_deg'].values)
    acc     = butter_lp(fd['shank_free_acceleration_resultant_m_s2'].values)
    impacts = detect_full_stride_impacts(acc, fs=FS)

    mid = len(impacts) // 2
    sel = impacts[mid - 4: mid + 5]
    n_strides = len(sel) - 1

    fig3, axes3 = plt.subplots(2, 4, figsize=(14, 6), sharey=True)
    fig3.suptitle(
        f'Individual Full Strides — {rep_subj}, Control  (full-stride detection)\n'
        'Red dot = PF peak location',
        fontsize=12, fontweight='bold'
    )
    axes3 = axes3.flatten()

    for idx in range(min(n_strides, 8)):
        ax = axes3[idx]
        s, e   = sel[idx], sel[idx + 1]
        seg    = ankle[s:e]
        n      = len(seg)
        t_ms   = np.arange(n) / FS * 1000

        pf_idx = int(np.argmin(seg))
        pf_val = seg[pf_idx]
        pf_ms  = pf_idx / FS * 1000
        pf_pct = pf_idx / n * 100

        ax.plot(t_ms, seg, color='#333333', lw=1.8, zorder=3)
        ax.axhline(0, color='black', lw=0.7, alpha=0.40)
        ax.scatter([pf_ms], [pf_val], color='crimson', s=70, zorder=5)
        ax.annotate(f'{pf_ms:.0f} ms\n({pf_pct:.0f}%)',
                    xy=(pf_ms, pf_val),
                    xytext=(pf_ms + t_ms[-1] * 0.12, pf_val - 3),
                    fontsize=7.5, color='crimson',
                    arrowprops=dict(arrowstyle='->', color='crimson', lw=0.8))

        ax.set_title(f'Stride {idx+1}  ({n/FS*1000:.0f} ms)', fontsize=9)
        ax.set_xlabel('Time (ms)', fontsize=8)
        if idx % 4 == 0:
            ax.set_ylabel('Ankle angle (°)\n← PF  DF →', fontsize=8)
        ax.set_xlim(0, t_ms[-1])
        ax.grid(True, alpha=0.20)

    for j in range(min(n_strides, 8), len(axes3)):
        axes3[j].set_visible(False)

    plt.tight_layout()
    fig3.savefig(os.path.join(OUTPUT_DIR, 'fig03_ankle_pf_peak_individual_strides.png'),
                 dpi=150, bbox_inches='tight')
    plt.close(fig3)
    print('Saved: fig03')


# ── FIGURE 4: 안승진 Control vs Metro 앙상블 비교 ────────────────────────────

fig4, axes4 = plt.subplots(1, 2, figsize=(13, 5), sharey=True)
fig4.suptitle(
    f'Ankle Angle Ensemble — {rep_subj}: Control vs Metro  (full-stride)\n'
    'Red dot = PF peak mean',
    fontsize=12, fontweight='bold'
)

for ax, cond in zip(axes4, ['control', 'metro']):
    fd = load_data(rep_subj, cond)
    if fd is None:
        ax.set_title(f'{COND_LABELS[cond]} — 데이터 없음')
        continue
    sn, pfl, dur = extract_strides(fd)
    if sn is None:
        ax.set_title(f'{COND_LABELS[cond]} — 검출 실패')
        continue

    x          = np.linspace(0, 100, 101)
    mean_a     = np.mean(sn, axis=0)
    std_a      = np.std(sn,  axis=0)
    mean_pf    = np.mean(pfl) * 100
    std_pf     = np.std(pfl)  * 100
    pf_on_mean = mean_a[int(mean_pf)]

    for s in sn[::3]:
        ax.plot(x, s, color='lightgray', lw=0.5, alpha=0.30, zorder=1)
    for s, p in zip(sn[::3], pfl[::3]):
        ax.scatter([p * 100], [s[int(p * 100)]],
                   color='crimson', s=18, alpha=0.28, zorder=4, edgecolors='none')

    ax.plot(x, mean_a, color=COND_COLORS[cond], lw=2.5, zorder=5, label='Mean')
    ax.fill_between(x, mean_a - std_a, mean_a + std_a,
                    alpha=0.18, color=COND_COLORS[cond], zorder=3, label='±1 SD')
    ax.scatter([mean_pf], [pf_on_mean], color='crimson', s=140, zorder=7,
               label=f'PF peak: {mean_pf:.1f}%')
    ax.axvline(mean_pf, color='crimson', lw=1.2, ls=':', alpha=0.85, zorder=6)
    ax.text(mean_pf + 1.5, pf_on_mean,
            f'{mean_pf:.1f}%', fontsize=9, color='crimson', va='center', fontweight='bold')
    ax.axhline(0, color='black', lw=0.7, alpha=0.45)

    ax.set_title(
        f'{COND_LABELS[cond]}  (n = {len(sn)} strides)\n'
        f'PF peak: {mean_pf:.1f}% ± {std_pf:.1f}%  |  dur: {np.mean(dur):.0f} ms',
        fontsize=10
    )
    ax.set_xlabel('Stride (%)', fontsize=11)
    if ax is axes4[0]:
        ax.set_ylabel('Ankle angle (°)\n← PF    DF →', fontsize=11)
    ax.legend(loc='upper right', fontsize=9, framealpha=0.9)
    ax.set_xlim(0, 100)
    ax.grid(True, alpha=0.22)

plt.tight_layout()
fig4.savefig(os.path.join(OUTPUT_DIR, 'fig04_ankle_ensemble_control_vs_metro_single_subj.png'),
             dpi=150, bbox_inches='tight')
plt.close(fig4)
print('Saved: fig04')


# ── FIGURE 5: 검증 — before vs after peak detection (안승진 control 5 s) ───

fd5 = load_data(rep_subj, 'control')
if fd5 is not None:
    acc_raw = butter_lp(fd5['shank_free_acceleration_resultant_m_s2'].values)

    # 전체의 중간 5초 구간
    mid_s  = len(acc_raw) // 2
    win    = int(5 * FS)
    seg_s  = max(0, mid_s - win // 2)
    seg_e  = seg_s + win
    acc_5s = acc_raw[seg_s:seg_e]
    t_5s   = np.arange(len(acc_5s)) / FS

    # Before: 280 ms min_dist (기존)
    p_before, _ = find_peaks(acc_5s, distance=int(0.280 * FS), prominence=1.962)
    p_before = _iqr_filter_peaks(acc_5s, p_before)

    # After: detect_full_stride_impacts
    p_after_full = detect_full_stride_impacts(acc_raw, fs=FS)
    # 5초 창 안에 있는 peak만 선택 (offset 보정)
    p_after = p_after_full[(p_after_full >= seg_s) & (p_after_full < seg_e)] - seg_s

    fig5, (ax_b, ax_a) = plt.subplots(2, 1, figsize=(13, 6), sharex=True)
    fig5.suptitle(
        f'Stride Detection Validation — {rep_subj}, Control  (5-second window)\n'
        'Before: min_dist=280 ms  |  After: adaptive full-stride',
        fontsize=12, fontweight='bold'
    )

    for ax, peaks, label, color in [
        (ax_b, p_before, f'BEFORE  (n={len(p_before)} peaks, step-level)', '#E53935'),
        (ax_a, p_after,  f'AFTER   (n={len(p_after)} peaks, full-stride)', '#1565C0'),
    ]:
        ax.plot(t_5s, acc_5s, color='#555555', lw=1.2, zorder=2)
        ax.scatter(t_5s[peaks], acc_5s[peaks],
                   color=color, s=80, zorder=5, label=label)
        # interval 표시
        if len(peaks) >= 2:
            ivs = np.diff(peaks) / FS * 1000
            for k in range(len(peaks) - 1):
                mid_x = (t_5s[peaks[k]] + t_5s[peaks[k+1]]) / 2
                ax.text(mid_x, ax.get_ylim()[1] if ax.get_ylim()[1] != 1 else acc_5s.max(),
                        f'{ivs[k]:.0f}ms', ha='center', va='top',
                        fontsize=7.5, color=color, alpha=0.85)
        ax.set_ylabel('Shank acc (m/s²)', fontsize=10)
        ax.legend(loc='upper right', fontsize=9)
        ax.grid(True, alpha=0.20)

    # 구간 interval 텍스트 다시 (ylim 확정 후)
    for ax, peaks, color in [(ax_b, p_before, '#E53935'), (ax_a, p_after, '#1565C0')]:
        if len(peaks) >= 2:
            ivs = np.diff(peaks) / FS * 1000
            ymax = ax.get_ylim()[1] * 0.97
            for k in range(len(peaks) - 1):
                mid_x = (t_5s[peaks[k]] + t_5s[peaks[k+1]]) / 2
                ax.text(mid_x, ymax, f'{ivs[k]:.0f} ms',
                        ha='center', va='top', fontsize=8, color=color, fontweight='bold')

    ax_a.set_xlabel('Time (s)', fontsize=11)
    plt.tight_layout()
    fig5.savefig(os.path.join(OUTPUT_DIR, 'fig05_stride_detection_validation.png'),
                 dpi=150, bbox_inches='tight')
    plt.close(fig5)
    print('Saved: fig05')

# ── 요약 ─────────────────────────────────────────────────────────────────────
print('\n=== Full-Stride Detection Summary ===')
for cond in CONDITIONS:
    pf  = cond_pf_data.get(cond,  np.array([]))
    dur = cond_dur_data.get(cond, np.array([]))
    if len(pf):
        print(f'  {COND_LABELS[cond]:12s}: '
              f'PF peak = {np.mean(pf)*100:.1f}% ± {np.std(pf)*100:.1f}%  |  '
              f'stride dur = {np.mean(dur):.0f} ± {np.std(dur):.0f} ms  |  '
              f'n = {len(pf)}')
