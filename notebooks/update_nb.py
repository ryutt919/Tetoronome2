import nbformat

with open('02_raw_data_visualization.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

markdown_code = """
## 6. 동적 임계값 및 필터링(Robust Peak Detection) 검증
새롭게 도입한 Low-pass Filter(15Hz)와 동적 임계값(Dynamic threshold)이 이중 피크(Double-counting) 문제를 어떻게 해결했는지 시각적으로 확인합니다.
"""
nb.cells.append(nbformat.v4.new_markdown_cell(source=markdown_code))

code = """
from scipy import signal
GRAVITY = 9.81
FS = 60.0

# 1. 필터링 및 동적 임계값 적용
nyq = 0.5 * FS
normal_cutoff = 15.0 / nyq
b, a = signal.butter(4, normal_cutoff, btype='low', analog=False)

raw_acc = sub_foot['shank_free_acceleration_resultant_m_s2'].values
smoothed = signal.filtfilt(b, a, raw_acc)

mean_val = np.mean(smoothed)
std_val = np.std(smoothed)
dynamic_height = max(1.5 * GRAVITY, mean_val + 1.2 * std_val)
dynamic_prominence = max(0.5 * GRAVITY, std_val * 0.5)
min_dist_ms = 280.0

peaks, _ = signal.find_peaks(
    smoothed,
    height=dynamic_height,
    distance=int(FS * min_dist_ms / 1000.0),
    prominence=dynamic_prominence,
)

# 2. 시각화 비교
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(t, raw_acc, color='#BDC3C7', linewidth=1, alpha=0.7, label='Raw Data (원본)')
ax.plot(t, smoothed, color='#2980B9', linewidth=1.5, label='Filtered (15Hz Low-pass)')

ax.axhline(dynamic_height, color='orange', linestyle='--', linewidth=1.5, label=f'Dynamic Threshold ({dynamic_height/9.81:.1f}g)')
ax.plot(t[peaks], smoothed[peaks], 'rv', markersize=8, label=f'Detected Peaks ({len(peaks)})')

ax.set_title('Robust Peak Detection: 원본 가속도 vs 필터링 + 동적 임계값 적용 후', fontproperties=fm.FontProperties(family=FONT, size=14, weight='bold'))
ax.set_ylabel('Resultant Acc (m/s²)', fontproperties=fm.FontProperties(family=FONT))
ax.set_xlabel('시간 (초)', fontproperties=fm.FontProperties(family=FONT))
ax.legend(prop=fm.FontProperties(family=FONT))
ax.grid(alpha=0.5)

plt.tight_layout()
plt.show()
"""
nb.cells.append(nbformat.v4.new_code_cell(source=code))

with open('02_raw_data_visualization.ipynb', 'w') as f:
    nbformat.write(nb, f)
