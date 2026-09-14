# 인용 사실검증 결과 (Independent Citation Fact-Check)

작성: 2026-06-10 · 작성자: Claude (별도 세션 재검증) · 도구: WebFetch(PMC/PubMed 원문 직접 fetch), Read(로컬 PDF)
목적: `results_interpretation_claude.html`이 인용한 **16편 전부를, 검증 로그를 신뢰하지 않고 원문에서 직접 재대조**하여 "보고서가 한 말 = 논문이 실제로 한 말"인지 확인.

> **총평: 16/16 사실 일치.** 모든 수치(%, p, d, 각도, BW/s)와 발췌가 원문과 맞았고, 방향(지지/대조/가능성) 분류도 타당했다. 발견된 흠은 **[14] 한 곳의 따옴표=의역** 문제 1건뿐.

---

## A. 메트로놈 → 충격 (보고서의 핵심·가설반대 주장)

| Ref | 보고서가 한 말 | 원문 실제 (이 세션 fetch로 확인) | 판정 |
|---|---|---|---|
| **[4] PMC6203338** (핵심 정합) | 케이던스↑로 경골 가속도 5.4/5.2/5.5g, loading rate 후족과 비유의, 감소는 forefoot만 | *"We did not find differences in peak tibial accelerations ... among running patterns."* 경골가속도 5.4±1.3 / 5.2±1.4 / **5.5±1.5g**; loading rate 후족 48.8·77.7 = 케이던스 48.0·77.7 (비유의), 전족만 28.8·41.6 (p<0.001). 속도 timing gate ±5%. 17 recreational runners | ✅ 정확 |
| [1] PMC3022995 Heiderscheit 2011 | braking impulse↓, impact transient↓(χ²=33.8), 무릎흡수 −20%/−34%, 속도고정 | *"impact transient occurrence ... decrease (χ²=33.8, p<0.001)"*; braking impulse p<0.01↓; *"~20% and ~34% less energy ... at the knee ... increased 5% and 10%"*; 속도 일정 | ✅ 정확 |
| [2] PMC8329321 | 메트로놈 cadence +7.3%, peak force −5.6%(p<.05), GPS로 속도유지, 15명 | *"Cadence differences of 7.3% ... (p<0.001)"*; *"decrease of average peak force of 5.6% ... (p<0.05)"*; MetroTimer app; GPS watch로 pace 유지; 15 recreational runners | ✅ 정확 |
| [3] PMC8772793 | +10%에서 vGRF −2.8%, braking −8.6%, rearfoot DF −1.58°, eversion −0.79°, 메트로놈 | vGRF *"approximately a 2.8% decrease"*; braking *"8.6% decrease"*; DF −1.58°(25.85→24.27), eversion −0.79°; 메트로놈 cue; 20 runners | ✅ 정확 |
| [5] PMC4000471 Schubert 2014 | "more plantar flexed at initial contact with increased stride rate"; stride rate↑→GRF·shock·관절흡수↓ | *"the ankle demonstrating a more plantar flexed position at initial contact with increased stride rate."* + GRF·shock attenuation·관절 흡수에너지 감소(체계적 고찰) | ✅ 정확 |
| [6] PMC12440572 (2025 고찰) | 5–10%↑ → loading↓ consistent; 저cadence(≤166) tibial injury 6–7배 | *"A moderate increase in cadence (5-10%) led to ... reduced vertical ground reaction forces, lower loading rates"*; ≤166spm vs ≥178spm tibial injury 6–7배 | ✅ 정확 |
| [7] PubMed 8849811 Farley 1996 | leg stiffness 2.3배↑(7.0→16.3 kN/m), 2.5 m/s | *"leg spring increased by 2.3-fold from 7.0 to 16.3 kNm-1 between the lowest and highest stride frequencies"*; treadmill 2.5 m/s | ✅ 정확 |
| [8] PMC6269547 Kulmala 2018 | maximalist 신발에서 impact peak·loading rate +10.7%·+12.3%, "신발 연구이지 케이던스 아님" | *"impact peak and loading rate were 10.7% and 12.3% greater ... in the maximalist shoe"*; *"stiffer leg ... diminish the impact attenuation effect"*; **신발 쿠셔닝 연구, cadence 통제** | ✅ 정확 (단서까지 옳음) |

→ 보고서가 "지배적 문헌은 우리(충격↑)와 **반대**(⚠️대조)"라 한 것이 사실 그대로다. 그리고 가장 위험했던 "충격이 안 줄어도 분절가속도 문헌과는 모순 아님" 주장의 버팀목 **[4]가 정확히 일치**한다 — 게다가 [4]는 경골 가속도계를 써 본 실험 shank IMU와 같은 신호다.

## B. 메트로놈 → 보폭 변동성

| Ref | 보고서가 한 말 | 원문 실제 | 판정 |
|---|---|---|---|
| [9] PMC3466237 | "No effect of RAC on fluctuation magnitude (SD)"; dual-constraint anti-persistent; 20명 건강 | *"No effect of RAC on fluctuation magnitude (SD) was observed"*; *"anti-persistent under dual-constraints (treadmill+RAC)"*; 20 healthy adults | ✅ 정확 |
| [10] PMC3424126 Hove | stride interval variability "significantly lower"; persistence→anti-persistence; 외부박자 부자연 리듬 | SIV *"significantly lower"*; *"override the naturally occurring statistical persistence"*; *"walking to an external beat may impose unnatural neuromuscular rhythms ... loss of functional adaptability"*; 15 healthy | ✅ 정확 |
| [11] PubMed 22871238 | 건강 고령자 변동성 미증가, cadence +1 step/min | *"variability ... did not increase with either cue type"*; *"small increase in cadence of 1 step/min"*; 19 healthy older adults | ✅ 정확 |
| [12] PubMed 35020171 Cronström | 낙상고령자 20명, "increase stride time variability", limited transfer | *"may reduce double leg support variability ... but seem to increase stride time variability"*; **20 older adults, 71±4.9yr, history of falls, walking** | ✅ 정확 (limited transfer 처리 옳음) |

→ 건강 성인에서 메트로놈은 변동성 크기를 **키우지 않는다**(본 결과와 반대). 유일하게 같은 방향인 [12]는 대상이 낙상 고령자·보행이라 보고서가 "limited transfer"로 제한한 것이 정확.

## C. 테이핑

| Ref | 보고서가 한 말 | 원문 실제 | 판정 |
|---|---|---|---|
| [13] PMC4080591 Chinn 2014 | 조깅에서 less dorsiflexed(12–21%), "more neutral", 15 CAI | jogging *"less dorsiflexed (MD=4.91°), from 12% to 21%"*; *"more neutral ankle position"*; 15 CAI, walk 1.34 / jog 2.68 m/s | ✅ 정확 |
| **[14] NBK68419 Cordova 2000** | **"taping offered the most support for limiting dorsiflexion ROM"** (따옴표) | 원문 요약 표현: *"Tape braces (mean −0.94) gave more support than lace-up braces (mean −0.51)"* — **의미(테이핑이 DF ROM 제한 최강)는 일치하나, 보고서 따옴표는 축자인용이 아니라 의역** | ⚠️ 의미 일치, **인용형식만 수정 권장** |
| [15] PubMed 22513304 Raymond 2012 | 테이핑/브레이스 고유수용성 무효과, MD 0.08°(−0.39–0.55) | *"no effect on proprioceptive acuity ..."*; *"mean difference: 0.08°, 95% CI: −0.39 to 0.55"* | ✅ 정확 |
| [16] Yong 2014 (로컬 PDF) | FFS 11±5°PF vs RFS 6±4°DF (p=0.023), gastroc↑·TA↓, FFS impact peak↓ | (PDF p.3595) *"11±5° of plantarflexion in the FFS ... compared to 6±4° of dorsiflexion in the RFS (p=0.023)"*; medial/lateral gastroc p=0.004/0.001, TA p=0.001; *"reduced impact peak"* for FFS; 12 RFS+10 FFS, 4.0 m/s | ✅ 정확 |

→ [15]로 "CV감소=고유수용성"을 금지, [16]으로 "PF↑=충격원인"을 금지한 것 모두 원문과 부합.

---

## 발견된 유일한 흠과 조치

**[14] Cordova 2000**: 보고서가 따옴표(직접인용)로 적은 *"taping offered the most support for limiting dorsiflexion ROM"*는 NBK68419 요약의 실제 문장(*"Tape braces gave more support than lace-up braces"*)을 **의역한 것**이다. 사실관계(테이핑이 dorsiflexion ROM 제한에 가장 효과적)는 옳다.
→ **조치 권장:** `results_interpretation_claude.html`의 [14] 발췌에서 따옴표를 풀고 "요지(paraphrase)"로 표기하거나, 원문 문장으로 교체. (나머지 15편의 따옴표 발췌는 원문 그대로였음.)

## 등급 일치 확인
`verification_log.md`의 전문/초록 등급도 이 세션 재확인과 일치: 전문 = [1][4][9][10][13][16] 등, 초록/요약 = [7][11][12][15] 등.

## 이 세션 fetch 기록 (재현용)
- 직접 fetch 확인: PMC6203338, PMC3022995, PMC8329321, PMC8772793, PMC4000471, PMC6269547, PubMed 8849811, PMC12440572, PMC3466237, PMC3424126, PubMed 22871238, PubMed 35020171, PMC4080591, NBK68419, PubMed 22513304 — 모두 2026-06-10 fetch.
- 로컬 PDF 직접 읽음: `literature_pack/02_mechanistic_support/yong_2014_forefoot_rearfoot_emg.pdf` (p.1–3).

> **결론: 보고서의 문헌 근거는 신뢰하고 그대로 인용 가능.** [14] 인용형식 1건만 손보면 된다.
> (별개 사안: 통계 해석 틀 — 40개 검정의 다중비교 미보정, n=5 Wilcoxon 최소 p=.0625 — 과 가설↔측정축 매핑(pelvis "rotation"=yaw vs 분석한 roll)은 데이터 해석 차원에서 별도 보완 권장.)
