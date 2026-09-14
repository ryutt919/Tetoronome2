"""
fig08: Pelvis Roll Angle Across Full Stride — 4 conditions
- 전체 피험자 앙상블 평균 ± 1 SD 밴드
- 개별 stride 라인 (회색)
- 각 조건의 overall Roll SD 값 표시
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
COND_LABELS = {
    'control':    'Control',
    'metro':      'Metro',
    'tape':       'Tape',
    'tape_metro': 'Tape+Metro',
}
COND_COLORS = {
    'control':    '#1565C0',
    'metro':      '#C62828',
    'tape':       '#2E7D32',
    'tape_metro': '#E65100',
}

# C→M, C→T, C→T+M Roll SD 변화율 (보고서 수치)
ROLL_SD_CHANGE = {
    'control':    '+0%  (baseline)',
    'metro':      'C→M  +4.26%',
    'tape':       'C→T  +51.03%',
    'tape_metro': 'C→T+M  +16.34%',
}

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'figure.dpi': 150,
})


def butter_lp(data, cutoff=15, fs=60, order=4):
    b, a = butter(order, cutoff / (fs / 2), btype='low')
    return filtfilt(b, a, data)


def iqr_filter(acc, peaks):
    if len(peaks) < 4:
        return peaks
    v = acc[peaks]
    q1, q3 = np.percentile(v, 25), np.percentile(v, 75)
    iqr = q3 - q1
    return peaks[(v >= q1 - 1.5 * iqr) & (v <= q3 + 1.5 * iqr)]


def detect_full_stride_impacts(acc, fs=60):
    p0, _ = find_peaks(acc, distance=int(0.200 * fs), prominence=1.962)
    p0 = iqr_filter(acc, p0)
    if len(p0) < 4:
        return p0
    med = np.median(np.diff(p0))
    new_dist = int(med * 1.6) if med < 0.40 * fs else int(med * 0.80)
    p1, _ = find_peaks(acc, distance=new_dist, prominence=1.962)
    p1 = iqr_filter(acc, p1)
    return p1 if len(p1) >= 4 else p0


def load_foot(subject, condition):
    path = os.path.join(DATA_ROOT, subject, f"{subject}_{condition}.csv")
    if not os.path.exists(path):
        return None
    df = pd.read_csv(path)
    return df[df['source_segment'] == 'foot'].copy().reset_index(drop=True)


def extract_pelvis_roll_strides(foot_df, n_interp=101):
    """
    full-stride로 pelvis roll 분리 후 정규화.
    Returns: strides_norm (N×101), overall_roll_sd (scalar)
    """
    roll_col = 'hip_quaternion_roll_deg'
    acc_col  = 'shank_free_acceleration_resultant_m_s2'
    if roll_col not in foot_df.columns or acc_col not in foot_df.columns:
        return None, None

    roll = butter_lp(foot_df[roll_col].values)
    acc  = butter_lp(foot_df[acc_col].values)

    # overall Roll SD (전체 시계열 SD — 보고서 지표와 동일)
    overall_sd = float(np.std(roll))

    impacts = detect_full_stride_impacts(acc, fs=FS)
    if len(impacts) < 4:
        return None, overall_sd

    strides_norm = []
    xnew = np.linspace(0, 100, n_interp)
    for i in range(len(impacts) - 1):
        s, e = impacts[i], impacts[i + 1]
        seg  = roll[s:e]
        n    = len(seg)
        if n < 20:
            continue
        strides_norm.append(np.interp(xnew, np.linspace(0, 100, n), seg))

    if not strides_norm:
        return None, overall_sd
    return np.array(strides_norm), overall_sd


# ── 데이터 수집 ──────────────────────────────────────────────────────────────
cond_data = {}   # cond → {'strides': np.array, 'roll_sds': list}

for cond in CONDITIONS:
    all_strides = []
    all_roll_sds = []

    for subj in SUBJECTS:
        fd = load_foot(subj, cond)
        if fd is None:
            continue
        sn, rsd = extract_pelvis_roll_strides(fd)
        if sn is not None:
            all_strides.append(sn)
        if rsd is not None:
            all_roll_sds.append(rsd)

    if all_strides:
        cond_data[cond] = {
            'strides':  np.vstack(all_strides),
            'roll_sds': all_roll_sds,
        }
    print(f"{COND_LABELS[cond]:12s}: n_strides={sum(len(s) for s in all_strides) if all_strides else 0}, "
          f"mean Roll SD={np.mean(all_roll_sds):.3f}°" if all_roll_sds else "")


# ── FIGURE 8: 2×2 그리드 ─────────────────────────────────────────────────────
fig8, axes = plt.subplots(2, 2, figsize=(13, 9), sharey=True, sharex=True)
fig8.suptitle(
    'Pelvis Roll Angle Across Full Stride — All Conditions\n'
    'Mean ± 1 SD band  |  Gray lines = individual strides',
    fontsize=13, fontweight='bold'
)

x = np.linspace(0, 100, 101)

for ax, cond in zip(axes.flatten(), CONDITIONS):
    color = COND_COLORS[cond]
    label = COND_LABELS[cond]

    if cond not in cond_data:
        ax.set_title(f'{label}\n(데이터 없음)')
        continue

    strides_arr  = cond_data[cond]['strides']
    roll_sds     = cond_data[cond]['roll_sds']
    mean_roll_sd = np.mean(roll_sds)

    mean_r = np.mean(strides_arr, axis=0)
    std_r  = np.std(strides_arr,  axis=0)

    # 개별 stride (서브셋)
    for s in strides_arr[::5]:
        ax.plot(x, s, color='lightgray', lw=0.4, alpha=0.35, zorder=1)

    # ±1 SD 밴드
    ax.fill_between(x, mean_r - std_r, mean_r + std_r,
                    alpha=0.25, color=color, zorder=2, label='±1 SD')

    # 평균선
    ax.plot(x, mean_r, color=color, lw=2.5, zorder=3, label='Mean')

    # 제로선
    ax.axhline(0, color='black', lw=0.7, alpha=0.40)

    # overall Roll SD 텍스트 (우상단)
    ax.text(0.97, 0.97,
            f'Overall Roll SD\n{mean_roll_sd:.2f}° (mean of n={len(roll_sds)})\n{ROLL_SD_CHANGE[cond]}',
            transform=ax.transAxes,
            ha='right', va='top', fontsize=8.5,
            bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.85, ec=color),
            color=color)

    ax.set_title(
        f'{label}  (n = {len(strides_arr)} strides, {len(roll_sds)} subjects)',
        fontsize=11
    )
    ax.set_xlim(0, 100)
    ax.grid(True, alpha=0.20)
    ax.legend(loc='upper left', fontsize=8.5, framealpha=0.9)

# 축 레이블
for ax in axes[1]:
    ax.set_xlabel('Stride (%)', fontsize=10)
for ax in axes[:, 0]:
    ax.set_ylabel('Pelvis Roll angle (°)', fontsize=10)

plt.tight_layout()
fig8_path = os.path.join(OUTPUT_DIR, 'fig08_pelvis_roll_across_stride.png')
fig8.savefig(fig8_path, dpi=150, bbox_inches='tight')
plt.close(fig8)
print(f'\nSaved: {fig8_path}')
