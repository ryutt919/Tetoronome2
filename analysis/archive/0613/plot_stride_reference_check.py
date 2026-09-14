"""
fig06: Stride start 기준 확인
  - shank acc + ankle angle 같은 시간축으로, impact peaks 표시
  - 안승진 control 약 4초 구간

fig07: Control vs Metro raw time domain 비교
  - 정규화(%) 없이 실제 ms 시간축
  - 같은 안승진 피험자, 4초 구간 나란히
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

def butter_lp(data, cutoff=15, fs=60, order=4):
    b, a = butter(order, cutoff / (fs / 2), btype='low')
    return filtfilt(b, a, data)

def iqr_filter(acc, peaks):
    if len(peaks) < 4:
        return peaks
    v = acc[peaks]
    q1, q3 = np.percentile(v, 25), np.percentile(v, 75)
    iqr = q3 - q1
    return peaks[(v >= q1 - 1.5*iqr) & (v <= q3 + 1.5*iqr)]

def detect_full_stride_impacts(acc, fs=60):
    p0, _ = find_peaks(acc, distance=int(0.200*fs), prominence=1.962)
    p0 = iqr_filter(acc, p0)
    if len(p0) < 4:
        return p0
    med = np.median(np.diff(p0))
    new_dist = int(med * 1.6) if med < 0.40*fs else int(med * 0.80)
    p1, _ = find_peaks(acc, distance=new_dist, prominence=1.962)
    p1 = iqr_filter(acc, p1)
    return p1 if len(p1) >= 4 else p0

def load_foot(subject, condition):
    path = os.path.join(DATA_ROOT, subject, f"{subject}_{condition}.csv")
    if not os.path.exists(path):
        return None
    df = pd.read_csv(path)
    return df[df['source_segment'] == 'foot'].copy().reset_index(drop=True)


# ── FIGURE 6: stride 시작 기준 확인 ─────────────────────────────────────────
#   panel 1: shank acceleration + impact peaks
#   panel 2: ankle angle + stride boundaries (수직선)

subj = '안승진'
fd   = load_foot(subj, 'control')

ankle_col = 'ankle_dorsiflexion_plantarflexion_deg'
acc_col   = 'shank_free_acceleration_resultant_m_s2'

ankle_f = butter_lp(fd[ankle_col].values)
acc_f   = butter_lp(fd[acc_col].values)
impacts = detect_full_stride_impacts(acc_f, fs=FS)

# 중간 구간 4초
mid   = len(acc_f) // 2
win   = int(4 * FS)
s0    = max(0, mid - win // 2)
e0    = s0 + win
t_s   = np.arange(win) / FS          # 초 단위
acc_w = acc_f[s0:e0]
ank_w = ankle_f[s0:e0]

# 창 안의 impact peaks (상대 인덱스)
imp_in = impacts[(impacts >= s0) & (impacts < e0)] - s0

fig6, (ax_acc, ax_ank) = plt.subplots(2, 1, figsize=(13, 7), sharex=True)
fig6.suptitle(
    f'Stride Start Reference — {subj}, Control  (4 s window)\n'
    'Impact peaks (▼) = detected foot strikes = stride boundaries',
    fontsize=12, fontweight='bold'
)

# --- panel 1: acc ---
ax_acc.plot(t_s, acc_w, color='#444', lw=1.2, label='Shank acc (filtered)', zorder=2)
ax_acc.scatter(t_s[imp_in], acc_w[imp_in],
               color='crimson', s=100, zorder=5, marker='v',
               label=f'Impact peaks (n={len(imp_in)})', clip_on=False)
for ip in imp_in:
    ax_acc.axvline(t_s[ip], color='crimson', lw=0.8, ls='--', alpha=0.4, zorder=1)
ax_acc.set_ylabel('Shank acc (m/s²)', fontsize=11)
ax_acc.legend(loc='upper right', fontsize=9)
ax_acc.grid(True, alpha=0.22)
ax_acc.set_title('Panel 1: Shank Resultant Acceleration', fontsize=10, loc='left')

# --- panel 2: ankle ---
ax_ank.plot(t_s, ank_w, color='#1565C0', lw=1.5, label='Ankle DF/PF angle', zorder=2)
ax_ank.axhline(0, color='black', lw=0.8, alpha=0.4)

# stride 구간 음영 + PF peak 표시
colors_stripe = ['#BBDEFB', '#E3F2FD']
for k, ip in enumerate(imp_in[:-1]):
    ie = imp_in[k+1]
    seg = ank_w[ip:ie]
    pf_idx = int(np.argmin(seg))
    pf_val = seg[pf_idx]
    pf_t   = t_s[ip + pf_idx]
    pf_pct = pf_idx / len(seg) * 100

    ax_ank.axvspan(t_s[ip], t_s[ie], alpha=0.18,
                   color=colors_stripe[k % 2], zorder=0)
    ax_ank.axvline(t_s[ip], color='crimson', lw=0.8, ls='--', alpha=0.4, zorder=1)
    ax_ank.scatter([pf_t], [pf_val],
                   color='crimson', s=70, zorder=5, label='PF peak' if k == 0 else '')
    ax_ank.annotate(f'{pf_pct:.0f}%',
                    xy=(pf_t, pf_val),
                    xytext=(pf_t + 0.03, pf_val - 4),
                    fontsize=8, color='crimson',
                    arrowprops=dict(arrowstyle='->', color='crimson', lw=0.7))

ax_ank.set_ylabel('Ankle angle (°)\n← PF    DF →', fontsize=11)
ax_ank.set_xlabel('Time (s)', fontsize=11)
ax_ank.legend(loc='upper right', fontsize=9)
ax_ank.grid(True, alpha=0.22)
ax_ank.set_title('Panel 2: Ankle DF/PF Angle  |  Blue shade = one full stride  |  Red dot = PF peak',
                 fontsize=10, loc='left')
ax_ank.set_xlim(t_s[0], t_s[-1])

plt.tight_layout()
fig6.savefig(os.path.join(OUTPUT_DIR, 'fig06_stride_reference_check.png'),
             dpi=150, bbox_inches='tight')
plt.close(fig6)
print('Saved: fig06')


# ── FIGURE 7: Control vs Metro raw time domain 비교 ─────────────────────────
#   같은 피험자, 4초, 실제 ms 시간축
#   위: acc (both conditions), 아래: ankle angle (both conditions)
#   stride boundaries 표시

fig7, axes7 = plt.subplots(2, 2, figsize=(15, 7), sharey='row')
fig7.suptitle(
    f'Control vs Metro — Raw Time Domain  ({subj}, 4 s window)\n'
    'Top: Shank Acc  |  Bottom: Ankle Angle  |  ▼ = detected stride start',
    fontsize=12, fontweight='bold'
)

for col_idx, cond in enumerate(['control', 'metro']):
    fd_c = load_foot(subj, cond)
    if fd_c is None:
        continue

    ankle_c = butter_lp(fd_c[ankle_col].values)
    acc_c   = butter_lp(fd_c[acc_col].values)
    imp_c   = detect_full_stride_impacts(acc_c, fs=FS)

    mid_c = len(acc_c) // 2
    s_c   = max(0, mid_c - win // 2)
    e_c   = s_c + win
    t_c   = np.arange(win) / FS * 1000   # ms 단위
    acc_w_c = acc_c[s_c:e_c]
    ank_w_c = ankle_c[s_c:e_c]
    imp_w_c = imp_c[(imp_c >= s_c) & (imp_c < e_c)] - s_c

    color_line = '#1565C0' if cond == 'control' else '#C62828'
    color_peak = 'crimson'
    label_cond = 'Control' if cond == 'control' else 'Metro'

    # acc panel
    ax_a = axes7[0, col_idx]
    ax_a.plot(t_c, acc_w_c, color=color_line, lw=1.3, label=label_cond)
    ax_a.scatter(t_c[imp_w_c], acc_w_c[imp_w_c],
                 color=color_peak, s=90, zorder=5, marker='v')
    for ip in imp_w_c:
        ax_a.axvline(t_c[ip], color=color_peak, lw=0.8, ls='--', alpha=0.35)
    ax_a.set_title(f'{label_cond}  (stride boundaries ▼)', fontsize=11)
    if col_idx == 0:
        ax_a.set_ylabel('Shank acc (m/s²)', fontsize=10)
    ax_a.legend(loc='upper right', fontsize=9)
    ax_a.grid(True, alpha=0.22)

    # interval 표시
    if len(imp_w_c) >= 2:
        ivs = np.diff(imp_w_c) / FS * 1000
        ymax = ax_a.get_ylim()[1] if ax_a.get_ylim()[1] != 1 else acc_w_c.max()
        for k in range(len(imp_w_c) - 1):
            mid_t = (t_c[imp_w_c[k]] + t_c[imp_w_c[k+1]]) / 2
            ax_a.text(mid_t, acc_w_c.max() * 0.95,
                      f'{ivs[k]:.0f}ms', ha='center', va='top',
                      fontsize=8, color=color_line, fontweight='bold')

    # ankle panel
    ax_k = axes7[1, col_idx]
    ax_k.plot(t_c, ank_w_c, color=color_line, lw=1.5, label=label_cond)
    ax_k.axhline(0, color='black', lw=0.7, alpha=0.4)

    for k, ip in enumerate(imp_w_c[:-1]):
        ie = imp_w_c[k+1]
        seg = ank_w_c[ip:ie]
        pf_idx = int(np.argmin(seg))
        pf_t_ms = t_c[ip + pf_idx]
        pf_pct  = pf_idx / len(seg) * 100
        ax_k.scatter([pf_t_ms], [seg[pf_idx]],
                     color=color_peak, s=60, zorder=5,
                     label='PF peak' if k == 0 else '')
        ax_k.text(pf_t_ms, seg[pf_idx] - 4,
                  f'{pf_pct:.0f}%', ha='center', fontsize=7.5, color=color_peak)
        ax_k.axvline(t_c[ip], color=color_peak, lw=0.8, ls='--', alpha=0.35)

    ax_k.set_xlabel('Time (ms)', fontsize=10)
    if col_idx == 0:
        ax_k.set_ylabel('Ankle angle (°)\n← PF    DF →', fontsize=10)
    ax_k.legend(loc='upper right', fontsize=9)
    ax_k.grid(True, alpha=0.22)
    ax_k.set_xlim(t_c[0], t_c[-1])

plt.tight_layout()
fig7.savefig(os.path.join(OUTPUT_DIR, 'fig07_control_vs_metro_raw_timedomain.png'),
             dpi=150, bbox_inches='tight')
plt.close(fig7)
print('Saved: fig07')
