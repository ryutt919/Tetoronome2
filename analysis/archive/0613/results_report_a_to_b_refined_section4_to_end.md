# Extracted Markdown: results_report_a_to_b_refined.html section 4 to end

- Source: `analysis/0613/results_report_a_to_b_refined.html`
- Range: from `4. Clinical Significance` to document end

## 4. 연구 목표별 종합 결론 (Clinical Significance)

### [목표 1] 메트로놈으로 인한 케이던스 증가 효과 분석

메트로놈 자극(Control → Metro)이 주어졌을 때 보행의 역학적 요인들이 어떻게 반응하는지 검토했습니다.

| 평가 항목 (목표) | 관련 지표 (Metric) | 통계적 변화 (C → M) | 임상적 해석 (논문 근거) |
| --- | --- | --- | --- |
| 충격량 근사 (acc 기반) | Peak g / Resultant RMS | Peak g 7.5% 증가, RMS 3.4% 증가 | 케이던스 상승 시 본 데이터에서는 shank IMU 기반 **shock proxy**가 함께 증가하는 경향이 관찰되었습니다. 이는 지면반력 충격량이 직접 증가했다는 의미가 아니라,<br>더 높은 step frequency에 맞추는 과정에서 **leg/vertical stiffness**와 shank acceleration response가 커졌을 가능성으로 해석할 수 있습니다.<br>이러한 해석은 직접적인 지면반력 검증이 아니라 **간접 기전 근거/가능성** 수준입니다. Farley & González는 초록 근거로<br>stride frequency 변화와 leg spring stiffness 조절을 보고했고, Kulmala et al.은 신발 쿠셔닝 연구에서 leg stiffness 증가가<br>impact loading amplification과 연결될 수 있음을 보였습니다. 따라서 두 문헌은 본 데이터의 GRF 충격 증가를 직접 입증하는 근거가 아니라,<br>shank acceleration response 증가를 설명할 수 있는 배경 기전으로만 해석합니다.<br><br>*→ Farley & González (1996): stride frequency 변화는 leg spring stiffness 조절과 관련됩니다(초록 근거).[9]<br>Kulmala et al. (2018): leg stiffness 증가는 impact loading amplification과 연결될 수 있으나, 신발 쿠셔닝 연구입니다.[10]* |
| 족저굴곡 peak / ankle strategy | Ankle Plantarflexion Peak | 34.7% 증가 | 메트로놈 조건에서 관찰된 **족저굴곡 각도 증가(5명 중 4명)**는 propulsive force 또는 ankle power를 직접 측정한 결과가 아니라, 더 plantarflexed ankle strategy 또는<br>forefoot-like strategy로의 전환 가능성을 보여주는 운동학적 결과로 해석하는 것이 타당합니다. 선행 running 문헌은 stride rate 변화가 발목 자세를 포함한 running mechanics를<br>바꾸고, forefoot-like running이 더 큰 foot/ankle demand 및 gastrocnemius 활성 차이와 관련될 수 있음을 보여주는 배경 근거입니다.<br><br>*→ Schubert et al. (2014): stride rate 변화는 running mechanics 전반과 발목 자세에 영향을 줍니다.[11]<br>Yong et al. (2014): forefoot runners는 더 plantarflexed ankle posture(ankle p<0.001)와 knee flexion 차이(p=0.023), gastrocnemius activity 차이를 보였습니다.[12]* |
| 골반 자세 안정성 | Pelvis Pitch / Roll SD | Roll SD 4.2% 증가 | 메트로놈은 본 데이터에서 골반 안정성 지표를 명확히 개선하지 않았습니다. RAS/RAC 문헌의 주된 효과는 cadence, stride length, gait velocity,<br>cue frequency accuracy 같은 시공간 보행 변수에 집중되어 있으며, 건강 러닝의 pelvis pitch/roll SD가 즉시 개선되어야 한다는 직접 근거는 아닙니다.<br><br>*→ Thaut et al. (2007)은 post-stroke gait training에서 RAS가 velocity, stride length, cadence, symmetry를 개선했다고 보고했습니다.[3]<br>Yu et al. (2015)은 healthy young female walking에서 rhythmic auditory cueing frequency가 stride length, cadence, gait speed에 영향을 준다고 보고했습니다.[4]* |
| 보폭의 일관성 | Step Interval CV% | 5.09% 증가 | 외부 박자에 발을 맞추는 과정에서 본 데이터는 **변동성 증가(일관성 감소)** 경향을 보였습니다. 이는 메트로놈 cue가 자연스러운 self-selected timing을<br>단순히 안정화한 것이 아니라, 박자에 맞추는 추가 task demand를 만들어 step timing variability를 증가시켰을 가능성을 시사합니다.<br><br>*→ Cronström et al. (2022): 낙상 이력 고령자에서 특정 metronome cueing 조건의 stride time variability 증가가 보고되었습니다(limited transfer).[14]<br>Terrier & Deriaz (2012): treadmill walking/RAC 조건에서 stride-to-stride variability dynamics 재조직이 보고되었습니다(limited transfer).[15]* |

### [목표 2] 테이핑 효과 분석

발목 테이핑(Control → Tape) 적용이 발목 관절 운동학과 IMU 기반 shock proxy에 미치는 영향을 검토했습니다.

| 평가 항목 (목표) | 관련 지표 (Metric) | 통계적 변화 (C → T) | 임상적 해석 (논문 근거) |
| --- | --- | --- | --- |
| 충격량 근사 (acc 기반) | Peak g / Resultant RMS | Peak g 1.7% 감소, RMS 0.8% 감소 | 본 데이터에서는 테이핑 조건에서 Peak g와 RMS가 소폭 감소했습니다. 다만 선행문헌은 테이핑의 직접적인 shock absorption 효과보다 발목 ROM 제한과 kinematic constraint를 더 직접적으로<br>뒷받침합니다. 또한 Raymond et al.의 PubMed 초록/결론 수준 근거는 테이핑/보조기가 proprioceptive acuity를 일관되게 개선한다는 해석을 지지하지 않습니다. 따라서 shock proxy 감소는 본 데이터의 탐색적 방향성으로 보고하되, 메커니즘은<br>탐색적으로 해석합니다.<br><br>*→ Cordova et al. (2000)은 ankle support가 ROM을 제한한다고 보고했습니다.[6] Raymond et al. (2012)은 tape/brace의<br>proprioceptive acuity 개선 효과가 확인되지 않았다고 결론냈습니다(초록/결론 근거).[8]* |
| 배측굴곡 억제 (Dorsiflexion) | Ankle Dorsiflexion Peak | 4.07% 감소 | 테이핑이 발목 전면부를 구속함으로써 발목이 위로 올라오는 배측굴곡 동작이 소폭 제한된 것으로 해석됩니다. 이는 Cordova et al.의 원문 문구처럼 taping이 dorsiflexion ROM 제한에 가장 큰 지지를 보였다는<br>메타분석과, chronic ankle instability 대상자의 taping 후 gait kinematics가 더 중립적인 발목 위치로 이동했다는 연구와 부합합니다.<br><br>*→ Cordova et al. (2000)은 "taping offered the most support for limiting dorsiflexion ROM"이라고 보고했습니다.[6] Chinn et al. (2014)은<br>taping 후 jogging에서 더 적은 dorsiflexion을 보고했습니다.[7]* |
| 족저굴곡 peak / ankle strategy | Ankle Plantarflexion Peak | 5.78% 증가 — 메트로(34.7%)보다 훨씬 작음 | C→T에서 Plantarflexion은 5.78% 증가했지만 C→M의 34.7% 증가보다 훨씬 작았습니다. 따라서 이 결과는 테이핑이 propulsive force 또는 ankle power를<br>강화했다는 근거가 아니라, 테이핑 단독 조건에서는 메트로놈 조건처럼 큰 ankle strategy 변화가 나타나지 않았다는 관찰로 해석하는 것이 타당합니다. 선행 taping gait 연구 역시 발목을<br>더 중립적인 위치로 이동시키는 방향을 보고했습니다.<br><br>*→ Chinn et al. (2014)은 walking에서 taping 후 더 적은 plantarflexion, jogging에서 더 적은 dorsiflexion을 보고했습니다.[7]* |
| 보폭의 일관성 | Step Interval CV% | 10.24% 감소 | 본 데이터에서는 테이핑 조건에서 Step Interval CV%가 감소하여 **step timing variability가 낮아지는 방향**이 관찰되었습니다. 그러나 현재 인용 가능한 문헌만으로<br>“테이핑이 신경근 피드백을 향상시켜 보행 리듬 안정성을 증가시켰다”고 단정하기는 어렵습니다. 해당 결과는 N=6 탐색 결과로 보고하고, 기계적 지지, 피험자 신뢰감, 개인차를 포함한<br>후속 검증이 필요합니다.<br><br>*→ Raymond et al. (2012)은 ankle tape/brace가 proprioceptive acuity에 일관된 전체 효과를 보이지 않았다고 보고했습니다(초록/결론 근거).[8]* |

### [목표 3] Tape + Metro 복합 효과 분석

발목 테이핑을 적용한 상태에서 메트로놈 자극이 추가되었을 때(Control → Tape+Metro, Tape → Tape+Metro)의 복합 조건 변화와 동시 적용 패턴을 검토했습니다.

| 평가 항목 (목표) | 관련 지표 (Metric) | 복합 조건 결과 (C → T+M) | 메트로놈 추가 효과 (T → T+M) | 종합 분석 |
| --- | --- | --- | --- | --- |
| 충격량 근사 (acc 기반) | Peak g / Resultant RMS | Peak g +3.57%, RMS +2.09% | Peak g +5.44%, RMS +2.97% | Tape 단독 조건에서는 Peak g가 1.77% 감소했지만, Tape+Metro에서는 오히려 Control보다 증가했습니다. 복합 조건은 mechanical ankle constraint와<br>external temporal cue가 동시에 주어진 **dual constraint** 조건으로 볼 수 있습니다. 이는 formal interaction model을 검정한 결론이 아니라 관찰 패턴 기반 해석이며,<br>더 높은 cadence에 맞추는 과정에서 leg stiffness와 shank IMU acceleration response가<br>커졌을 가능성이 있습니다. 즉, 복합 조건은 **shock proxy 감소 목적에는 일관된 이득을 보이지 않았습니다.** |
| 보폭의 일관성 | Step Interval CV% | +4.50% | +16.41% | Tape 단독 조건에서는 CV%가 10.24% 감소해 step timing variability가 낮아지는 방향이었지만, 메트로놈을 추가하면 CV%가 크게 증가했습니다. 이는 ankle constraint 위에<br>external temporal cue가 추가되면서 timing 조절 task demand가 커진 결과로 해석할 수 있으며, **Tape+Metro의 핵심 결과는 step timing variability 증가**입니다. |
| 골반 자세 안정성 | Pelvis Pitch / Roll SD | Pitch SD +2.69%, Roll SD +16.34% | Pitch SD -3.73%, Roll SD -22.97% | Control 대비 Tape+Metro는 골반 안정성을 명확히 개선하지 못했습니다. 다만 Tape 단독에서 크게 증가했던 Roll SD가 Tape+Metro에서 낮아지는 방향을 보였으므로, 메트로놈이 테이핑으로<br>생긴 측면 흔들림을 일부 완화했을 가능성은 있습니다. 그러나 표본이 작고 방향성 관찰에 그치므로 **골반 안정화 효과로 단정하기는 어렵습니다.** |
| 발목 운동학 변화 | Ankle PF / DF / ROM | PF +36.09%, DF -8.31%, DP/PF ROM +3.87% (n=5) | PF +18.96%, DF -2.53%, DP/PF ROM +10.31% (n=5) | Tape+Metro에서는 Plantarflexion이 크게 증가하고 Dorsiflexion은 감소하는 방향이 관찰되었습니다. 이는 propulsive force 또는 ankle power 증가라기보다, external temporal cue에 따른<br>more plantarflexed ankle strategy와 테이핑의 전방 구속에 따른 dorsiflexion constraint가 함께 나타난 패턴으로 해석됩니다. 단, 진현준 Tape+Metro 발목 지표는<br>이상치로 제외되어 발목 관련 통계는 **n=5 기준**입니다. |

## 5. 가설과 실제 결과의 차이 — IMU 기반 측정의 한계와 수행 요인

### 가설 vs 실제 결과 비교

| 개입 | 가설 | 실제 결과 | 불일치 여부 |
| --- | --- | --- | --- |
| 메트로놈 | 충격량 감소 (acc 기반) | Peak g **7.5% 증가** | ⚠️ 반대 방향 (가설 불지지) |
| 메트로놈 | 골반 안정성 증가 (Pitch/Roll SD 감소) | Roll SD 4.2% 증가, Pitch SD ≈ 불변 | ⚠️ 반대 방향 (가설 불지지) |
| 메트로놈 | 보폭 일관성 증가 (CV% 감소) | CV% **5.1% 증가** | ⚠️ 반대 방향 (가설 불지지) |
| 테이핑 | 충격량 감소 (acc 기반) | Peak g 1.7% 감소 | ✅ 동일 방향 (가설 지지) |
| 테이핑 | 족저굴곡(PF) 증가 | Plantarflexion 5.8% 증가 | ✅ 동일 방향 (가설 지지) |
| 테이핑 | 보폭 일관성 증가 (CV% 감소) | CV% 10.2% **감소** | ✅ 동일 방향 (가설 지지) |

### IMU 측정 및 실험 수행의 한계 — 오차/해석 원인 분류

| 오차/해석 요인 | 영향 받는 지표 | 메커니즘 설명 | 가설-결과 불일치와의 연관 |
| --- | --- | --- | --- |
| **1. 소프트 티슈 아티팩트 (Soft Tissue Artifact, STA)** | Peak g, Ankle Kinematics | IMU는 피부와 근막 위에 부착되므로, 달리기/걷기의 충격 시 센서가 뼈와 함께 움직이지 않고 근육 진동과 함께 흔들림. 이로 인해 실제 골격 운동보다 **가속도 피크가 과대<br>계측**될 수 있음. 특히 Shank(하퇴)는 착지 충격이 크기 때문에 STA 영향이 최대 15-20% 오차를 유발할 수 있음. | 메트로놈 조건에서 케이던스가 증가하면 더 높은 step frequency에 맞추기 위한 leg/vertical stiffness 조절과 shank acceleration response 변화가 함께 나타날 수 있습니다.<br>따라서 Peak g 증가는 실제 지면반력 충격 증가와 동일한 의미가 아니라, IMU 부착 조건과 soft tissue artifact, 그리고 stiffness-related acceleration response가 함께 반영된<br>**shock proxy 증가**로 해석해야 합니다. |
| **2. 센서 고정 불량 및 위치 이탈 (Sensor Drift & Displacement)** | Ankle Kinematics, Pelvis | Foot, shank, pelvis에 부착된 IMU는 운동 중 점진적으로 위치가 이탈하거나 회전(Misalignment)할 수 있습니다. 특히 foot/shank 센서는 착지 충격과 테이핑 상태의 영향을<br>직접 받으므로, 센서와 피부 또는 테이프 사이의 상대 운동이 발생할 수 있습니다. 이로 인해 **실제 분절 상대각과 측정된 상대각 사이에 체계적 오프셋**이 생길 수 있습니다. | 테이핑 조건에서 Dorsiflexion 값이 예상보다 크거나 작게 측정될 경우, 이는 테이핑의 생물역학적 효과가 아닌 센서 위치 변화에 의한 허상(artifact)일 가능성이 있음. 진현준<br>피험자의 Tape+Metro 조건에서 이상치가 관찰된 것도 이와 관련 가능. |
| **3. 자기장 간섭 (Magnetic Interference)** | Pelvis Kinematics (Roll/Yaw) | IMU의 방향 추정은 내부 AHRS(Attitude & Heading Reference System) 알고리즘에 의존하며, 이는 지구 자기장을 참조함. 실험실 환경(트레드밀, 금속<br>프레임 등)에서는 자기장이 왜곡되어 Yaw/Roll 방향의 방위각 추정에 오차 발생 가능. | 골반 Roll SD 결과(메트로놈 조건에서 4.2% 증가)가 실제 몸통 움직임의 변화인지, 아니면 자기장 간섭으로 인한 추정 오류인지를 IMU만으로는 구분하기 어려움. 가설(안정성 증가)과의<br>불일치는 이 오차도 원인일 수 있음. |
| **4. 통합(Integration) 드리프트 오차** | Pelvis/Ankle 각도 추정 | IMU에서 각도를 추정하는 방법은 자이로스코프(Gyroscope) 적분값과 가속도계(Accelerometer) 중력 벡터를 상보 필터 등으로 융합함. 발목 각도는 shank-foot 상대각으로<br>계산되므로 두 센서에 공통으로 발생한 일부 드리프트는 상쇄될 수 있지만, 각 센서의 독립적인 축 정렬 오차와 적분 드리프트는 남을 수 있습니다. 20초 측정에서도 착지 충격이 반복될 때마다 추정 오류가<br>누적 가능. | 골반 Pitch SD와 발목 DF/PF 값이 조건 간에 생각보다 작은 차이를 보이는 이유 중 하나로, 잔여 드리프트와 센서별 방향 추정 오차가 실제 개입 효과보다 큰 노이즈를 만들어 효과를<br>희석(attenuate)시켰을 가능성이 있음. |
| **5. 분절 간 상대각 계산의 좌표계/캘리브레이션 오차** | Ankle Dorsiflexion/Plantarflexion, DP/PF ROM | 본 연구는 pelvis, shank, foot 3개 IMU를 부착하여 **shank-foot 분절 간 상대 방향**을 사용했습니다. 따라서 상대각 계산도 센서 좌표계와 해부학적 축을 맞추는 초기 캘리브레이션, 부착 각도, 센서-피부 간<br>미세 이동, 테이핑으로 인한 foot 센서 장착 상태 변화에 민감합니다. | 센서 축 정렬 오차가 있으면 PF/DF의 **방향성은<br>유지되더라도 변화량의 크기**가 과소 또는 과대 평가될 수 있습니다. 특히 Tape+Metro처럼 plantarflexed ankle strategy가 커지는 조건에서는 foot/shank 센서의 미세한 회전 오차가 발목<br>피크 각도에 더 크게 반영될 수 있습니다. |
| **6. 메트로놈 미훈련 피험자의 동기화 부담** | Cadence, Step Interval CV%, Peak g, Ankle PF | 메트로놈 보행에 충분히 익숙하지 않은 피험자는 외부 박자에 즉시 동기화하는 과정에서 보폭과 접지 타이밍을 반복적으로 수정할 수 있습니다. 이때 케이던스는 목표 방향으로 증가하더라도,<br>external temporal cue가 self-selected internal timing regulation을 방해하거나 task demand를 높여 스텝 간격 변동성(CV%)을 키울 수 있습니다.<br>rhythmic auditory cueing이 stride-to-stride variability dynamics를 바꿀 수 있다는 점을 고려하면 본 결과는 cue 적응 부담의 가능성을 시사합니다.[14][15] | 메트로놈 조건에서 CV%가 5.1% 증가하고, Tape → Tape+Metro에서 CV%가 16.41% 증가한 결과는 IMU 측정 오차만으로 설명하기보다 **미훈련 피험자의<br>동기화 부담**을 함께 고려해야 합니다. 또한 plantarflexion 증가는 propulsive force 또는 ankle power 증가로 단정하기보다 more plantarflexed ankle strategy 또는 forefoot-like strategy로 해석하는 것이<br>더 정합적이며, 이 전략 변화와 stiffness-related shank acceleration response가 shock proxy 증가와 함께 나타났을 가능성이 있습니다. |
| **7. 소표본(N=6) 환경에서의 해석 제한** | 모든 지표 | N=6의 극소표본에서는 t-test, Wilcoxon, p-value 기반 유의성 판단을 제외하고 변화율과 피험자별 방향성을 중심으로 해석해야 함. 개인차(individual<br>variability)가 크거나 1-2명의 역방향 반응만 있어도 그룹 평균 방향이 크게 바뀔 수 있음. | 메트로놈의 충격 감소 효과나 골반 안정화 효과가 실제로 일부 피험자에서 발생했더라도, 다른 피험자의 반대 반응으로 인해 그룹 수준에서는 가설과 반대 방향의 평균값이 산출될 수 있음. 이는<br>IMU 오차가 아닌 **실제 개인차의 반영**일 수 있으며, 표본을 늘렸을 때 다시 검증이 필요함. |

## 6. 참고문헌 (수정본)

1. Heiderscheit, B. C., Chumanov, E. S., Michalski, M. P., Wille, C. M., & Ryan, M. B. (2011). Effects of step rate manipulation on joint mechanics during running. *Medicine & Science in Sports & Exercise, 43*(2), 296-302. doi:10.1249/MSS.0b013e3181ebedf4. *요지: step rate 증가 시 step length, braking impulse, impact transient occurrence, hip/knee loading이 감소했다.*
2. Thaut, M. H., McIntosh, G. C., Prassas, S. G., & Rice, R. R. (1993). Effect of rhythmic auditory cuing on temporal stride parameters and EMG patterns in hemiparetic gait of stroke patients. *Journal of Neurologic Rehabilitation, 7*(1), 9-16. doi:10.1177/136140969300700103. *요지: rhythmic auditory cueing은 temporal stride parameters와 EMG pattern을 변화시켰다. 단, stroke walking 배경 근거이며 건강 러닝 plantarflexion의 직접 근거는 아니다.*
3. Thaut, M. H., Leins, A. K., Rice, R. R., Argstatter, H., Kenyon, G. P., McIntosh, G. C., Bolay, H. V., & Fetter, M. (2007). Rhythmic auditory stimulation improves gait more than NDT/Bobath training in near-ambulatory patients early poststroke. *Neurorehabilitation and Neural Repair, 21*(5), 455-459. doi:10.1177/1545968307300523. *요지: RAS는 post-stroke gait training에서 velocity, stride length, cadence, symmetry를 개선했다. 본 보고서에서는 보행 변수 배경 근거로만 사용한다.*
4. Yu, L., Zhang, Q., Hu, C., Huang, Q., Ye, M., & Li, D. (2015). Effects of different frequencies of rhythmic auditory cueing on the stride length, cadence, and gait speed in healthy young females. *Journal of Physical Therapy Science, 27*(2), 485-487. doi:10.1589/jpts.27.485. *요지: 110% RAC 조건에서 stride length, cadence, gait speed가 증가했다. 단, healthy young female walking 연구이며 러닝 또는 pelvis pitch/roll SD의 직접 근거는 아니다.*
5. Repp, B. H., & Su, Y.-H. (2013). Sensorimotor synchronization: A review of recent research (2006-2012). *Psychonomic Bulletin & Review, 20*(3), 403-452. doi:10.3758/s13423-012-0371-2. *요지: SMS는 외부 리듬과 움직임의 시간적 협응이다. 본 보고서에서는 외부 박자 동기화의 배경 이론으로만 사용한다.*
6. Cordova, M. L., Ingersoll, C. D., & LeBlanc, M. J. (2000). Influence of ankle support on joint range of motion before and after exercise: a meta-analysis. *Journal of Orthopaedic & Sports Physical Therapy, 30*(4), 170-177. doi:10.2519/jospt.2000.30.4.170. *요지: taping은 dorsiflexion ROM 제한에 가장 큰 지지를 보였다.*
7. Chinn, L., Dicharry, J., Hart, J. M., Saliba, S., Wilder, R., & Hertel, J. (2014). Gait kinematics after taping in participants with chronic ankle instability. *Journal of Athletic Training, 49*(3), 322-330. doi:10.4085/1062-6050-49.3.08. *요지: taping 후 walking/jogging에서 발목 위치가 더 neutral한 방향으로 이동했다.*
8. Raymond, J., Nicholson, M., Hiller, C. E., & Refshauge, K. M. (2012). The effect of ankle taping or bracing on proprioception in functional ankle instability: a systematic review and meta-analysis. *Journal of Science and Medicine in Sport, 15*(5), 386-392. doi:10.1016/j.jsams.2012.03.008. *요지: PubMed 초록/결론 기준으로 pooled evidence는 tape/brace가 proprioceptive acuity에 일관된 효과를 보이지 않았음을 제시했다.*
9. Farley, C. T., & González, O. (1996). Leg stiffness and stride frequency in human running. *Journal of Biomechanics, 29*(2), 181-186. doi:10.1016/0021-9290(95)00029-1. *요지: stride frequency 변화는 spring-like running에서 leg stiffness 조절과 관련된다.*
10. Kulmala, J.-P., Kosonen, J., Nurminen, J., & Avela, J. (2018). Running in highly cushioned shoes increases leg stiffness and amplifies impact loading. *Scientific Reports, 8*, 17496. doi:10.1038/s41598-018-35980-6. *요지: leg stiffness 증가는 impact loading amplification과 연결될 수 있다.*
11. Schubert, A. G., Kempf, J., & Heiderscheit, B. C. (2014). Influence of stride frequency and length on running mechanics: a systematic review. *Sports Health, 6*(3), 210-217. doi:10.1177/1941738113508544. *요지: stride rate 변화는 running mechanics와 발목 자세를 포함한 하지 운동학에 영향을 준다.*
12. Yong, J. R., Silder, A., Montgomery, K. L., Fredericson, M., & Delp, S. L. (2014). Differences in muscle activity between natural forefoot and rearfoot strikers during running. *Journal of Biomechanics, 47*(15), 3593-3597. doi:10.1016/j.jbiomech.2014.10.015. *요지: forefoot strike는 더 plantarflexed ankle posture(ankle p<0.001) 및 gastrocnemius activity 차이와 관련된다. knee flexion 차이의 p-value는 p=0.023이다.*
13. Williams, D. S. B., Green, D. H., & Wurzinger, B. (2012). Changes in lower extremity movement and power absorption during forefoot striking and barefoot running. *International Journal of Sports Physical Therapy, 7*(5), 525-532. *요지: forefoot/barefoot running은 foot/ankle demand 및 ankle power absorption 증가와 관련된다. 본 데이터의 PF angle이 propulsive force를 증명한다는 뜻은 아니다.*
14. Cronström, A., et al. (2022). Acute effect of traditional and adaptive metronomes on gait variability in older adults with a history of falls. *Ageing Clinical and Experimental Research*. *요지: 낙상 이력 고령자에서 특정 metronome cueing 조건의 stride time variability 증가가 보고되었으며, 본 연구에는 limited transfer 근거로만 사용한다.*
15. Terrier, P., & Deriaz, O. (2012). Persistent and anti-persistent pattern in stride-to-stride variability of treadmill walking: influence of rhythmic auditory cueing. *PLoS ONE, 7*(11), e47171. doi:10.1371/journal.pone.0047171. *요지: treadmill walking/RAC 조건에서 rhythmic auditory cueing은 stride-to-stride variability dynamics를 재조직할 수 있다. 본 러닝 결과에는 limited transfer 근거로만 사용한다.*
