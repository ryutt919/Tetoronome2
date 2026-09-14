import pandas as pd
import numpy as np

# Load the latest results
from pipeline import run_all_analyses

# Re-run analyses to get the latest dataframe (including NaN for JHJ Tape+Metro)
df = run_all_analyses()

# Metrics to include in the table
metrics = [
    ("cadence_steps_per_min", "케이던스 (steps/min)"),
    ("shank_mean_peak_g", "Peak g (Shank) - 평균"),
    ("shank_median_peak_g", "Peak g (Shank) - 중앙값"),
    ("step_interval_cv_pct", "Step CV%"),
    ("pelvis_pitch_sd_deg", "골반 수직 안정성 (Pitch SD)"),
    ("pelvis_roll_sd_deg", "골반 측면 안정성 (Roll SD)"),
    ("ankle_dp_pf_rom_deg", "Ankle DF/PF ROM (°) - 평균 피크차"),
    ("ankle_median_dp_pf_rom_deg", "Ankle DF/PF ROM (°) - 중앙 피크차"),
    ("ankle_mean_dorsiflexion_peak_deg", "Ankle Dorsiflexion (°) - 평균"),
    ("ankle_median_dorsiflexion_peak_deg", "Ankle Dorsiflexion (°) - 중앙값"),
    ("ankle_mean_plantarflexion_peak_deg", "Ankle Plantarflexion (°) - 평균"),
    ("ankle_median_plantarflexion_peak_deg", "Ankle Plantarflexion (°) - 중앙값"),
]

# Create a pivot table for each metric
html_tables = []
for col_name, title in metrics:
    if col_name not in df.columns:
        continue
    
    pivot = df.pivot_table(index="subject", columns="condition_label", values=col_name, aggfunc="first")
    # Reorder columns
    cols = ["Control", "Tape", "Metro", "Tape+Metro"]
    pivot = pivot[[c for c in cols if c in pivot.columns]]
    
    # Format to 2 decimal places
    pivot = pivot.applymap(lambda x: f"{x:.2f}" if pd.notnull(x) else "N/A")
    
    # Generate HTML
    table_html = pivot.to_html(classes="table table-bordered table-striped", border=0, justify="center")
    
    # Add title
    html_tables.append(f"<h3>{title}</h3>\n<div class='table-responsive'>\n{table_html}\n</div><br>")

all_tables_html = "\n".join(html_tables)

# Now, read the results_report.html and replace Section 2
with open("analysis/results_report.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
# Regex to find Section 2 and everything up to Section 3
pattern = r"<h2>2\. 유의미한 결과 하이라이트.*?</h2>.*?<h2>3\. 통계 검정 히트맵"
replacement = f"<h2>2. 스파게티 플롯 데이터 요약표</h2>\n<p>각 피험자별 시각화(스파게티 플롯)에 사용된 실제 데이터 수치입니다.</p>\n{all_tables_html}\n<h2>3. 통계 검정 히트맵"

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open("analysis/results_report.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Table successfully injected and Section 2 replaced.")
