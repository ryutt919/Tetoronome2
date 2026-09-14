# Analysis — Tetoronome

## Component Status
각 컴포넌트의 현재 상태를 설명합니다. 작업 중에 직접 업데이트하세요.
중복 내용을 기재하지 마세요.

### Pipeline & Analysis Summary HTML
- **현재 값/로직**: `pipeline.py`는 피크 감지에 `Prominence 0.2g` 및 IQR 필터(동적 높이 없음)를 사용합니다. 케이던스 및 충격 계산에는 15Hz Butterworth 필터링을 적용합니다. 충격 지표(RMS, Impulse)는 `Resultant` 가속도를 사용하여 `shank`에서만 계산합니다. 골반 운동학은 ROM 대신 수직/수평 안정성(SD, Vel RMS)에 집중합니다. 발목 운동학은 보행 분절별 최대 배측굴곡 및 저측굴곡(절댓값)을 계산합니다. `pipeline_summary.html`이 이러한 논리 변경 사항을 문서화합니다.
- **구현**: 정확한 수학적 기준에 맞게 `pipeline.py`, `visualize.py`, `run_analysis.py`를 업데이트했습니다. 근거(예: 15Hz 한계, Resultant 사용, CV% 의미)를 명확히 설명하도록 `pipeline_summary.html`을 업데이트했습니다.
- **관련 파일**: `analysis/pipeline_summary.html`, `analysis/run_analysis.py`, `analysis/pipeline.py`, `analysis/visualize.py`
- **근거**: 사용자가 최종 방법론 보고서를 위해 심층 물리적 논리(Resultant, 15Hz 제한) 및 특정 지표 업데이트(Shank 전용, Ankle Peak, Pelvis 안정성)를 요청했습니다.

---

## Change History
델타만 기록합니다. Component Status에 이미 있는 내용은 반복하지 마세요.

| Timestamp | Task | Change Summary |
|-----------|------|----------------|
| 2026-05-31 20:08 | Create pipeline summary HTML | Pipeline Summary HTML → None → Created `pipeline_summary.html` (to visually summarize the analysis pipeline components) |
| 2026-05-31 20:15 | Exhaustive methodology update | Pipeline Summary HTML → High-level summary → Detailed methodology breakdown (peak detection, kinematics, stats) with light theme and larger fonts. |
| 2026-05-31 20:52 | Pipeline refactoring & HTML update | Pipeline & Analysis HTML → Resultant & Shank impact focus, Ankle Peak, Pelvis SD → Refactored metrics and detailed HTML explanations |
| 2026-05-31 21:00 | Add IQR and Butterworth filters | Pipeline & Analysis HTML → IQR on cadence/CV, Butterworth on pelvis/ankle → Updated calculations and HTML docs |
| 2026-05-31 21:15 | Add academic references to HTML | Pipeline Summary HTML → Added citations for 15Hz filter and 280ms peak distance |
| 2026-05-31 21:26 | Add cumulative load reference | Pipeline Summary HTML → Added PlayerLoad citation and continuous integration rationale |
| 2026-05-31 21:30 | Add CV vs SD rationale | Pipeline Summary HTML → Added statistical and biomechanical rationale for CV and SD |
| 2026-05-31 21:36 | Add PlayerLoad critique to HTML | Pipeline Summary HTML → Updated Jerk vs Impulse explanation and references |
| 2026-05-31 21:40 | Update stats criteria | Pipeline Summary HTML → Added criteria for choosing between t-test and Wilcoxon |
| 2026-05-31 22:15 | Full data analysis (N=6) | Pipeline & Visualize → Forced Wilcoxon, added Cohen's d, generated results_report.html |
| 2026-05-31 22:42 | Update Spaghetti plots | visualize.py, HTML → Split plots by metric, custom X-axis order |
| 2026-05-31 22:56 | Refactor Ankle IQR and Conclusions | pipeline.py, visualize.py, HTML → Applied IQR to ankle peaks, Korean plot labels, structured conclusions |
| 2026-05-31 23:07 | Update Cadence and Add Median Plots | pipeline.py, visualize.py, HTML → Use manual cadence from txt, compute medians for peak_g and ankle ROM, and show side-by-side plots |
| 2026-05-31 23:10 | Update Visualizations and HTML | visualize.py, HTML → Add separate Dorsi/Plantar plots, split heatmap into two large plots, remove boxplot section |
| 2026-05-31 23:13 | Jin Hyun-jun Simulation & Heatmap Update | pipeline.py, HTML → Exclude ankle Tape+Metro data for JHJ, update HTML highlight to C → T+M Cadence |
| 2026-05-31 23:13 | Fix encoding corruption | 01_analysis.md → UTF-16 LE 혼합 인코딩 → UTF-8로 재저장, 깨진 한글 복원 |
