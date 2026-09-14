# 검증된 근거 발췌 (Verified Evidence Excerpts)

작성: 2026-06-10 · 작성자: Claude · 검증 방법: WebFetch로 원문(PMC/PubMed/출판사) 직접 fetch, 또는 로컬 PDF 직접 읽기.

## 이 문서의 목적과 사용 규칙

사용자 요구: **검증되지 않은 내용을 사실로 쓰지 않는다.** 이 문서는 `results_interpretation_claude.html`이 인용하는 모든 문장의 **원문 근거**를 1:1로 남긴다. 발췌(quote)는 **영어 원문 그대로** 두었다(번역 시 의미 왜곡 위험 제거). 한국어는 주석·경계 설명이다.

### 검증 등급
- **✅ 전문 검증**: 논문 본문(full text)을 직접 fetch/읽어 해당 문장·수치를 확인.
- **◐ 초록/요약 검증**: 초록 또는 공식 구조화 요약만 확인. 본문 세부는 미확인.
- **⛔ 미검증**: 원문 확인 실패. → **본문에서 사실로 인용 금지.** (현재 인용 목록에는 없음)

### 인용 시 색상/등급 규칙 (해석 HTML과 연동)
- ✅지지(support): 우리 결과 **방향과 같고** 대상·변수가 가깝다.
- ⚠️대조(contrast): 선행연구의 지배적 방향이 우리 결과와 **반대**다.
- 🔬기전적 가능성(mechanistic possibility): 직접 측정 안 했으나 생체역학적 연결이 있는 **가설 수준**.
- ❓프로토콜 정보 필요: 우리 측정 조건(특히 러닝 속도 통제 여부)이 불명해 판단 보류.

---

# A. 핵심결과 1 — 메트로놈/케이던스 증가와 충격(shock) proxy

우리 결과: `results/statistical_tests.csv` 기준 C→M `shank_mean_peak_g` **+7.51%** (d=1.17, p=0.0625, n.s.), `shank_resultant_rms` **+3.43%** (d=1.20, p=0.0625). 가설은 "충격 감소". → **방향 반대.**

### A1. Heiderscheit et al. 2011 — ✅ 전문 검증
- 출처: Med Sci Sports Exerc 43(2):296-302. https://pmc.ncbi.nlm.nih.gov/articles/PMC3022995/ (fetch 2026-06-10)
- 속도 통제: **"Running speed was self-selected by each subject and maintained across conditions."**
- 발췌: "Step length (p<0.01) ... breaking impulse (p<0.01) and peak knee flexion angle (p<0.01) were observed to decrease with increasing step rate." / Step length 100.8→96.0→91.9 cm (preferred/+5%/+10%). / Braking impulse 306.0→274.1→256.7 N·s/kg. / "As step rate increased, the impact transient occurrence was found to decrease (χ2 =33.8, p<0.001)." / "~20% and ~34% less energy was absorbed at the knee when preferred step rate was increased 5% and 10%." / "The ankle joint displayed a reduction in energy generation with step rate."
- **분류: ⚠️대조.** 정속에서 케이던스↑는 loading(보폭·braking·impact transient·관절 흡수)을 **낮춘다**. 우리 결과(증가)와 반대.

### A2. (야외 케이던스·메트로놈) PMC8329321 — ✅ 전문 검증
- 출처: "Effect of Increasing Running Cadence on Peak Impact Force in an Outdoor Environment." https://pmc.ncbi.nlm.nih.gov/articles/PMC8329321/ (fetch 2026-06-10)
- 발췌: 메트로놈 사용 "implemented using the MetroTimer metronome app." / "Cadence differences of 7.3% were observed." / "A concurrent decrease in average peak force of 5.6% was demonstrated during the cadence run (p<0.05)." (2.539→2.396 BW) / 속도 통제 "instructed to maintain that pace with use of GPS watch." / 대상 15 recreational runners.
- **분류: ⚠️대조 + ✅(메트로놈으로 케이던스 부과 가능).** 속도 통제 시 케이던스↑ → peak force↓.

### A3. (Step rate, rearfoot, GRF) PMC8772793 — ✅ 전문 검증
- 출처: "Increasing Step Rate Affects Rearfoot Kinematics and Ground Reaction Forces during Running." https://pmc.ncbi.nlm.nih.gov/articles/PMC8772793/ (fetch 2026-06-10)
- 발췌: "+5% and +10% of their preferred step rate while being cued by a metronome." / "Peak vertical ground reaction force was significantly reduced in the +10% step rate condition ... approximately a 2.8% decrease." / Braking force "8.6% decrease." / "Increasing step rate significantly decreased peak sagittal and frontal plane rearfoot and tibial rotation angles" (rearfoot dorsiflexion −1.58°, eversion −0.79°). / 대상 20 runners.
- **분류: ⚠️대조 + 발목/후족 운동학 참고.**

### A4. (Foot strike·cadence·tibial accel) PMC6203338 — ✅ 전문 검증 — **핵심 nuance**
- 출처: "Acute Changes in Foot Strike Pattern and Cadence Affect Running Parameters Associated with Tibial Stress Fractures." https://pmc.ncbi.nlm.nih.gov/articles/PMC6203338/ (fetch 2026-06-10)
- 발췌: "peak tibial acceleration was 5.4 ± 1.3 g [rearfoot], compared to 5.2 ± 1.4 g during forefoot striking trials and **5.5 ± 1.5 g during increased cadence trials**." (즉 케이던스↑로 경골 가속도 **감소 안 함**) / "Increased cadence trials had average and peak instantaneous loading rates of 48.0 ± 9.3 and 77.7 ± 20.0 BW/s, which were **not significantly different from rearfoot striking trials**." / 반면 forefoot은 loading rate를 낮춤(77.7→41.6 BW/s). / 속도 통제 "Consistency in speed was ensured using the timing gates." / 대상 17 habitual rearfoot recreational runners.
- **분류: ✅(가장 중요한 정합 근거).** GRF loading은 케이던스로 낮아져도, **경골/분절 가속도(우리 shank IMU가 측정하는 바로 그 신호)는 케이던스 증가만으로 감소하지 않는다**는 통제 연구. 우리의 shock proxy 비감소/소폭증가가 분절 가속도 문헌에서는 이례적이지 않음을 뒷받침.

### A5. Schubert et al. 2014 — ✅ 전문 검증
- 출처: Sports Health 6(3):210-217 (systematic review). https://pmc.ncbi.nlm.nih.gov/articles/PMC4000471/ (fetch 2026-06-10)
- 발췌: "Changes at the ankle joint were observed, with the ankle demonstrating a **more plantar flexed position at initial contact with increased stride rate**." / "There was consistent evidence that increased stride rate resulted in decreased center of mass vertical excursion, ground reaction force, shock attenuation, and energy absorbed at the hip, knee, and ankle joints."
- **분류: ⚠️대조(loading) + ✅(plantarflexed ankle = 우리 PF↑ 해석 지지).**

### A6. (2025 cadence review) PMC12440572 — ✅ 전문 검증
- 출처: "The Influence of Running Cadence on Biomechanics and Injury Prevention: A Systematic Review." https://pmc.ncbi.nlm.nih.gov/articles/PMC12440572/ (fetch 2026-06-10)
- 발췌: "A moderate increase in cadence (typically 5-10%) led to consistent biomechanical improvements, including reduced vertical ground reaction forces, lower loading rates, shorter stride length." / 저케이던스(≤166 spm)는 ≥178 spm 대비 tibial injury 위험 약 6-7배.
- **분류: ⚠️대조.** 리뷰 수준에서 케이던스↑ → loading↓가 "consistent". (단, 이 리뷰는 경골 *가속도* 특이적 불일치는 별도 보고하지 않음 → A4가 그 nuance를 담당.)

### A7. Farley & González 1996 — ◐ 초록 검증
- 출처: J Biomech 29(2):181-186. https://pubmed.ncbi.nlm.nih.gov/8849811/ (fetch 2026-06-10)
- 발췌: "The stiffness of the leg spring increased by 2.3-fold from 7.0 to 16.3 kNm-1 between the lowest and highest stride frequencies." (treadmill 2.5 m/s) / "the most important adjustment ... is that leg spring becomes stiffer."
- **분류: 🔬기전적 가능성(1단계).** stride frequency↑ → leg stiffness↑.

### A8. Kulmala et al. 2018 — ✅ 전문 검증
- 출처: Sci Rep 8:17496. https://pmc.ncbi.nlm.nih.gov/articles/PMC6269547/ (fetch 2026-06-10)
- 발췌: "ground reaction force impact peak and loading rate were 10.7% and 12.3% greater, respectively, in the maximalist shoe" (14.5 km/h). / "The stiffer leg during the landing phase in MAX shoes can diminish the impact attenuation effect." / 12 healthy male runners, 10 & 14.5 km/h.
- **분류: 🔬기전적 가능성(2단계).** leg stiffness↑ → impact loading↑. **주의: 신발(쿠셔닝) 연구이지 케이던스 연구가 아님.** 따라서 "케이던스→stiffness→impact" 사슬은 A7+A8을 이은 **가설**일 뿐, 직접 측정 아님.

---

# B. 핵심결과 2 — 메트로놈과 보폭 타이밍 변동성(step interval CV)

우리 결과: C→M `step_interval_cv_pct` **+5.09%** (p=1.0, n.s.); **T→T+M +16.41% (p=0.0312, d=1.39, 유의)**. 가설은 "일관성 증가(CV 감소)". → **방향 반대**, 그리고 복합조건에서 유의.

### B1. Terrier & Deriaz / Roerdink 계열 — PMC3466237 — ✅ 전문 검증
- 출처: "Step-to-Step Variability in Treadmill Walking: Influence of Rhythmic Auditory Cueing." https://pmc.ncbi.nlm.nih.gov/articles/PMC3466237/ (fetch 2026-06-10)
- 발췌: "**No effect of RAC on fluctuation magnitude (SD) was observed.**" / 과거 연구에서는 RAC가 "markedly reduced stride to stride variability of stride time at low speed." / 구조 변화: "RAC deeply modifies statistical persistence of stride time, while fluctuation magnitude (CV) remained unchanged." / dual constraints(treadmill+RAC)에서 "stride time ... exhibited an **anti-persistent pattern**" (편차 뒤 과보정). / 20 healthy adults.
- **분류: ⚠️대조(크기 미증가) + 🔬(dual-constraint anti-persistent = 우리 T→T+M 복합조건 기전 가설).**

### B2. Hove et al. — PMC3424126 — ✅ 전문 검증
- 출처: "The Effects of Rhythmic Sensory Cues on the Temporal Dynamics of Human Gait." https://pmc.ncbi.nlm.nih.gov/articles/PMC3424126/ (fetch 2026-06-10)
- 발췌: 청각 메트로놈에서 stride interval variability "significantly lower." / 메트로놈이 fractal scaling을 "from ... statistical persistence ... to one of anti-persistence"로 이동. / "walking to an external beat may impose unnatural neuromuscular rhythms ... resulting in a loss of functional adaptability." / 15 healthy adults.
- **분류: ⚠️대조(크기 오히려 감소) + 🔬(과보정 기전).**

### B3. (Music vs metronome, 건강 고령자) PubMed 22871238 — ◐ 초록 검증
- 출처: Gait Posture. https://pubmed.ncbi.nlm.nih.gov/22871238/ (fetch 2026-06-10)
- 발췌: "Mean spatio-temporal variability was low at baseline and **did not increase with either cue type**." / metronome은 cadence +1 step/min. / 19 healthy older adults.
- **분류: ⚠️대조(크기 미증가).**

### B4. Cronström et al. 2022 — ◐ 초록 검증 — **유일한 증가 보고, 단 transfer 약함**
- 출처: Aging Clin Exp Res. https://pubmed.ncbi.nlm.nih.gov/35020171/ (fetch 2026-06-10)
- 발췌: "Metronome cueing strategies may reduce double leg support variability in older adults with a history of falls but **seem to increase stride time variability**." / 대상 **20 older adults (15 women, 71 ± 4.9 yr) with a history of falls**, walking.
- **분류: ✅(방향 일치) 단 ⚠️limited transfer.** 낙상 고령자·보행 연구 → 우리 건강군·러닝·테이핑 복합과 대상·동작이 다름. 직접 근거로 과신 금지.

---

# C. 테이핑 결과 (가설 방향과 대체로 일치)

우리 결과: C→T `shank_mean_peak_g` −1.77%(n.s.), `ankle_mean_dorsiflexion_peak` **−4.07%**(n.s., d=−0.27), `ankle_mean_plantarflexion_peak` +5.78%(n.s.), `step_interval_cv_pct` **−10.24%**(p=0.0938, d=−0.67).

### C1. Chinn et al. 2014 — ✅ 전문 검증
- 출처: J Athl Train 49(3):322-330. https://pmc.ncbi.nlm.nih.gov/articles/PMC4080591/ (fetch 2026-06-10)
- 발췌: walking "less plantar flexed ... (mean difference = 5.73° ± 0.54°)"; jogging "**less dorsiflexed** from 12% to 21%"; 결론 "taping resulted in a **more neutral ankle position** during walking and jogging in shoes on a treadmill." / 15 CAI(만성 발목 불안정성), treadmill walk 1.34 / jog 2.68 m/s.
- **분류: ✅(우리 DF↓ 지지)** 단 대상이 CAI → 건강군 transfer 주의, 동작은 jog(2.68 m/s).

### C2. Cordova et al. 2000 — ◐ 구조화 요약 검증
- 출처: JOSPT 30(4):170-177 (meta-analysis). https://www.ncbi.nlm.nih.gov/books/NBK68419/ (fetch 2026-06-10)
- 발췌: "**taping offered the most support for limiting dorsiflexion ROM**." (frontal plane는 semi-rigid가 최대 제한)
- **분류: ✅(테이핑이 dorsiflexion ROM 제한).**

### C3. Raymond et al. 2012 — ✅ 초록 검증(메타분석 결론)
- 출처: J Sci Med Sport 15(5):386-392. https://pubmed.ncbi.nlm.nih.gov/22513304/ (fetch 2026-06-10)
- 발췌: "The pooled evidence suggests that using an ankle brace or ankle tape has **no effect on proprioceptive acuity** in participants with recurrent ankle sprain or who have functional ankle instability." / "no significant effect ... (mean difference: 0.08°, 95% CI: −0.39 to 0.55)."
- **분류: ⚠️주의/반대 근거.** 테이핑 CV 감소를 "고유수용성 향상"으로 설명 금지.

### C4. Yong et al. 2014 — ✅ 전문 검증 (로컬 PDF 직접 읽음)
- 출처: J Biomech 47(15):3593-3597. 로컬: `literature_pack/02_mechanistic_support/yong_2014_forefoot_rearfoot_emg.pdf` (read 2026-06-10)
- 발췌: "The mean ankle angle at foot contact was **11 ± 5° of plantarflexion in the FFS runners compared to 6 ± 4° of dorsiflexion in the RFS runners (p=0.023)**." / FFS는 late swing에서 medial/lateral gastrocnemius RMS 유의 증가, tibialis anterior 감소. / "the vertical ground reaction forces for the natural FFS runners demonstrated a **reduced impact peak** compared to the RFS runners." / 12 RFS + 10 FFS healthy runners, treadmill 4.0 m/s.
- **분류: ✅(plantarflexed ankle = forefoot strategy 해석 지지).** 주의: forefoot/plantarflexed는 impact peak를 **낮추는** 쪽 → 우리 PF↑를 "충격 증가 원인"으로 쓰면 안 됨.

---

# D. 본 보고서에서 인용하지 않거나 강등한 항목 (정직성 기록)

- **"메트로놈이 충격을 줄였다" 직접 지지 논문**: 없음. 오히려 A1·A2·A3·A5·A6가 반대. → 우리 충격결과는 ⚠️대조/탐색으로만 기술.
- **"메트로놈이 보폭 일관성(CV)을 높였다(개선)" 직접 지지**: 없음. B1·B2·B3는 크기 미증가/감소. → 우리 CV결과는 ⚠️대조 + 🔬가능성으로 기술.
- **"plantarflexion 증가 = push-off/추진력 증가"**: 직접 측정(발목 파워·모멘트·추진 GRF·EMG) 없음 → 본문 사용 금지. PF↑는 ankle strategy/posture로만.
- **IMU 적분값 = GRF impulse**: 등치 금지. acceleration-time load proxy로 한정.
- **Williams 2012, Hamner 2010, Thaut 1993, Terrier&Deriaz 2012(PLoS 별도본)**: 이번 본문 핵심 인용에서 제외(전문 재검증 미수행 또는 배경용). 필요 시 별도 검증 후 추가.
