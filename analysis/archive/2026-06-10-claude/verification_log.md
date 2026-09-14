# 검증 로그 (Verification Log)

작성: 2026-06-10 · 작성자: Claude · 도구: WebFetch(원문→마크다운 변환 후 추출), WebSearch(탐색), Read(로컬 PDF).
목적: 본 폴더의 모든 인용이 **실제로 접근·확인된 원문**에 근거함을 추적 가능하게 남김.

## WebFetch — 원문 직접 확인
| # | 출처 | URL | 결과 |
|---|---|---|---|
| 1 | Heiderscheit 2011 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3022995/ | ✅ 전문. 속도고정, step rate↑→loading↓ 수치 확보 |
| 2 | 야외 cadence/peak force | https://pmc.ncbi.nlm.nih.gov/articles/PMC8329321/ | ✅ 전문. 메트로놈 +7.3%, peak force −5.6% |
| 3 | step rate/rearfoot/GRF | https://pmc.ncbi.nlm.nih.gov/articles/PMC8772793/ | ✅ 전문(리다이렉트 후). vGRF −2.8% |
| 4 | 경골가속도·케이던스 (핵심) | https://pmc.ncbi.nlm.nih.gov/articles/PMC6203338/ | ✅ 전문. 케이던스↑로 경골가속도 5.5 vs 5.4g(n.s.) |
| 5 | Schubert 2014 리뷰 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4000471/ | ✅ 전문. "more plantar flexed position at initial contact" |
| 6 | cadence 리뷰 2025 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12440572/ | ✅ 전문. 5–10%↑ → loading↓ consistent |
| 7 | Farley & González 1996 | https://pubmed.ncbi.nlm.nih.gov/8849811/ | ✅ 초록. leg stiffness 2.3배↑ |
| 8 | Kulmala 2018 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6269547/ | ✅ 전문. impact peak +10.7%, loading rate +12.3% |
| 9 | RAC step-to-step 변동성 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3466237/ | ✅ 전문(리다이렉트 후). "No effect of RAC on fluctuation magnitude (SD)"; anti-persistent |
| 10 | 리듬 cue 시간역학 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3424126/ | ✅ 전문. SIV "significantly lower"; persistence→anti-persistence |
| 11 | music vs metronome 고령자 | https://pubmed.ncbi.nlm.nih.gov/22871238/ | ✅ 초록. "did not increase with either cue type" |
| 12 | Cronström 2022 | https://pubmed.ncbi.nlm.nih.gov/35020171/ | ✅ 초록. 낙상 고령자 20명; "increase stride time variability" |
| 13 | Chinn 2014 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4080591/ | ✅ 전문. jogging "less dorsiflexed", "more neutral" |
| 14 | Cordova 2000 | https://www.ncbi.nlm.nih.gov/books/NBK68419/ | ✅ 구조화 요약. "limiting dorsiflexion ROM" |
| 15 | Raymond 2012 | https://pubmed.ncbi.nlm.nih.gov/22513304/ | ✅ 결론. "no effect on proprioceptive acuity" (MD 0.08°) |

## Read — 로컬 PDF 직접 확인
| # | 출처 | 경로 | 결과 |
|---|---|---|---|
| 16 | Yong 2014 | `literature_pack/02_mechanistic_support/yong_2014_forefoot_rearfoot_emg.pdf` (p.1-3) | ✅ 전문. FFS 11±5° PF vs RFS 6±4° DF (p=0.023) |

## WebSearch — 탐색용(인용 아님)
- "increased step rate cadence running tibial acceleration impact loading metronome" → PMC6203338, PMC8329321, PMC8772793, PMC12440572 발견.
- "metronome rhythmic auditory cueing increases stride time variability healthy adults" → PMC3466237, PMC3424126, PubMed 22871238 발견.
- "Kulmala 2018 ... PMC full text" → PMC6269547 확인.

## ⛔ 접근 실패 → 인용하지 않음 (정직성 기록)
| 출처 | 시도 URL | 결과 | 처리 |
|---|---|---|---|
| Kulmala 2018 (Nature) | https://www.nature.com/articles/s41598-018-35980-6 | 인증 리다이렉트(idp.nature.com) | PMC6269547로 대체 검증 |
| Hausdorff 2005 | PMC1226196 (오ID), BMC→Springer | 잘못된 문서 / Springer 인증 게이트 | **수치 인용 보류.** data_caveats §5에서 "미재검증"으로 명시, 사실 주장 안 함 |

## 미채택(이번 본문 핵심 인용 제외)
- Williams 2012, Hamner 2010, Thaut 1993, Terrier&Deriaz 2012(PLoS 별도), Repp&Su 2013: 배경/중복으로 제외. 필요 시 별도 검증 후 추가.

> 규칙: 위 ✅ 항목만 본문에서 사실로 인용. ⛔ 항목은 사실 주장에 사용하지 않음.
