# 핵심 결과의 직접 근거 탐색 결과 (Core-Result Evidence Landscape)

작성: 2026-06-10 · 작성자: Claude
우선순위 지시: "핵심 결과 직접 근거". 핵심 결과 = **가설과 반대로 나온 메트로놈 2건** (① 메트로놈→충격 proxy 증가, ② 메트로놈→step CV 증가).

> **가장 중요한 정직성 결론 (먼저 읽으세요)**
> 이 두 핵심 결과를 **"직접 지지"하는 논문을 찾으려 했으나, 지배적 문헌은 오히려 반대 방향입니다.**
> 따라서 올바른 과학적 처리는 *지지 인용을 억지로 만드는 것*이 아니라, **(a) 문헌의 지배적 방향을 정직히 제시하고, (b) 우리 결과를 그와 다른 탐색/대조 결과로 규정하며, (c) 검증된 기전적 *가능성*과 측정 한계를 분리해 제시**하는 것입니다. 이렇게 해야 잘못된 주장으로 인한 출판 리스크를 피할 수 있습니다.
> 모든 발췌의 원문 근거는 [evidence_excerpts_verified.md](evidence_excerpts_verified.md)에 있습니다.

---

## 핵심결과 ① 메트로놈 → 충격(shock) proxy 증가

우리 측정: C→M shank peak g **+7.51%** (d=1.17), RMS +3.43%. T→T+M peak g +5.44%. (모두 n.s., 그러나 효과크기 큼)

### 문헌 지형
| 방향 | 근거(검증됨) | 핵심 수치 | 우리 결과와 |
|---|---|---|---|
| 케이던스↑ → GRF loading **감소**(지배적) | Heiderscheit 2011, PMC8329321, PMC8772793, Schubert 2014, 리뷰 PMC12440572 | braking impulse↓, peak force −5.6%, vGRF −2.8%, impact transient↓, "5–10%↑ → reduced GRF/loading rate (consistent)" | **반대** |
| 케이던스↑ → **경골/분절 가속도는 비감소**(특이적) | **PMC6203338** | 경골 가속도 5.5 vs 5.4 g (n.s.), loading rate 77.7 BW/s (n.s.); forefoot만 감소 | **정합** |
| stiffness↑ → impact↑(기전 가설) | Farley&González 1996 + Kulmala 2018 | stride freq↑→leg stiffness 2.3배↑ ; stiffer leg→impact peak +10.7% | 가설로만 |

### 해석 가능한 가장 강한 문장 (검증 근거 내)
1. (사실) "정속 러닝에서 케이던스 증가는 **GRF 기반 loading 지표**(보폭·braking impulse·impact transient·관절 흡수)를 낮추는 것이 지배적이다 [Heiderscheit 2011; PMC8772793; Schubert 2014; review PMC12440572]."
2. (사실, 핵심) "그러나 **경골/분절 가속도 자체는 케이던스 증가만으로 일관되게 감소하지 않는다.** 한 통제 연구는 케이던스 증가 시 peak tibial acceleration과 loading rate가 rearfoot 대비 유의하게 변하지 않았고, 감소는 forefoot strike에서만 나타났다고 보고했다 [PMC6203338]."
3. (해석) "본 연구의 지표는 shank IMU **합성가속도 proxy**로, GRF가 아니라 분절 가속도에 가깝다. 따라서 우리 proxy가 감소하지 않고 오히려 소폭 증가한 것은, GRF-loading 문헌과는 다르지만 **분절 가속도 특이적 문헌과는 모순되지 않는** 탐색 결과로 볼 수 있다."
4. (가능성, 🔬) "기전적으로는 더 높은 step frequency 적응 과정에서 leg stiffness가 커지고 [Farley&González 1996], 더 단단한 다리가 충격 노출을 키울 수 있다 [Kulmala 2018]는 사슬이 *가능성*으로 제시될 수 있다. 단 본 연구는 stiffness·GRF를 측정하지 않았고, Kulmala는 신발 연구이므로 직접 증거가 아니다."
5. (한계, ❓) "가장 큰 미확인 변수는 **러닝 속도 통제 여부**다. 위 선행연구들은 모두 속도를 고정했다. 본 프로토콜에서 메트로놈으로 케이던스를 올릴 때 속도가 함께 올랐다면 loading 증가는 당연한 결과이며, 이는 생체역학적 결론이 아니라 설계 교란이다." → [data_caveats.md](data_caveats.md) 참조.

### 쓰면 안 되는 문장
- "선행연구가 메트로놈/케이던스 증가로 충격이 커진다는 것을 지지한다." (거짓 — 반대)
- "본 결과는 메트로놈이 충격을 증가시킨다는 것을 입증했다." (n.s., N=6, proxy)

---

## 핵심결과 ② 메트로놈 → 보폭 타이밍 변동성(step interval CV) 증가

우리 측정: C→M CV **+5.09%** (n.s.); **T→T+M CV +16.41% (p=0.0312, d=1.39, 유의).**

### 문헌 지형
| 방향 | 근거(검증됨) | 핵심 발췌 | 우리 결과와 |
|---|---|---|---|
| 건강 성인에서 메트로놈은 변동성 **크기 미증가/감소** | PMC3466237, PMC3424126, PubMed 22871238 | "No effect of RAC on fluctuation magnitude (SD)"; SIV "significantly lower"; "did not increase with either cue type" | **반대** |
| 메트로놈은 변동성 **구조**를 anti-persistent로(과보정) | PMC3466237, PMC3424126 | "anti-persistent pattern"; persistence→anti-persistence | 기전 가능성 |
| 메트로놈이 stride time variability **증가**(유일) | Cronström 2022 | "seem to increase stride time variability" | 방향 일치, 단 대상=낙상 고령자 |

### 해석 가능한 가장 강한 문장 (검증 근거 내)
1. (사실) "건강 성인 보행에서 리듬 청각 자극(RAC)/메트로놈은 보폭시간 변동성의 **크기(SD/CV)를 키우지 않으며, 오히려 줄이거나 변화시키지 않는다** [PMC3466237; PMC3424126; PubMed 22871238]."
2. (사실/기전) "대신 메트로놈은 변동성의 **시간적 구조**를 바꾼다 — 자연 보행의 persistence를 **anti-persistence(편차 직후 과보정)**로 전환시킨다 [PMC3466237; PMC3424126]. dual constraint(트레드밀+박자)에서 특히 뚜렷하다 [PMC3466237]."
3. (해석) "따라서 본 연구의 CV 증가, 특히 **T→T+M에서의 유의한 증가**는 건강 성인 보행 문헌과 방향이 다르다. 가능한 설명은 (a) 러닝에서의 **급성·미훈련 동기화 부담**, (b) 테이핑(기계적) + 메트로놈(시간적)의 **이중 제약**, (c) N=6 소표본이다."
4. (제한적 일치) "메트로놈이 stride time variability를 **증가**시켰다는 보고는 존재하나, 이는 **낙상 이력 고령자 20명의 보행 연구**[Cronström 2022]로 본 연구(건강군·러닝·테이핑)와 대상·동작이 달라 **limited transfer**로만 사용한다."

### 쓰면 안 되는 문장
- "메트로놈은 보폭 일관성을 개선한다(가설대로)." (우리 데이터도, 문헌의 magnitude도 이를 지지 안 함)
- "anti-persistent 기전이 우리 CV 증가를 입증한다." (구조 변화가 곧 크기 증가를 예측하지 않음 — 가능성까지만)

---

## 추가로 탐색했으나 본문 직접근거로 채택하지 않은 후보
- JSR 2025 "Running Step Rate Can Be Increased With Both Metronome and Music Auditory Cueing" (humankinetics): 메트로놈으로 러닝 케이던스 부과 가능 = 이미 Heiderscheit/PMC8329321로 충족. 전문 페이월 → 미채택.
- Wiley PM&R Souza "Cadence and tibial acceleration in runners with/without PFP": 경골가속도-케이던스 직접 다룸. 전문 미검증 → 필요 시 추가 검증 후 채택 가능(현재 PMC6203338로 핵심 nuance 충족).

## 한 줄 요약
> 핵심 메트로놈 결과 2건은 **직접 지지 근거가 없고 지배적 문헌은 반대**다. 단 ①은 "분절 가속도는 케이던스로 안 줄어든다"[PMC6203338]는 통제연구와 정합하고, ②는 "메트로놈이 변동성 구조를 바꾼다"[PMC3466237/3424126]는 기전과 연결된다. 모두 ⚠️대조/🔬가능성 수준으로 기술해야 안전하다.
