# Tetoronome — 메트로놈/테이핑 러닝 개입 IMU 분석

- 러닝 중 **메트로놈(케이던스 유도)** 과 **발목 테이핑**이 충격량, 관절 운동학, 보행 안정성에 미치는 효과를 IMU 3개(발/정강이/골반)로 측정한 N=6 파일럿 연구임.
- 데이터 수집 웹앱부터 지표 산출, 통계 검정, 시각화까지 분석 파이프라인을 Python으로 직접 구현함.

## 1. 연구 설계

| 항목 | 내용 |
|---|---|
| 피험자 | 6명, P01–P06 (건강한 성인, 개인별 고정 러닝 속도 13~16km/h 트레드밀) |
| 조건 (Within-subject) | Control / Metro / Tape / Tape+Metro (피험자별 무작위 순서) |
| 센서 | Xsens 계열 IMU 3개 — `foot`(발), `shank`(정강이), `hip`(골반), 공통 샘플링레이트 60Hz |
| 측정 항목 | shank 3축 자유가속도(+resultant), 각 부위 quaternion 기반 자세각 |
| 개입 가설 | 메트로놈: 충격량↓, 골반 안정성↑, 보폭 일관성↑ [1] / 테이핑: 충격량↓, 족저굴곡↑, 보폭 일관성↑ [2][3] |

| 그림 | 설명 |
|---|---|
| ![실험 설계](보고용%20figure/실험%20설계%201.png) | 웜업 3분 → 점진적 강도 증가 → RPE 기준 cadence 측정 → 2분 러닝 블록, 조건 간 충분한 휴식을 두고 4개 조건을 무작위 순서로 진행 |
| ![IMU 부착](보고용%20figure/IMU%20부착.png) | IMU 3개를 골반(pelvis), 정강이(shank), 발(foot)에 벨트/테이프로 고정 부착 |
| ![테이핑 예시](보고용%20figure/테이핑%20예시.png) | 발목 테이핑 개입 조건의 실제 시술 예시 (발목 안정화 패턴) |

## 2. 분석 파이프라인

### 데이터 수집

- Xsens DOT IMU 3개를 Web Bluetooth로 브라우저에 직접 스트리밍하는 웹앱([`tools/xsens_dot_streaming_app.html`](tools/xsens_dot_streaming_app.html))을 만들어 수집함. 별도 프로그램 설치 없이 Chrome/Edge에서 페어링, 측정, CSV 저장까지 처리함.
- 각 센서는 자세(quaternion w/x/y/z)와 free acceleration(x/y/z)을 BLE 알림마다 전송함.
- 발목각은 foot/shank 쿼터니언의 상대 회전(`conjugate(shank) × foot`)을 axis-angle로 변환해 계산하고, 골반각은 hip 쿼터니언을 같은 방식으로 변환함. 오일러각의 짐벌락과 축 순서 문제를 피하려고 쿼터니언을 그대로 사용함.
- 측정 직전 quiet standing 자세의 쿼터니언을 기준으로 저장하고, 이후 값을 이 기준에 대한 상대 회전으로 계산해 중립 자세를 0°로 맞춤.
- 화면 표시에는 ±180° 경계에서 값이 튀지 않도록 각도 차를 -180~180°로 감싸는 circular 저역통과 필터를 사용함. CSV에는 raw, unfiltered, filtered 값을 모두 저장하고, 분석 단계에서 4차 Butterworth 15Hz(zero-phase)로 다시 필터링함.
- 가속도는 shank IMU에서만 측정했으며, foot/hip 행의 가속도 값은 가장 가까운 시각의 shank 값임.
- 현장에서 부착 상태를 확인할 수 있도록 GCT와 케이던스를 실시간으로 표시함. 통계에는 오프라인 분석 결과만 사용함.

```
data/{피험자}/{피험자}_{조건}.csv
        │  (60Hz, source_segment ∈ {foot, shank, hip})
        ▼
analysis/pipeline.py      ── 지표 계산 (피험자 × 조건 단위)
        │
        ├─ load_subject_condition()      CSV 로드 + segment 분리
        ├─ _detect_impact_peaks()        충격 피크 검출
        ├─ compute_cadence()             케이던스
        ├─ compute_impact_all_segments() 충격량 지표 (shank)
        ├─ compute_ground_contact_variability()  보폭 일관성 (CV%)
        ├─ compute_pelvis_kinematics()   골반 안정성 (Pitch/Roll SD)
        ├─ compute_ankle_kinematics()    발목 DF/PF, Inv/Ev ROM
        └─ run_statistical_tests()       Wilcoxon + Cohen's d
        ▼
results/metrics_by_condition.csv, statistical_tests.csv, subject_condition_table.csv
        ▼
analysis/visualize.py  ──▶  results/figures/*.png (스파게티 플롯, 히트맵, 조건별 효과 그래프)
        ▼
analysis/run_analysis.py  ── 위 과정을 한 번에 실행하고 콘솔에 핵심 결과 요약 출력
```

### 실행 방법

```bash
cd analysis
pip install numpy pandas scipy matplotlib seaborn
python run_analysis.py
```

### 신호 처리 로직

| 처리 | 방법 | 근거 |
|---|---|---|
| 저역통과 필터 | 4차 Butterworth, cutoff 15Hz | 보행 신호 주성분은 보존하면서 STA(soft tissue artifact), 부착 노이즈 억제 — 단, 저역통과 필터만으로는 착지 충격 시 발생하는 STA를 완전히 제거하지 못한다는 한계가 있음 [4] |
| 충격 피크 검출 | `scipy.find_peaks`, 고정 prominence 0.2g, 최소 간격 280ms | 개인별 절대 충격량 차이를 흡수하기 위해 height 대신 prominence 사용, 280ms로 이중 피크(double peak) 방지 |
| 이상치 제거 | Tukey IQR (1.5×IQR) | 피크 높이, 관절각 최대치 모두에 적용해 센서 튐값 제거 |
| 케이던스 | 수기 기록값으로 최종 대체 | 실험 중 실측한 케이던스를 정답값으로 사용 |
| 통계 검정 | Wilcoxon signed-rank (양측) + Cohen's d | N=6이라 정규성 가정이 어려워 비모수 검정 사용. 양측 최소 p값이 0.031이므로 효과크기, 변화율, 개인별 추이를 함께 확인 |

| 그림 | 설명 |
|---|---|
| ![피크 검출 20초 예시](assets/peak_detection_example_20s.png) | 원본 피크 예시 (P04 / Control / shank) |
| ![이중 피크 방지 + IQR 필터](assets/preprocessing_peak_detection.png) | 0-5초 확대: 회색=원신호, 검정=15Hz 스무딩, 파란 점=최종 피크, 주황 원=IQR로 걸러진 후보 — 스무딩과 280ms 최소 간격이 없으면 착지 후 잔진동이 별도 걸음으로 오검출됨 |
| ![IQR 필터 개념](assets/iqr_filter_explanation.png) | 후보 피크 높이 분포에서 Q1-1.5×IQR ~ Q3+1.5×IQR 범위를 벗어난 값(노란 점)만 이상치로 제외하는 구조 |

## 3. 결과 요약

| 개입 | 가설 | 실측 결과 (Control 대비) | 가설 지지 여부 |
|---|---|---|---|
| 메트로놈 | 충격량 ↓ | Peak g **+7.5%** (n.s.) | ❌ 반대 방향 |
| 메트로놈 | 골반 안정성 ↑ | Roll SD +4.3%, Pitch SD 거의 불변 | ❌ 반대 방향 |
| 메트로놈 | 보폭 일관성 ↑ | Step CV% **+5.1%** (n.s.) | ❌ 반대 방향 |
| 테이핑 | 충격량 ↓ | Peak g −1.8% (n.s.) | ✅ 방향 일치 |
| 테이핑 | 족저굴곡 ↑ | Plantarflexion +5.8% (n.s.) | ✅ 방향 일치 |
| 테이핑 | 보폭 일관성 ↑ | Step CV% −10.2% (n.s.) | ✅ 방향 일치 |

- p<0.05 결과는 **Control→Tape+Metro 케이던스 증가**와 **Tape→Tape+Metro Step CV% 증가** 두 건뿐임.
- 두 건 모두 p=.031로, N=6 양측 Wilcoxon에서 나올 수 있는 최소 p값임.

| 그림 | 설명 |
|---|---|
| ![변화율 히트맵](assets/heatmap_pctchange.png) | 4개 비교(C→M, C→T, C→T+M, T→T+M) × 10개 지표 전체 변화율 한눈에 비교 |
| ![p-value 히트맵](assets/heatmap_pvalue.png) | 같은 비교의 Wilcoxon p-value — 녹색(0.031) 두 칸을 제외하면 전부 비유의 |
| ![케이던스 개인 추이](assets/spaghetti_cadence.png) | 6명 전원이 Metro 조건에서 케이던스가 오르는 방향으로 일관되게 반응 — 유의성이 나온 이유 |
| ![Step CV% 개인 추이](assets/spaghetti_step_cv.png) | Tape에서 낮았던 Step CV%가 Tape+Metro에서 다시 오르는 패턴이 대부분 피험자에서 반복 |
| ![Shank Peak g 개인 추이](assets/spaghetti_shank_peak_g.png) | 케이던스가 오른 피험자일수록 오히려 충격 피크(g)도 함께 오르는 경향 — 아래 해석의 근거 |

**해석**

- 메트로놈 조건의 충격량 증가는 IMU 기반 shock proxy가 실제 지면반력과 다르게 반응한 결과에 가까움. Force-plate 연구에서는 cadence를 5~10% 올리면 step length, braking impulse, impact transient가 줄어든다고 보고했으나 [1], 본 연구의 shank 가속도는 반대로 상승함.
- cadence 증가 시 medial gastrocnemius 활성 증가 [5], peak ankle dorsiflexion 감소 [6], 착지 시 더 plantarflexed된 발목 자세 [7]가 보고됨. 가속도계가 지면 충격보다 발목/종아리 근육의 반응 변화를 함께 반영했을 가능성이 있음.
- 메트로놈 조건의 Step CV% 증가도 같은 맥락임. 메트로놈은 걸음 간격 변동계수를 줄이지 못하고 [8], 고령자 보행에서는 stride time 변동성을 오히려 늘린다는 보고가 있음 [9].
- 러닝은 걷기보다 박자 동기화가 덜 이뤄지고 [10], 외부 박자를 따라가려는 과잉보정(overcorrection)이 anti-persistent 패턴을 만든다는 설명도 있음 [11]. 메트로놈은 케이던스를 유의하게 올렸지만 보폭 일관성은 개선하지 못함.
- 테이핑 조건의 족저굴곡, 보폭 일관성 개선 방향은 발목 키네시오 테이핑이 peak torque/power와 고유수용성 감각을 향상시킨다는 보고와 일치함 [12][13].
- IMU 가속도는 지면반력의 근사치(proxy)이며 직접 측정값이 아님. 이번 분석에서 가장 크게 확인된 점임.

## 4. 문제와 해결

- **이중 피크**
  - 착지 충격 뒤 잔진동 때문에 한 걸음이 두 걸음으로 검출됨.
  - 15Hz Butterworth 스무딩 후 height 대신 prominence(0.2g)와 최소 간격 280ms로 검출함. 피험자마다 절대 충격량이 달라 height 기준은 오탐이 많았음.

- **편측 IMU로 케이던스 검출 불가**
  - 한쪽 다리에만 센서가 있어 자동 검출 케이던스가 실측과 맞지 않음.
  - 실험 중 직접 측정한 케이던스로 대체하고, 자동 검출 피크는 걸음 간격 CV% 계산에만 사용함.

- **발목 각도 이상치**
  - P05의 Tape+Metro 조건에서 발목 각도가 다른 조건/피험자와 비교해 설명되지 않는 값으로 튐. 센서 이탈로 추정함.
  - 해당 조건의 발목 지표만 분석에서 제외함.

## 5. 한계

- 골반 IMU에서 예상과 다른 값이 많이 나옴. 이후 밴드를 IMU 위로 덮어 고정하면 샘플링레이트가 약 50% 떨어지고 튐값과 결측이 더 자주 생긴다는 것을 발견함.
- 연부조직 진동(STA)은 저역통과 필터로 완전히 제거되지 않음 [4].
- 트레드밀 금속 프레임의 자기장 왜곡과 달리기 충격이 겹치면 자세 추정에서 Roll/Yaw 오차와 자이로 드리프트가 누적될 수 있음 [14][15][16].

## 6. 폴더 구조

```
tetoronome-portfolio/
├── assets/                    # README에 직접 삽입되는 그림 (익명화된 결과/파이프라인 그림)
├── tools/
│   └── xsens_dot_streaming_app.html  # IMU 3개 BLE 연결, 실시간 각도 계산, CSV 로깅용 자체 제작 웹앱
├── data/                      # 피험자별 원시 IMU CSV (P01~P06, 60Hz, foot/shank/hip) — 폴더만 유지, 내용은 git에서 제외
├── analysis/
│   ├── pipeline.py            # 지표 계산 (피크 검출, 충격량, 케이던스, 관절/골반 kinematics, 통계)
│   ├── run_analysis.py        # 전체 파이프라인 실행 진입점
│   ├── visualize.py           # results/figures/ 생성
│   └── add_table.py, plot_change_rates.py
├── literature_pack/            # 결과 해석에 사용한 참고문헌 자료
├── results/                    # metrics_by_condition.csv 등 + figures/ — 폴더만 유지, 내용은 git에서 제외 (run_analysis.py로 재생성)
├── 보고용 figure/               # 실험설계, 부착, 테이핑 사진 및 최종 보고서 PDF/DOCX
└── Research_object.md         # 가설 정의
```

## 7. 참고문헌

1. Heiderscheit, B. C., Chumanov, E. S., Michalski, M. P., Wille, C. M., & Ryan, M. B. (2011). Effects of step rate manipulation on joint mechanics during running. *Medicine & Science in Sports & Exercise*, 43(2), 296–302. https://doi.org/10.1249/MSS.0b013e3181ebedf4
2. Bartík, P., & Šagát, P. (2022). Positive effect of kinesiotape on 1 km run performance in university-level males: A cross-sectional study. *Journal of Functional Morphology and Kinesiology*, 7(2), 32. https://doi.org/10.3390/jfmk7020032
3. Eom, S. Y., Lee, W. J., Lee, J. I., Lee, E. H., Lee, H. Y., & Chung, E. J. (2014). The effect of ankle Kinesio taping on range of motion and agility during exercise in university students. *Physical Therapy Rehabilitation Science*, 3(1), 63–68. https://doi.org/10.14474/ptrs.2014.3.1.63
4. Rong, R., & Kuo, C. (2024). Dynamic soft tissue artifacts during impulsive loads: Measurement errors vary with wearable inertial measurement unit sensor design. *IEEE Transactions on Biomedical Engineering*, 71(11), 3073–3082. https://doi.org/10.1109/TBME.2024.3416378
5. Chumanov, E. S., Wille, C. M., Michalski, M. P., & Heiderscheit, B. C. (2012). Changes in muscle activation patterns when running step rate is increased. *Gait & Posture*, 36(2), 231–235. https://doi.org/10.1016/j.gaitpost.2012.02.023
6. Lescure, Y., Nicolas, M. A., Perrin, E., Sanchis-Sales, E., Lopezosa-Reca, E., Travouillon, C., & Gijon-Nogueron, G. (2025). Biomechanical strategies to improve running: Cadence, footwear, and orthoses — A quasi-experimental study. *Sensors*, 25(8), 2414. https://doi.org/10.3390/s25082414
7. Schubert, A. G., Kempf, J., & Heiderscheit, B. C. (2014). Influence of stride frequency and length on running mechanics: A systematic review. *Sports Health*, 6(3), 210–217. https://doi.org/10.1177/1941738113508544
8. Ludwig, C., Lipfert, S., & Seyfarth, A. (2011). Variability in human running is not reduced by metronome signals. *Proceedings of the International Society of Biomechanics Congress*.
9. Cronström, A., Cole, M. H., Chalkley, D., & Ekvall Hansson, E. (2022). Acute effect of traditional and adaptive metronomes on gait variability in older individuals with a history of falls. *Aging Clinical and Experimental Research*, 34, 1397–1404. https://doi.org/10.1007/s40520-021-02066-9
10. Nijs, A., Roerdink, M., & Beek, P. J. (2020). Cadence modulation in walking and running: Pacing steps or strides? *Brain Sciences*, 10(5), 273. https://doi.org/10.3390/brainsci10050273
11. Terrier, P., & Dériaz, O. (2012). Persistent and anti-persistent pattern in stride-to-stride variability of treadmill walking: Influence of rhythmic auditory cueing. *Human Movement Science*, 31(6), 1585–1597. https://doi.org/10.1016/j.humov.2012.05.004
12. Li, Y., Xia, Y., Zhang, D., Fu, S., Liu, M., Pan, X., & Liu, H. (2024). Immediate effect of kinesiology taping on muscle strength, static balance and proprioception after eccentric muscle fatigue on ankle: A randomized cross-over trial. *BMC Musculoskeletal Disorders*, 25, 244. https://doi.org/10.1186/s12891-024-07365-6
13. Ghai, S., Ghai, I., & Narciss, S. (2024). Influence of taping on joint proprioception: A systematic review with between and within group meta-analysis. *BMC Musculoskeletal Disorders*, 25, 488. https://doi.org/10.1186/s12891-024-07571-2
14. Justa, J., Šmídl, V., & Hamáček, A. (2020). Fast AHRS filter for accelerometer, magnetometer, and gyroscope combination with separated sensor corrections. *Sensors*, 20(14), 3824. https://doi.org/10.3390/s20143824
15. Yoo, T. S., Hong, S. K., Yoon, H. M., & Park, S. (2011). Gain-scheduled complementary filter design for a MEMS based attitude and heading reference system. *Sensors*, 11(4), 3816–3830. https://doi.org/10.3390/s110403816
16. Fan, B., Li, Q., & Liu, T. (2017). How magnetic disturbance influences the attitude and heading in magnetic and inertial sensor-based orientation estimation. *Sensors*, 18(1), 76. https://doi.org/10.3390/s18010076


