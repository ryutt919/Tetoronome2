# 독립 인용 감사 보고서 - 2026-06-12

대상 폴더: `analysis/2026-06-10-claude/`

검토 방법:
- `results_interpretation_claude.html`, `evidence_excerpts_verified.md`, `citation_factcheck_session.md`, `verification_log.md`, `acute_exposure_supplement.html`, `untrained_acute_metronome_evidence.md`의 인용과 주장 추출
- PMC/NCBI Bookshelf printable page, PubMed EFetch XML, 로컬 PDF(`literature_pack/02_mechanistic_support/yong_2014_forefoot_rearfoot_emg.pdf`)를 직접 조회
- 직접 인용문은 원문 문구와 축자 비교, 숫자와 p-value는 원문 표/문단과 비교

## 총평

현재 Claude 메인 해석본의 문헌 지형은 대체로 타당하다. 핵심 결론인 "메트로놈 결과는 지배적 문헌과 반대이므로 대조/가능성으로 써야 한다", "테이핑은 dorsiflexion/ROM 제한 쪽 문헌과 정합한다", "PF 증가는 push-off가 아니라 ankle strategy로 제한해야 한다"는 방향은 유지 가능하다.

다만 기존 `citation_factcheck_session.md`의 총평은 그대로 믿으면 안 된다. 그 문서는 [14] Cordova를 유일한 흠으로 봤지만, 실제로는 반대다. [14]는 원문 문장이 존재하고, [16] Yong의 p-value 인용이 틀렸다.

## 즉시 수정 권장

| 심각도 | 위치 | 현재 내용 | 원문 확인 | 판정/수정 |
|---|---|---|---|---|
| 높음 | `results_interpretation_claude.html:237`, `evidence_excerpts_verified.md:116`, `citation_factcheck_session.md:43`, `verification_log.md:28` | Yong 2014의 ankle angle 차이를 `p=0.023`으로 인용 | 로컬 PDF p.3595: ankle angle은 FFS 11±5° PF vs RFS 6±4° DF이고 `p<0.001`; `p=0.023`은 knee flexion angle 문장에 붙어 있음 | ankle angle p-value를 `p<0.001`로 수정. `p=0.023`은 무릎 굴곡 차이에만 사용 |
| 중간 | `citation_factcheck_session.md:6,41,51,52,61`, `acute_exposure_supplement.html:91,95` | [14] Cordova quote가 의역이므로 인용형식 수정 필요 | NCBI Bookshelf NBK68419에 "taping offered the most support for limiting dorsiflexion ROM" 문장이 실제 존재 | 기존 fact-check의 [14] 문제 제기는 오판. [14]는 직접인용으로 유지 가능 |
| 중간 | `results_interpretation_claude.html:333`, `results_interpretation_claude.html:272` | Raymond 2012를 "전문 검증"으로 표시 | PubMed abstract에서 핵심 결론과 MD 0.08° 확인. 전문을 별도로 읽은 증거는 없음 | 등급을 "초록/결론 검증"으로 낮추는 것이 정직함 |
| 낮음 | `untrained_acute_metronome_evidence.md:49`, `acute_exposure_supplement.html:130` | PMC5832267을 "minimal impact on timing skill transfer"로 따옴표 처리 | 원문은 "practice conditions had little effect on learning and transfer performance of timing skill" | 의미는 유사하지만 축자 인용 아님. 따옴표 문구를 원문으로 교체하거나 의역 표시 |

## 메인 16편 감사 결과

| Ref | 출처 | 로컬 주장 | 원문 직접 확인 | 판정 |
|---|---|---|---|---|
| [1] Heiderscheit 2011, PMC3022995 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3022995/ | step rate 증가 시 braking impulse, impact transient, knee energy absorption 감소. 속도 유지 | 원문: "Running speed was self-selected..." 및 impact transient 감소, knee energy 약 20/34% 감소 문단 확인 | 정확. 단 본 연구 결과에는 지지보다 대조 근거 |
| [2] PMC8329321 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8329321/ | MetroTimer, cadence +7.3%, peak force -5.6%, GPS pace monitor | 원문에 MetroTimer, "Cadence differences of 7.3%" 및 peak force -5.6% 확인 | 정확 |
| [3] PMC8772793 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8772793/ | +10% step rate에서 vGRF 약 -2.8%, braking -8.6%, rearfoot DF/eversion 감소 | 원문 표에서 DF 25.85→24.27, eversion 8.97→8.18, 문단에서 2.8%/8.6% 확인 | 정확 |
| [4] PMC6203338 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6203338/ | cadence 증가만으로 peak tibial acceleration/loading rate가 감소하지 않음 | 원문: peak tibial acceleration 5.4/5.2/5.5g, cadence loading rate 후족과 비유의 확인 | 정확. shank IMU 해석의 핵심 근거 |
| [5] Schubert 2014, PMC4000471 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4000471/ | stride rate 증가와 더 plantarflexed initial contact, GRF/shock attenuation 감소 | 원문: "more plantar flexed position..." 및 GRF/shock attenuation 감소 확인 | 정확 |
| [6] 2025 cadence review, PMC12440572 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12440572/ | 5-10% cadence 증가가 vGRF/loading rate 감소와 정합, 낮은 cadence의 tibial injury 위험 | 원문 abstract/table에서 5-10%, reduced vGRF/loading rates, <=166 vs >=178 spm 6-7배 문구 확인 | 정확. review 근거로 사용 |
| [7] Farley 1996, PMID 8849811 | https://pubmed.ncbi.nlm.nih.gov/8849811/ | stride frequency 변화 시 leg stiffness 2.3배 증가 | PubMed abstract에서 7.0→16.3 kNm-1, 2.3-fold 확인 | 정확. 초록 근거 |
| [8] Kulmala 2018, PMC6269547 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6269547/ | maximalist shoe에서 impact peak/loading rate +10.7/+12.3%, stiffer leg | 원문에서 해당 수치와 stiffer leg 설명 확인 | 정확. cadence 연구가 아니라 신발 연구로 제한한 것도 맞음 |
| [9] PMC3466237 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3466237/ | RAC는 fluctuation magnitude(SD)를 키우지 않고 anti-persistent 구조 유발 | 원문: "No effect of RAC..." 및 anti-persistent 관련 문단 확인 | 정확 |
| [10] Hove et al., PMC3424126 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3424126/ | auditory cue에서 SIV lower, persistence to anti-persistence, unnatural rhythm/loss of adaptability | 원문에서 "significantly lower", "anti-persistence", "loss of functional adaptability" 확인 | 정확 |
| [11] PMID 22871238 | https://pubmed.ncbi.nlm.nih.gov/22871238/ | healthy older adults에서 variability did not increase, cadence +1 step/min | PubMed abstract에서 해당 문구 확인 | 정확. 초록 근거 |
| [12] PMID 35020171 | https://pubmed.ncbi.nlm.nih.gov/35020171/ | 낙상 이력 고령자 20명에서 stride time variability 증가, limited transfer | PubMed abstract에서 20명, 71±4.9세, increased stride time variability 확인 | 정확. full text PMC도 존재하지만 초록만으로도 핵심 확인 가능 |
| [13] Chinn 2014, PMC4080591 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4080591/ | taping 후 jogging에서 less dorsiflexed, more neutral ankle position | 원문에서 12%-21%, MD 4.91°, more neutral 확인 | 정확 |
| [14] Cordova 2000, NBK68419 | https://www.ncbi.nlm.nih.gov/books/NBK68419/ | taping offered most support for limiting dorsiflexion ROM | NCBI Bookshelf에 같은 문장 존재. Tape braces vs lace-up braces 수치도 확인 | 정확. 기존 fact-check의 "의역" 판정은 틀림 |
| [15] Raymond 2012, PMID 22513304 | https://pubmed.ncbi.nlm.nih.gov/22513304/ | tape/brace가 proprioceptive acuity에 유의한 효과 없음, MD 0.08° | PubMed abstract에서 no significant effect, MD 0.08°, CI -0.39 to 0.55 확인 | 내용 정확. 검증등급은 "초록/결론"으로 낮춰야 함 |
| [16] Yong 2014, 로컬 PDF | `literature_pack/02_mechanistic_support/yong_2014_forefoot_rearfoot_emg.pdf` | FFS 11±5° PF vs RFS 6±4° DF, gastroc↑, TA↓, FFS impact peak↓ | 각도/EMG/impact peak는 확인. 단 p-value는 ankle angle `p<0.001`, knee flexion `p=0.023` | 부분 오류. p-value 수정 필요 |

## 보충본 추가 인용 감사

| 출처 | 로컬 주장 | 원문 확인 | 판정 |
|---|---|---|---|
| PMC7450991 | 12주 cadence retraining 후 impact peak -10.2%, musculoskeletal adaptation 필요 | 원문에서 impact peak -10.2% 및 "initial adaptation..." 확인 | 정확 |
| PMC1564141 | treadmill walking은 "not a purely automatic task" | 원문 결론에서 확인 | 정확 |
| PMC11233570 | older adults metronome walking에서 alpha 0.74→0.39, anti-persistence와 attention 관련 | 원문 표와 discussion에서 확인 | 정확. 대상/동작 차이로 limited transfer 표기는 적절 |
| PMID 33895635 / S096663622100151X | PD에서 familiarity가 stride amplitude/variability 개선과 관련 | PubMed abstract에서 enhanced familiarity가 stride amplitude/variability 개선 및 reduced stride-to-stride time variability를 보였음을 확인 | 정확. limited transfer 유지 |
| PMC5832267 | timing skill transfer에 practice condition 영향이 작음 | 원문은 "little effect on learning and transfer performance of timing skill" | 의미는 정확. 직접인용 문구만 수정 필요 |

## 분석 상태 판단

1. `results_interpretation_claude.html`은 이전 `results_report_source_copy.html`보다 훨씬 안전한 작업본이다. 반대 방향 결과를 억지 지지로 만들지 않고 contrast/possibility로 낮춘 점이 타당하다.
2. 결과 수치 자체는 `results/statistical_tests.csv`와 맞는다. 예: C→M peak g +7.51%, C→M step CV +5.09%, C→T+M cadence +4.25% p=.0312, T→T+M step CV +16.41% p=.0312.
3. 핵심 리스크는 문헌 조작이 아니라 검증 문서의 세부 품질이다. [16] p-value 오류와 [14] false alarm을 고치면 문헌 감사 신뢰도가 올라간다.
4. `results_report_source_copy.html` 및 IDE 활성 파일 `analysis/2026-06-10/results_report_a_to_b_refined.html`에는 Thaut, Yu, Repp, Williams, Hamner 등 legacy/reference set이 남아 있다. Claude 메인 작업본은 이들을 대부분 핵심 인용에서 제외했으므로, 출판/보고에는 `results_interpretation_claude.html` 쪽의 16편 체계를 기준으로 삼는 것이 안전하다.

## 권장 수정 문구

Yong 2014:

> FFS runners contacted the ground with a more plantarflexed ankle than RFS runners (11±5° PF vs 6±4° DF, p<0.001). Knee flexion at foot contact was also greater in FFS runners (p=0.023). FFS runners showed lower tibialis anterior and higher gastrocnemius activity during terminal swing, and reduced impact peak compared with RFS runners.

Cordova 2000:

> 기존처럼 직접인용 유지 가능. `citation_factcheck_session.md`와 `acute_exposure_supplement.html`의 "[14] 의역 문제" 문단은 삭제하거나 "오판"으로 정정.

Raymond 2012:

> `전문 검증`이 아니라 `초록/결론 검증`으로 표기. 내용 자체는 정확하다.

PMC5832267:

> 따옴표 안 문구는 "practice conditions had little effect on learning and transfer performance of timing skill"로 교체.
