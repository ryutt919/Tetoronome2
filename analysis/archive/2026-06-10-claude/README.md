# 테토로놈 결과 해석 (Claude 작업본) — 2026-06-10

이 폴더는 `Research_object.md`의 가설로 수행한 N=6 실험 결과(`results/`)를 **해석하고, 원문 검증된 문헌으로 뒷받침**한 신규 작업본입니다.

## ⚠️ 정직성 헤드라인 (먼저 읽으세요)
- **메트로놈 가설 3개(충격↓·골반안정성↑·보폭일관성↑)는 모두 방향이 반대로** 나왔습니다.
- **테이핑 가설 3개(충격↓·PF↑·보폭일관성↑)는 모두 방향이 맞았습니다**(대부분 비유의).
- 통계적으로 유의한 결과는 **C→T+M 케이던스↑(p=.031)**, **T→T+M step CV↑(p=.031)** 둘뿐.
- 가설과 반대로 나온 두 메트로놈 결과는 **직접 지지 논문이 없고 지배적 문헌은 반대**입니다. → 억지 지지 대신 **대조(contrast)·가능성(possibility)**으로 정직하게 기술했습니다. 이는 잘못된 주장으로 인한 출판 리스크를 막기 위함입니다.

## 파일 구성 (읽는 순서 권장)
1. **[results_interpretation_claude.html](results_interpretation_claude.html)** — 메인 해석본. 가설별로 결과·검증 발췌·근거등급 배지·manuscript-safe 문장. 브라우저로 열기.
2. **[new_papers_core_results.md](new_papers_core_results.md)** — 핵심 결과(가설 반대) 2건의 증거 지형과 쓸 수 있는/없는 문장.
3. **[evidence_excerpts_verified.md](evidence_excerpts_verified.md)** — 인용 16편의 **원문 발췌 + 검증등급**(전문/초록). 모든 인용의 근거 추적용.
4. **[data_caveats.md](data_caveats.md)** — 해석 신뢰도에 영향을 주는 데이터 한계(속도 통제 불명, 수기 케이던스, roll SD 2명 견인, n=5/6, CV 절대값 한계).
5. **[verification_log.md](verification_log.md)** — fetch/read 로그(URL·날짜·성공/실패).
6. `*_source_copy.html` — 기존 main 리포트의 **읽기 전용 스냅샷**(참조용).

## 근거 등급 범례
| 배지 | 의미 |
|---|---|
| ✅ 지지 | 우리 결과 방향과 같고 변수가 가까움 |
| ⚠️ 대조 | 지배적 선행연구가 우리 결과와 반대 |
| 🔬 가능성 | 직접 측정 안 한 생체역학 가설 수준 |
| ❓ 정보 필요 | 우리 측정조건(특히 러닝 속도) 불명으로 보류 |

## 핵심 인용 요약 (전부 원문 검증)
- 케이던스↑ → GRF loading **감소**(대조): Heiderscheit 2011, PMC8329321, Schubert 2014, 리뷰 PMC12440572.
- 케이던스↑ → **경골/분절 가속도 비감소**(우리 결과와 정합, 핵심): **PMC6203338**.
- 메트로놈 → 변동성 크기 **미증가**, 구조만 anti-persistent(대조+기전): PMC3466237, PMC3424126, PubMed 22871238. 증가 보고는 낙상 고령자(Cronström 2022, limited transfer).
- 테이핑 → **dorsiflexion/ROM 제한**(지지): Chinn 2014, Cordova 2000. 고유수용성 향상은 **근거 없음**(Raymond 2012).
- PF↑ = ankle strategy(가능성): Schubert 2014, Yong 2014. (push-off 아님)

## 다음 단계로 권장
1. **러닝 속도 통제 여부**를 프로토콜에서 확정(충격 결과 해석의 최대 변수, data_caveats §1).
2. step interval 검출 품질(좌우 분리·결측률) 점검(CV 절대값 12–34% 한계, §5).
3. 표본 확대 시 핵심 결과(메트로놈 충격·CV) 재검증.

---
**무결성 보증:** 이 폴더 작업은 `analysis/results_report.html`, `analysis/pipeline_summary.html`, `analysis/2026-06-10/` 등 **기존 파일을 일절 수정하지 않았습니다.** 결과 수치는 `results/statistical_tests.csv`에서 인용했습니다.
