# Section 4: 연구 목표별 종합 결론 — 수정본

> 작성 기준: 2026-06-13 | N=6 IMU 러닝 실험 (Control / Metro / Tape / TapeMetro)
> 실험 강도: RPE 17 (~4.17 m/s, 15 km/h)
> p-value·Wilcoxon 삭제, 평균·변화율 기반 해석으로 전면 재작성

---

## [목표 1] 메트로놈으로 인한 케이던스 증가 효과 분석

메트로놈 자극(Control → Metro)이 주어졌을 때 보행의 역학적 요인들이 어떻게 반응하는지 검토했습니다.

| 평가 항목 | 관련 지표 | 변화 (C → M) | 임상적 해석 (근거 기반) |
| --- | --- | --- | --- |
| 충격량 근사 (acc 기반) | Peak g / Resultant RMS | Peak g **+7.5%** 증가, RMS +3.4% 증가 | 선행연구(Heiderscheit 2011)는 self-selected 기준 cadence를 5–10% 증가시켰을 때 step length, braking impulse, impact transient occurrence가 감소함을 force plate로 보고하였다.[1] 그러나 본 실험은 RPE 17(Borg 17/20, ~4.17 m/s)의 고강도 조건이었으며, Heiderscheit의 2.9 m/s 중강도 대비 신경근 및 대사 자원이 이미 최대치 근방에 있는 상태였다. 이 고강도 조건에서 비훈련된 외부 박자 cadence 조절이 추가로 부과되어 역학적 붕괴가 발생했을 가능성이 있다.<br><br>또한 Heiderscheit가 측정한 braking impulse(force × time 적분값)와 본 실험의 shank IMU peak g(순간 최대 가속도)는 서로 다른 충격 측면을 반영한다. Cadence 증가로 step 주기가 빨라지면 shank의 충격 사이클 빈도 자체가 증가하여 IMU peak g proxy가 상승할 수 있다. Farley & González(1996)는 stride frequency 증가 시 leg spring stiffness 조절이 필요함을 보고하였으며[9], cadence 급성 증가 시 이 stiffness 조절이 충분히 이루어지지 않으면 shank에 전달되는 가속도가 증가할 수 있다.<br><br>따라서 본 결과는 선행연구와 단순히 모순되는 것이 아니라, 고강도 조건 + IMU proxy 특성 + 비훈련된 cadence 조절의 복합적 결과로 해석하는 것이 타당하다. |
| 족저굴곡 peak | Ankle Plantarflexion Peak | **+34.7%** 증가 (5명 중 4명) | 본 분석에서 Plantarflexion Peak는 stride 전체 구간의 최소 DF 각도(np.min)로 계산된다. 시각화 분석(fig06, fig07) 결과, stride는 foot strike → next foot strike로 정의되며, ankle angle 패턴은 다음과 같다: foot strike(~0°) → PF peak(~20-30% of stride) → DF peak(mid-swing, ~50%) → 중립 복귀(100%). 본 실험 운동 강도(RPE 17, ~4.17 m/s)에서 stance duration은 약 180-220ms로 추정되며, 이는 전체 stride(~650ms)의 약 28-34%에 해당한다. 따라서 **PF peak가 stride의 ~20-30%에 발생한다는 것은 terminal stance(push-off)/toe-off 구간과 일치**한다.<br><br>+34.7%는 push-off 시 발목의 kinematic PF 범위가 증가했음을 의미한다. 빠른 cadence cue에 맞추기 위해 push-off 단계에서 더 강한 ankle PF 전략이 나타났을 가능성이 있다. Chumanov et al.(2012)은 step rate +10% 조건에서 medial gastrocnemius activity가 증가했음을 보고하였으며(late swing pre-activation)[19], 이는 cadence 증가 시 더 강한 ankle 근육 동원을 시사한다. PMC12031012(2025)는 10% cadence 증가 시 peak ankle dorsiflexion이 25.80°에서 23.59°로 감소함을 보고하였다.[17]<br><br>Schubert et al.(2014)는 systematic review에서 stride rate 증가 시 "the ankle demonstrating a more plantar flexed position at initial contact with increased stride rate"를 보고하였다.[11] 즉 cadence 증가 시 foot strike 순간부터 발목이 더 plantarflexed 위치에 놓이며, 이는 stance 전반의 ankle kinematic pattern이 PF 방향으로 이동함을 시사한다. 본 실험의 PF peak 증가(+34.7%)는 이 방향과 일치한다.<br><br>단, +34.7%는 운동학적 각도 변화(push-off PF peak)로, 추진력(GRF) 또는 ankle power 증가를 직접 측정한 결과가 아니다. 실제 추진력 변화 여부는 force plate 측정이 필요하며, 본 결과는 IMU 기반 kinematic proxy로 해석한다. |
| 골반 자세 안정성 | Pelvis Pitch SD / Roll SD | Pitch SD **−0.46%** (n=5, 2.2455→2.2351)<br>Roll SD **+4.26%** (n=5, 8.844→9.2208) | Pitch SD(시상면 안정성)는 거의 불변이었으며, Roll SD(측면 안정성)만 +4.26% 증가하였다. 이는 메트로놈이 골반 안정성을 개선한 것이 아니라, 메트로놈으로 인한 **갑작스러운 cadence 증가**가 lateral/frontal plane 제어 부담을 증가시킨 결과로 해석된다.<br><br>본 실험과 동일하게 러닝에서 메트로놈을 적용한 Ludwig et al.(2011)은 "Variability in human running is not reduced by metronome signals. The coefficient of variation in step frequency was not reduced with the metronome, and variability in gait pattern appears to be a fundamental property in human running"을 보고하였다.[27] PMC7288070(running 연구)은 "Synchronization was achieved less often in running, especially at slow pacing frequencies"를 보고하였다.[28]<br><br>보행 배경 근거(limited transfer): Cronström et al.(2022)은 낙상 이력 노인의 보행에서 "Participants had significantly increased stride time variability during feedback(F(2)=9.83)"을 보고하였다.[14] Terrier & Dériaz(2012)는 treadmill 보행에서 메트로놈이 "anti-persistent dynamics: deviations followed by rapid over-correction, producing oscillations around target values"를 유발함을 보고하였다.[15] 두 문헌은 보행 연구로 러닝에 직접 적용할 수 없으나, 외부 박자 동기화가 variability를 증가시키는 방향성을 보여준다. |
| 보폭의 일관성 | Step Interval CV% | **+5.09%** 증가 | 메트로놈 조건에서 step timing variability가 오히려 증가하였다. 러닝 직접 근거로, Ludwig et al.(2011)은 "Variability in human running is not reduced by metronome signals. The coefficient of variation in step frequency was not reduced with the metronome"을 보고하였다.[27] PMC7288070(running 연구)은 "Synchronization was achieved less often in running, especially at slow pacing frequencies"를 보고하였다.[28]<br><br>보행 배경 근거(limited transfer): Cronström et al.(2022)은 보행에서 메트로놈 cueing이 stride time variability를 증가시켰음을 보고하였으며(F(2)=9.83)[14], Terrier & Dériaz(2012)는 treadmill 보행에서 isochronous metronome 적용 시 anti-persistent dynamics(박자 맞추기 과교정 반복 패턴)가 나타남을 보고하였다.[15] 두 문헌은 보행 연구로 러닝 결과에 직접 적용할 수 없으나 방향성을 보강한다.<br><br>본 결과는 외부 박자 cue가 self-selected timing을 안정화하지 못하고, RPE 17 고강도 조건에서 이미 높은 신경근 부하 위에 추가 동기화 task demand를 만들어 step timing variability를 증가시킨 것으로 해석된다. |

---

## [목표 2] 테이핑 효과 분석

발목 테이핑(Control → Tape) 적용이 발목 관절 운동학과 IMU 기반 shock proxy에 미치는 영향을 검토했습니다. 테이핑 배치: 후방(calf/Achilles) 2개 스트립 + 전방(tibialis anterior/발등) 1개 스트립.

| 평가 항목 | 관련 지표 | 변화 (C → T) | 임상적 해석 (근거 기반) |
| --- | --- | --- | --- |
| 충격량 근사 (acc 기반) | Peak g / Resultant RMS | Peak g **−1.7%** 감소, RMS −0.8% 감소 | 테이핑 조건에서 Peak g와 RMS가 소폭 감소하는 방향이 관찰되었다. 기전 해석: 후방 스트립이 posterior talar glide를 제한함으로써 DF ROM이 감소하고[19], DF 제한이 착지 kinematic 패턴을 변화시켰을 가능성이 있다. PMC11374426은 "Deficits in ankle dorsiflexion ROM result in a more plantarflexed ankle at initial contact during running"을 보고하였으며[23], 이 착지 패턴 변화가 shank IMU peak g에 반영되었을 수 있다.<br><br>단, 이는 "테이핑이 shock absorption을 개선했다"는 직접 결론이 아니다. Cordova et al.(2000)은 ankle support가 dorsiflexion ROM 제한에 가장 큰 지지를 보임을 meta-analysis로 보고하였다.[6] 이 ROM 제한과 착지 kinematic constraint가 shank IMU proxy 소폭 감소에 반영된 탐색적 결과로 해석한다. |
| 배측굴곡 억제 | Ankle Dorsiflexion Peak | **−4.07%** 감소 | 테이핑 배치(후방 ×2 + 전방 ×1)가 sagittal plane DF ROM을 제한한 기전을 두 경로로 설명할 수 있다.<br><br>**후방 스트립(calf/Achilles)**: DF 동작 시 talus가 posterior 방향으로 glide해야 하는데, 후방 스트립이 이 glide를 기계적으로 제한한다. PMC3820234는 "tibial advancement over foot acts as ankle dorsiflexion; posterior taping may constrain posterior talar glide essential for dorsiflexion"을 보고하였다.[20]<br><br>**전방 스트립(tibialis anterior/발등)**: tibialis anterior 부위의 I-shape 스트립은 tibial advancement over foot를 기계적으로 제한하고 cutaneous sensory input을 제공한다. PMC9498427은 "tibialis anterior I-shaped strip provides mechanical constraint AND proprioceptive sensory input"을 보고하였다.[21]<br><br>PMC10393384(2024)는 단회기 테이핑에서 "ankle taping effectively decreased the ankle dorsiflexion ROM immediately after application in male and female basketball players"를 보고하였다.[22] Cordova et al.(2000)은 "taping offered the most support for limiting dorsiflexion ROM"을 meta-analysis로 확인하였다.[6] Chinn et al.(2014)은 만성 발목 불안정성 피험자에서 taping 후 jogging에서 더 적은 dorsiflexion을 보고하였다.[7] |
| 족저굴곡 peak | Ankle Plantarflexion Peak | **+5.78%** 증가 (메트로놈 +34.7%보다 훨씬 작음) | 목표 1과 동일한 지표: **push-off/terminal stance PF peak**(stride의 ~20-30%). DF 제한 → 발목의 sagittal ROM이 전반적으로 PF 방향으로 편향 → push-off PF peak 소폭 증가 가능성. PMC11374426은 "Deficits in ankle dorsiflexion ROM result in a more plantarflexed ankle at initial contact during running"을 보고하였으며[23], DF 제한이 전반적인 ankle 작동 범위를 PF 방향으로 이동시켰을 수 있다.<br><br>+5.78%는 메트로놈 조건(+34.7%)에 비해 매우 작은 변화로, 테이핑 단독으로는 push-off PF peak의 큰 변화가 나타나지 않았다는 관찰과 일치한다. Chinn et al.(2014)은 walking 후 taping에서 less plantarflexion을 보고하였으나[7], 본 데이터는 소폭 증가 방향이었다. 이는 running vs walking의 역학 차이, 혹은 테이핑의 DF 제한이 push-off PF range를 오히려 증가시키는 방향으로 작용했을 가능성에서 비롯될 수 있다. |
| 골반 자세 안정성 | Pelvis Pitch SD / Roll SD | Pitch SD **+6.67%** (n=6, 2.2324→2.3813)<br>Roll SD **+51.03%** (n=6, 8.7835→13.2661) | 테이핑 단독 조건에서 Roll SD가 51% 급증하였다. 이는 발목 기계적 constraint가 proximal 분절(골반)로 보상적 운동을 유발한 결과일 가능성이 있다. 발목의 sagittal plane ROM이 제한되면 보행 역학적 에너지를 골반/체간의 측면 움직임으로 분산시키는 보상 패턴이 나타날 수 있다.<br><br>이 결과는 "테이핑이 골반 안정성을 개선한다"는 가설과 반대 방향이며, 테이핑이 발목 레벨의 역학을 제한하는 동시에 상위 분절에서 보상적 불안정성을 증가시킬 수 있음을 시사한다. 직접 러닝 근거는 발견되지 않으며, N=6 탐색 결과로 보고한다. |
| 보폭의 일관성 | Step Interval CV% | **−10.24%** 감소 | 테이핑 조건에서 step timing variability가 낮아지는 방향이 관찰되었다. 두 기전이 제안된다: (1) ankle mechanical constraint → foot-shank coupling의 운동 패턴 일관화, (2) cutaneous mechanoreceptor 자극 → 감각 입력 강화 → motor output 일관화.<br><br>보행 배경 근거(limited transfer): Wang et al.(2021)은 비탄성 테이핑 후 보행에서 "stride time variability showed a statistically significant decrease. Mechanism: restricted joint ROM AND changed sensorimotor neural circuit"을 보고하였다.[24] Hertel et al.(2020)은 보행에서 "bracing diminished coordination variability of foot-shank, foot-thigh, shank-thigh couplings during swing phase"를 보고하였다.[26]<br><br>단, 이들은 모두 **보행 연구**로 러닝에 직접 적용할 수 없다. 러닝 연구 PMC11594344(2024)는 treadmill running에서 ankle taping이 running kinematics에 유의한 차이를 만들지 않았음을 보고하였다(null result).[29] Raymond et al.(2012)은 tape/brace가 proprioceptive acuity에 일관된 전체 효과를 보이지 않았음을 meta-analysis로 보고하였다.[8] 따라서 본 Step CV −10.24% 감소는 N=6 탐색 결과로 보고하며, 러닝 특이적 직접 근거가 부족함을 명시한다. |

---

## [목표 3] Tape + Metro 복합 효과 분석

발목 테이핑을 적용한 상태에서 메트로놈 자극이 추가되었을 때(Control → Tape+Metro, Tape → Tape+Metro)의 복합 조건 변화와 동시 적용 패턴을 검토했습니다.

| 평가 항목 | 관련 지표 | 복합 조건 결과 (C → T+M) | 메트로놈 추가 효과 (T → T+M) | 종합 분석 |
| --- | --- | --- | --- | --- |
| 충격량 근사 (acc 기반) | Peak g / Resultant RMS | Peak g **+3.57%**, RMS +2.09% | Peak g +5.44%, RMS +2.97% | Tape 단독에서는 Peak g가 −1.7% 감소 방향이었으나, Tape+Metro에서는 Control 대비 오히려 증가하였다. 복합 조건은 mechanical ankle constraint(테이핑)와 external temporal cue(메트로놈)가 동시에 부과된 dual constraint 조건으로 볼 수 있다. 이는 formal interaction model을 검정한 결론이 아니라 관찰 패턴 기반 해석이며, 메트로놈으로 인한 고강도 cadence 조절 부담이 테이핑의 소폭 감소 방향을 역전시킨 결과로 해석된다. 따라서 복합 조건은 충격량 proxy 감소 목적에 일관된 이득을 보이지 않았다. |
| 보폭의 일관성 | Step Interval CV% | **+4.50%** | **+16.41%** | Tape 단독에서는 CV% −10.24%(감소, 일관성 향상)였으나, 메트로놈을 추가하면 CV%가 크게 증가하였다. Tape+Metro에서의 CV% 급증(T→T+M: +16.41%)은 ankle constraint 위에 external temporal cue가 추가되면서 timing 조절 task demand가 더 커진 결과로 해석된다. 러닝에서 외부 박자 동기화가 step variability를 감소시키지 못한다는 직접 근거(Ludwig 2011[27], PMC7288070[28])와 일치하는 방향이다. Tape+Metro의 핵심 결과는 step timing variability 증가이다. |
| 골반 자세 안정성 | Pelvis Pitch SD / Roll SD | Pitch SD +2.69%<br>Roll SD +16.34% | Pitch SD −3.73%<br>Roll SD **−22.97%** | Tape 단독에서 Roll SD가 +51.03%로 급증했으나, 메트로놈 추가(T→T+M) 시 −22.97%로 낮아지는 방향이 관찰되었다. 그러나 Control 대비(C→T+M)로는 여전히 +16.34% 증가 상태이다. 이는 "테이핑 단독에서 51%였던 Roll SD 증가가 복합 조건에서 16%로 낮아졌으나, Control 대비 골반 안정성은 여전히 악화된 상태"임을 의미한다. 메트로놈이 테이핑으로 생긴 측면 흔들림을 일부 완화했을 가능성은 있으나, 방향성 관찰에 그치므로 골반 안정화 효과로 단정하기는 어렵다. |
| 발목 운동학 변화 | Ankle PF / DF / ROM | PF +36.09%, DF −8.31%, DP/PF ROM +3.87% (n=5) | PF +18.96%, DF −2.53%, DP/PF ROM +10.31% (n=5) | Tape+Metro에서는 Plantarflexion이 크게 증가하고 Dorsiflexion은 감소하는 방향이 관찰되었다. 이는 propulsive force 또는 ankle power 증가가 아니라, external temporal cue에 따른 push-off PF peak 증가(stride의 ~20-30%, terminal stance 구간)와 테이핑의 sagittal DF constraint가 동시에 나타난 패턴으로 해석된다. 단, 이 조건에서 1명(진현준) 발목 지표가 이상치로 제외되어 발목 관련 분석은 **n=5 기준**이다. |

---

## 신규 참고문헌 (기존 [1]–[15] 유지, 아래 추가)

16. Yong, J. R., Silder, A., & Delp, S. L. (2018). Acute changes in foot strike pattern and cadence affect running parameters associated with tibial stress fractures. *Journal of Biomechanics, 76*, 62-67. doi:10.1016/j.jbiomech.2018.05.017. *요지: acute cadence 증가 및 forefoot 착지 전환 시 발목이 더 plantarflexed 위치에 놓인다. 본 보고서에서는 보조 배경 근거로 사용 (loading phase 관련).*

17. — (2025). Biomechanical strategies to improve running: Cadence, footwear, and orthoses. *PMC12031012*. *요지: 10% cadence 증가 → peak ankle dorsiflexion 25.80°→23.59° 감소. 발목이 stance 전반에 걸쳐 더 plantarflexed 상태 유지.*

18. Meyns, P., Van de Walle, P., Leys, N., Swinnen, E., & Calenbergh, F. V. (2018). What are the effects of internal and external focus of attention on gait kinematics and variability? *Scientific Reports, 8*, 16515. *요지: external auditory cueing이 gait variability에 부정적 영향을 줄 수 있음. 보행 연구, limited transfer.*

19. Chumanov, E. S., Wille, C. M., Michalski, M. P., & Heiderscheit, B. C. (2012). Changes in muscle activation patterns when running step rate is increased. *Gait & Posture, 36*(2), 231-235. doi:10.1016/j.gaitpost.2012.02.023. PMC3387288. *요지: step rate +10% → medial gastrocnemius activity 증가(late swing phase pre-activation). cadence 증가 시 더 많은 ankle 근육 동원의 간접 근거.*

20. — (2013). Influence of walking with talus taping on the ankle dorsiflexion passive range of motion. *Journal of Physical Therapy Science*. PMC3820234. *요지: tibial advancement over foot acts as ankle dorsiflexion; posterior taping constrains posterior talar glide essential for dorsiflexion. 후방 스트립의 DF 제한 기전.*

21. Kwon, J. W., et al. (2022). Effects of extensor digitorum longus and tibialis anterior taping on balance and gait performance. *Journal of Clinical Medicine*. PMC9498427. *요지: tibialis anterior I-shaped strip provides mechanical constraint AND proprioceptive sensory input. 전방 스트립의 이중 기전.*

22. Ruiz-Echevarría, M., et al. (2024). Is ankle taping effective to limit the ankle dorsiflexion in a single training session? *Journal of Clinical Medicine*. PMC10393384. *요지: "Ankle taping effectively decreased the ankle dorsiflexion ROM immediately after application in male and female basketball players." 단회기 즉각 DF 제한 직접 근거.*

23. — (2024). The effect of different degrees of ankle dorsiflexion restriction on the biomechanics of the lower extremity. *PMC11374426*. *요지: "Deficits in ankle dorsiflexion ROM result in a more plantarflexed ankle at initial contact during running." DF 제한 → PF 방향 이동 직접 기전.*

24. Wang, F., et al. (2021). Effects of nonelastic taping and dual task on kinematics and kinetics of the ankle joint. *Journal of Healthcare Engineering*. PMC7937460. *요지: "Stride time variability showed a statistically significant decrease with taping. Mechanism: restricted joint ROM AND changed sensorimotor neural circuit." 보행 연구, limited transfer.*

25. Pathak, P., & Ahn, J. (2023). Taping-induced cutaneous stimulation to the ankle tendons reduces minimum toe clearance variability. *Heliyon, 9*(1), e12682. PMC9850051. *요지: cutaneous stimulation → continuous proprioceptive afferent input → more consistent motor output. 보행 연구, limited transfer.*

26. Hertel, J., et al. (2020). Ankle bracing alters coordination and coordination variability in individuals with and without chronic ankle instability. *Journal of Sport Rehabilitation, 30*(1), 62-69. PMID 32131049. *요지: "Bracing diminished coordination variability of foot-shank, foot-thigh, shank-thigh couplings during swing phase." 보행 연구, limited transfer.*

27. Ludwig, C., Lipfert, S., & Seyfarth, A. (2011). Variability in human running is not reduced by metronome signals. *Proceedings of the International Society of Biomechanics (ISB)*. *요지: "Variability in human running is not reduced by metronome signals. The coefficient of variation in step frequency was not reduced with the metronome, and variability in gait pattern appears to be a fundamental property in human running." 러닝 직접 근거.*

28. Nombela-Manzaneque, L., et al. (2020). Cadence modulation in walking and running: pacing steps or strides? *Frontiers in Psychology*. PMC7288070. *요지: "Synchronization was achieved less often in running, especially at slow pacing frequencies." 러닝 직접 근거.*

29. — (2024). Ankle taping does not affect running kinematics during a treadmill protocol in well-trained runners. *Journal of Clinical Medicine*. PMC11594344. *요지: treadmill running에서 ankle taping 조건 간 running kinematics 유의한 차이 없음 (null result). 테이핑+러닝 Step CV 반례.*
