# A-to-B 보고서 피드백 반영 수정 계획

## 사용자 피드백 정리

| 구분 | 항목 | 사용자 피드백 | 실제 반영 방향 |
| --- | --- | --- | --- |
| 메트로놈/케이던스 증가 | 충격량 근사 | 선행연구는 cadence 증가 시 충격 감소 경향인데, 본 결과는 Peak g/RMS 증가라 설명이 부족함 | 속도는 피험자별 고정이므로 speed confound 삭제. 같은 속도에서 cadence를 급성으로 올렸는데 shock proxy가 증가한 결과를 미훈련 동기화 부담, landing timing/foot placement 조정 실패, IMU proxy 한계로 설명 |
| 메트로놈/케이던스 증가 | 족저굴곡 peak / ankle strategy | PF +34.7%가 왜 발생했는지 설명 부족. 빠른 박자를 억지로 맞추며 push-off가 증가한 것일 수 있음 | “push-off-like adjustment 가능성”은 쓰되, GRF/ankle power 미측정이므로 추진력 증가로 결론내지 않음. 빠른 cadence cue에 맞추는 급성 ankle strategy 변화로 해석 |
| 메트로놈/케이던스 증가 | 골반 자세 안정성 | 메트로놈 자체가 아니라 메트로놈으로 인한 갑작스러운 cadence 증가 결과로 봐야 함 | Roll SD 증가는 급성 cadence-up cue에 대한 비적응, timing task demand, trunk/pelvis control 부담 증가로 설명 |
| 메트로놈/케이던스 증가 | 골반 Pitch 누락 | Pitch 분석이 빠진 것 같으므로 실제 값을 보고 추가해야 함 | C→M Pitch SD `2.2455 → 2.2351`, `-0.46%`, `p=1.0`, `n=5`를 명시. Pitch는 사실상 불변/방향성 혼재, Roll은 `+4.26%`로 증가해 lateral/frontal 안정성 악화가 더 두드러졌다고 분리 |
| 메트로놈/케이던스 증가 | 보폭의 일관성 | Step Interval CV +5.09%도 메트로놈 부적응 문제로 이어지는 것 같음 | 외부 박자가 self-selected rhythm을 안정화하지 못하고 오히려 step timing variability를 증가시킨 acute synchronization burden으로 설명 |
| 테이핑 | 충격량 근사 | Tape에서 Peak g/RMS가 왜 감소했는지 근거 기반 설명 부족 | shock absorption 개선 단정 금지. 발목/후족부 움직임 제약과 landing pattern 일관화로 shank IMU proxy가 작아진 탐색 결과로 설명 |
| 테이핑 | 배측굴곡 억제 | posterior calf 2개 + anterior/tibialis anterior 1개 tape 배치 영향 반영 필요 | tape 배치가 sagittal ankle ROM constraint와 tibial advancement 제한을 만들었을 가능성을 Cordova/Chinn 근거와 연결 |
| 테이핑 | 족저굴곡 peak / ankle strategy | PF +5.78%도 tape 배치 영향일 수 있음 | push-off 강화 금지. DF 제한에 따른 ankle posture shift, tape 장력/촉각 cue, 센서/개인차 가능성으로 낮춰 해석 |
| 테이핑 | 보폭의 일관성 | Step CV -10.24%의 이유 설명 부족 | proprioception 향상 단정 금지. 기계적 안정화, tactile cue, perceived stability, shank-rearfoot coupling variability 감소 가능성을 새 근거로 설명 |

## Summary
- 수정 대상은 `analysis/0613/results_report_a_to_b_refined.html`의 section 4-6입니다.
- 같은 내용으로 `analysis/0613/results_report_a_to_b_refined_section4_to_end.md`도 갱신합니다.
- 수치, p-value, 표 구조는 유지하되, 각 행의 해석을 “결과가 왜 이렇게 나왔는가” 중심으로 재작성합니다.
- 중요한 전제: **속도는 피험자별로 고정**이었으므로, 메트로놈 결과는 “같은 속도에서 cadence만 급성 증가시킨 조건”으로 해석합니다.

## Key Changes
- 메트로놈/케이던스 증가:
  - 충격량 근사 행은 선행연구의 일반적 경향과 본 결과의 반대 방향을 먼저 제시합니다.
  - Peak g/RMS 증가는 미훈련 피험자의 급성 동기화 부담, 빠른 박자에 맞추는 landing timing 조정, Step CV 증가와 연결된 temporal control 불안정, shank IMU shock proxy 한계로 설명합니다.
  - PF +34.7%는 “빠른 박자를 맞추기 위한 push-off-like adjustment 또는 more plantarflexed ankle strategy 가능성”으로 쓰되, ankle power/GRF를 측정하지 않았다는 제한을 붙입니다.
  - 골반 안정성 행은 Pitch와 Roll을 분리합니다: Pitch SD `-0.46%`는 거의 불변, Roll SD `+4.26%`는 증가. 따라서 골반 안정화 효과는 없고, lateral/frontal plane 흔들림 증가가 더 핵심이라고 씁니다.
  - Step CV +5.09%는 메트로놈 cue가 안정화 cue가 아니라 acute task demand로 작동한 결과로 해석합니다.

- 테이핑:
  - Tape shock proxy 감소는 shock absorption 직접 효과가 아니라, ankle ROM constraint와 landing repeatability 변화가 IMU peak/RMS에 반영된 탐색 결과로 씁니다.
  - posterior calf 2개 + anterior/tibialis anterior 1개 배치를 명시하고, 이 배치가 발목 sagittal plane 움직임을 기계적/촉각적으로 제한했을 가능성을 설명합니다.
  - DF -4.07%는 dorsiflexion ROM 제한 근거와 연결합니다.
  - PF +5.78%는 작은 변화이며 직접 근거가 약하므로, DF 제한에 따른 posture shift 또는 개인차로 제한합니다.
  - Step CV -10.24%는 proprioceptive acuity 향상으로 쓰지 않고, ankle-rearfoot coupling variability와 perceived stability 변화 가능성으로만 기술합니다.

## Evidence Updates
- 기존 참고문헌 `[1]~[15]`는 유지합니다.
- 메트로놈 관련 근거:
  - Heiderscheit et al. 2011: 고정 속도 step rate 증가 시 step length, braking impulse, impact transient 감소.
  - Anderson et al. 2022: step rate 증가의 부하 감소/무변화 경향과 effort/awkwardness 증가 가능성.
  - Cronström et al. 2022: metronome cue가 stride time variability를 증가시킬 수 있음.
  - Terrier & Deriaz 2012: rhythmic cueing이 stride-to-stride variability dynamics를 재조직할 수 있음.
- 테이핑 관련 새 근거:
  - Riemann et al. 2002: ankle support가 peak impact force 도달 시간을 줄일 수 있음.
  - Niu et al. 2016: prophylactic ankle support가 충격 buffering을 항상 개선하지 않음.
  - Hall et al. 2016: tape/brace의 perceived stability 및 inversion ROM/velocity 영향.
  - Herb, Chinn & Hertel 2014: taping 후 shank-rearfoot coupling variability 감소.
  - Yin & Wang 2020 또는 Tsikopoulos et al. 2020: postural control/proprioception 효과가 제한적임을 보강.

## Test Plan
- 수정 후 `rg`로 과잉 해석 문구를 확인합니다:
  - `속도 증가`, `speed increase`, `shock absorption`, `propulsive force`, `ankle power 증가`, `proprioception 개선`
- 수정 후 `rg`로 필수 반영 문구를 확인합니다:
  - `고정 속도`, `급성`, `미훈련`, `task demand`, `Pitch SD -0.46%`, `Roll SD +4.26%`, `posterior calf`, `tibialis anterior`, `shock proxy`, `탐색적`
- HTML 참고문헌 번호가 기존 순서를 유지하고, 새 문헌이 뒤에 순차적으로 추가됐는지 확인합니다.
- MD 파일이 HTML section 4부터 끝까지의 수정 내용과 일치하는지 확인합니다.

## Assumptions
- Pitch C→M 값은 `results/statistical_tests.csv` 기준으로 사용합니다: `n=5`, `2.2455 → 2.2351`, `-0.46%`, `p=1.0`.
- 박민규 Metro Pitch 값은 누락되어 C→M Pitch 분석에는 포함하지 않습니다.
- 통계 결과, 변화율, p-value, 표의 수치 자체는 수정하지 않고 해석 문장만 수정합니다.
- `pipeline_summary_a_to_b_refined.html`은 이번 수정 범위에서 제외합니다.
