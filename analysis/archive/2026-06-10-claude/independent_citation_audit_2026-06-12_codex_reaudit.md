# Codex 재감사: 독립 인용 감사 보고서 검토 - 2026-06-12

대상:
- `analysis/2026-06-10-claude/independent_citation_audit_2026-06-12.md`
- `analysis/2026-06-10-claude/`의 관련 검증 문서
- 참고 확인: `analysis/2026-06-10/results_report_a_to_b_refined.html`

검증 방법:
- PMC 웹 화면은 reCAPTCHA에 걸려, 같은 NCBI 공식 경로인 E-utilities `efetch` XML을 사용했다.
- PubMed 초록/메타데이터, NCBI Bookshelf printable page, 로컬 PDF 2개를 직접 대조했다.
- 따옴표 문구, 수치, p-value, 문헌 적용 범위를 각각 분리해 판정했다.

## 총평

기존 `independent_citation_audit_2026-06-12.md`의 핵심 판정은 재검증 후에도 유지된다. 메인 16편과 보충 5편에서 새로 발견된 중대 오류는 없었다.

다만 기존 감사 파일이 지적한 수정 사항 4개는 실제로 고쳐야 한다.

1. Yong 2014의 ankle angle p-value는 `p=0.023`이 아니라 `p<0.001`이다. `p=0.023`은 knee flexion 문장에 붙는다.
2. Cordova 2000의 `"taping offered the most support for limiting dorsiflexion ROM"`은 NCBI Bookshelf에 실제 존재한다. 기존 `citation_factcheck_session.md`와 `acute_exposure_supplement.html`의 "의역" 판정은 오판이다.
3. Raymond 2012는 내용은 맞지만 PubMed 초록/결론 검증 수준이다. `전문 검증`으로 표시하면 과장이다.
4. PMC5832267의 `"minimal impact on timing skill transfer"`는 의미상 맞지만 축자 인용이 아니다. 원문 문구로 교체해야 한다.

## 즉시 수정 필요

| 우선순위 | 파일/위치 | 현재 문제 | 재검증 판정 | 권장 조치 |
|---|---|---|---|---|
| 높음 | `results_interpretation_claude.html:237`, `evidence_excerpts_verified.md:116`, `citation_factcheck_session.md:43`, `verification_log.md:28` | Yong ankle angle에 `p=0.023` 사용 | 로컬 PDF에서 ankle angle은 `p<0.001`, knee flexion은 `p=0.023` | ankle angle p-value를 `p<0.001`로 수정 |
| 중간 | `citation_factcheck_session.md:41,51`, `acute_exposure_supplement.html:91,95` | Cordova 직접인용을 의역이라고 판정 | NCBI Bookshelf에 해당 문장 존재 | "의역 문제" 문단 삭제 또는 오판으로 정정 |
| 중간 | `results_interpretation_claude.html:333`, `results_interpretation_claude.html:272` | Raymond 2012를 전문 검증처럼 표시 | PubMed 초록/결론 수준 확인 | 검증 등급을 `초록/결론 검증`으로 낮춤 |
| 낮음 | `untrained_acute_metronome_evidence.md:49`, `acute_exposure_supplement.html:130` | PMC5832267 축자 아닌 문구에 따옴표 | 원문 문구는 `"practice conditions had little effect..."` | 따옴표 문구 교체 또는 의역 표시 |

## 메인 16편 재감사

| Ref | 출처 | 원문 앵커 | 로컬 주장과 대조 | 판정 |
|---|---|---|---|---|
| [1] Heiderscheit 2011, PMC3022995 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3022995/ | `"Running speed was self-selected"`; `"~20% and ~34% less energy"` | 속도 유지, braking impulse/impact transient/knee energy 감소 주장은 맞다. 본 연구 결과와는 주로 대조 근거다. | 정확 |
| [2] PMC8329321 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8329321/ | `"Cadence differences of 7.3%"`; `"peak force of 5.6%"` | MetroTimer, GPS pace monitor, cadence 증가와 peak force 감소가 확인된다. | 정확 |
| [3] PMC8772793 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8772793/ | `"2.8% decrease"`; `"8.6% decrease"` | +10% step rate에서 vGRF/braking 감소, rearfoot DF/eversion 감소 방향이 맞다. | 정확 |
| [4] PMC6203338 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6203338/ | `"did not find differences"`; `5.4/5.2/5.5 g` | cadence 증가만으로 peak tibial acceleration/loading rate가 줄지 않았다는 핵심 근거가 맞다. | 정확, 핵심 근거 |
| [5] Schubert 2014, PMC4000471 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4000471/ | `"more plantar flexed position"`; `"shock attenuation"` | stride rate 증가와 plantarflexed IC, GRF/shock 관련 요지가 맞다. | 정확 |
| [6] 2025 cadence review, PMC12440572 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12440572/ | `"5-10%"`; `"reduced vertical ground reaction forces"` | 5-10% cadence 증가의 loading 감소 및 낮은 cadence의 tibial injury 위험 언급이 맞다. | 정확 |
| [7] Farley 1996, PMID8849811 | https://pubmed.ncbi.nlm.nih.gov/8849811/ | `"2.3-fold"`; `7.0 to 16.3 kNm-1` | stride frequency 변화와 leg stiffness 증가 주장은 PubMed 초록과 일치한다. | 정확, 초록 근거 |
| [8] Kulmala 2018, PMC6269547 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6269547/ | `"10.7% and 12.3% greater"`; `"stiffer leg"` | maximalist shoe 연구라는 제한과 impact/loading 증가 수치가 맞다. | 정확 |
| [9] PMC3466237 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3466237/ | `"No effect of RAC"`; `"anti-persistent"` | RAC가 변동성 크기 SD를 키우지 않고 구조를 anti-persistent로 바꾼다는 주장이 맞다. | 정확 |
| [10] Hove et al., PMC3424126 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3424126/ | `"significantly lower"`; `"loss of functional adaptability"` | auditory cue에서 SIV 감소, anti-persistence, adaptability 해석이 원문과 맞다. | 정확 |
| [11] PMID22871238 | https://pubmed.ncbi.nlm.nih.gov/22871238/ | `"did not increase with either cue type"`; `1 step/min` | 건강 고령자에서 variability가 증가하지 않았고 cadence가 소폭 증가한 설명이 맞다. | 정확, 초록 근거 |
| [12] PMID35020171 | https://pubmed.ncbi.nlm.nih.gov/35020171/ | `"Twenty older adults"`; `"increased stride time variability"` | 낙상 이력 고령자 20명, stride time variability 증가 주장이 맞다. | 정확, 초록 근거 |
| [13] Chinn 2014, PMC4080591 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4080591/ | `"less dorsiflexed"`; `"more neutral"` | jogging에서 less dorsiflexed, more neutral ankle position 주장이 맞다. | 정확 |
| [14] Cordova 2000, NBK68419 | https://www.ncbi.nlm.nih.gov/books/NBK68419/ | `"taping offered the most support"`; `"Tape braces"` | 직접인용 문장이 실제 존재한다. 기존 false alarm이 틀렸다. | 정확 |
| [15] Raymond 2012, PMID22513304 | https://pubmed.ncbi.nlm.nih.gov/22513304/ | `"no effect on proprioceptive acuity"`; `MD 0.08°` | 내용은 정확하다. 단 초록/결론 검증으로 표기해야 한다. | 내용 정확, 검증등급 수정 |
| [16] Yong 2014, 로컬 PDF | `literature_pack/02_mechanistic_support/yong_2014_forefoot_rearfoot_emg.pdf` | ankle `p<0.001`; knee `p=0.023` | 각도/EMG/impact peak 요지는 맞지만 p-value 하나가 틀렸다. | 부분 오류 |

## 보충 5편 재감사

| 출처 | 원문 앵커 | 로컬 주장과 대조 | 판정 |
|---|---|---|---|
| PMC7450991 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7450991/ | `"10.2%"`; `"initial adaptation"` | 12주 cadence retraining 후 impact peak 감소와 적응 필요성 주장이 맞다. | 정확 |
| PMC1564141 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1564141/ | `"not a purely automatic task"` | treadmill walking의 attention 요구 설명이 맞다. | 정확 |
| PMC11233570 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11233570/ | `0.74 -> 0.39`; `"anti-persistence"` | older adults metronome walking의 alpha 감소와 attention 연결 설명이 맞다. | 정확, 대상 차이 명시 필요 |
| PMID33895635 | https://pubmed.ncbi.nlm.nih.gov/33895635/ | `"enhanced familiarity"`; `"stride-to-stride time variability"` | PD 음악 cue 친숙도와 variability 개선 주장은 맞다. 단 limited transfer로만 써야 한다. | 정확, 간접 근거 |
| PMC5832267 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5832267/ | `"little effect on learning and transfer performance"` | timing skill transfer에 대한 의미는 맞다. 따옴표 문구만 원문으로 교체해야 한다. | 의미 정확, 축자 수정 |

## A-to-B refined 보고서에 남은 legacy 인용

`analysis/2026-06-10/results_report_a_to_b_refined.html`에는 Claude 메인 16편 체계 밖의 legacy/reference set이 남아 있다. 존재 여부와 기본 요지는 확인되지만, 출판용으로는 `results_interpretation_claude.html`의 16편 체계를 기준으로 정리하는 것이 더 안전하다.

| 위치 | 인용 | 확인 결과 | 주의 |
|---|---|---|---|
| `results_report_a_to_b_refined.html:979` | Thaut 2007, DOI `10.1177/1545968307300523` | PubMed에서 velocity, stride length, cadence, symmetry 개선 확인 | stroke gait training 근거다. 건강 러닝 직접 근거 아님 |
| `results_report_a_to_b_refined.html:980` | Yu 2015, DOI `10.1589/jpts.27.485` | PubMed에서 90/100/110% RAC, stride length/cadence/gait speed 확인 | healthy young female walking 연구다. 러닝 직접 근거 아님 |
| `results_report_a_to_b_refined.html:1288` | Williams 2012, PMC3474309 | forefoot/barefoot, ankle power absorption, foot/ankle demand 확인 | PF angle만으로 push-off force를 증명하지는 못함 |
| `results_report_source_copy.html` 및 `literature_pack` | Thaut 1993, DOI `10.1177/136140969300700103` | SAGE 초록에서 stroke hemiparetic gait, gastrocnemius EMG, stride symmetry 확인 | running plantarflexion/push-off의 직접 근거로 쓰면 안 됨 |
| `results_report_a_to_b_refined.html:1262` | Repp & Su 2013, DOI `10.3758/s13423-012-0371-2` | PubMed/Springer 초록에서 SMS review와 external rhythm 설명 확인 | 보행/러닝 결과의 직접 근거가 아니라 배경 이론 |

## 최종 판정

- 기존 독립 감사 파일은 대체로 신뢰 가능하다.
- 새로 확인된 추가 중대 오류는 없다.
- 실제 수정해야 할 항목은 Yong p-value, Cordova false alarm, Raymond 검증등급, PMC5832267 축자 문구다.
- `results_report_a_to_b_refined.html`은 사실관계 자체보다 적용 범위가 넓다. 출판/제출용이면 Claude 메인 해석본의 16편 체계로 통합하고, legacy 인용은 배경/간접 근거로 낮춰야 한다.

