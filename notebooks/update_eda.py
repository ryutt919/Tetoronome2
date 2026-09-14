import nbformat

file_path = '01_data_structure_eda_executed.ipynb'

with open(file_path, 'r') as f:
    nb = nbformat.read(f, as_version=4)

new_code = """fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=False)
fig.suptitle('Segment별 Shank Resultant Acceleration 시계열 (Robust Peak Detection 적용)\\n(각 segment row의 타임스탬프 기준)',
            fontproperties=fm.FontProperties(family=FONT, size=12))

segs_data = {
    'foot  (발)':  df[df['source_segment']=='foot'].sort_values('iso_time'),
    'shank (무릎/정강이)': df[df['source_segment']=='shank'].sort_values('iso_time'),
    'hip   (골반)': df[df['source_segment']=='hip'].sort_values('iso_time'),
}
colors_seg = ['#2E86AB', '#E84855', '#3BB273']

from scipy import signal
# 필터 설정
GRAVITY = 9.81
FS = 60.0
nyq = 0.5 * FS
normal_cutoff = 15.0 / nyq
b, a = signal.butter(4, normal_cutoff, btype='low', analog=False)
min_dist_ms = 280.0

for ax, (label, sub), color in zip(axes, segs_data.items(), colors_seg):
    t = np.arange(len(sub)) / FS
    raw_acc = sub['shank_free_acceleration_resultant_m_s2'].values
    
    # 1. 신호 스무딩
    smoothed = signal.filtfilt(b, a, raw_acc)
    
    # 2. 동적 임계값 설정
    mean_val = np.mean(smoothed)
    std_val = np.std(smoothed)
    dynamic_height = max(1.5 * GRAVITY, mean_val + 1.2 * std_val)
    dynamic_prominence = max(0.5 * GRAVITY, std_val * 0.5)
    
    # 3. Peak 감지
    peaks, _ = signal.find_peaks(
        smoothed,
        height=dynamic_height,
        distance=int(FS * min_dist_ms / 1000.0),
        prominence=dynamic_prominence,
    )
    
    # 시각화: 원본은 회색으로 옅게, 필터된 신호는 자기 색깔로 진하게
    ax.plot(t, raw_acc, color='#BDC3C7', linewidth=0.6, alpha=0.5, label='Raw')
    ax.plot(t, smoothed, color=color, linewidth=1.0, alpha=0.9, label='Filtered')
    
    ax.axhline(dynamic_height, color='orange', linestyle='--', linewidth=1, label=f'Threshold ({dynamic_height/9.81:.1f}g)')
    
    ax.plot(t[peaks], smoothed[peaks], 'rv', markersize=5, label=f'peaks ({len(peaks)})')
    
    ax.set_title(label, fontproperties=fm.FontProperties(family=FONT, size=9))
    ax.set_ylabel('Resultant acc\\n(m/s²)', fontsize=8)
    ax.legend(fontsize=7, prop=fm.FontProperties(family=FONT, size=7), loc='upper right')
    ax.grid(alpha=0.4)

axes[-1].set_xlabel('시간 (s)', fontproperties=fm.FontProperties(family=FONT))
plt.tight_layout()
plt.show()
"""

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        if isinstance(source, list):
            source_str = "".join(source)
        else:
            source_str = source
            
        if "fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=False)" in source_str:
            cell['source'] = new_code

with open(file_path, 'w') as f:
    nbformat.write(nb, f)
