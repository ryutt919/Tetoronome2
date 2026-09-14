"""
Tetoronom Analysis Runner
==========================
전체 분석 파이프라인 실행 스크립트.
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(__file__))
from pipeline import run_all_analyses, run_statistical_tests, build_subject_table
from visualize import run_all_visualizations

BASE_DIR    = os.path.join(os.path.dirname(__file__), '..')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
FIGS_DIR    = os.path.join(RESULTS_DIR, 'figures')

def main():
    print('=' * 60)
    print('  Tetoronom Data Analysis Pipeline')
    print('  메트로놈 & 테이핑 intervention 효과 분석')
    print('=' * 60)

    # ── Step 1: 지표 계산
    print('\n[Step 1] 모든 피험자-조건 지표 계산...')
    results_df = run_all_analyses()
    os.makedirs(RESULTS_DIR, exist_ok=True)
    results_df.to_csv(
        os.path.join(RESULTS_DIR, 'metrics_by_condition.csv'),
        index=False, encoding='utf-8-sig')
    print(f'  → {RESULTS_DIR}/metrics_by_condition.csv')

    # ── Step 2: 통계 검정
    print('\n[Step 2] 통계 검정 수행...')
    stats_df = run_statistical_tests(results_df)
    stats_df.to_csv(
        os.path.join(RESULTS_DIR, 'statistical_tests.csv'),
        index=False, encoding='utf-8-sig')
    print(f'  → {RESULTS_DIR}/statistical_tests.csv')

    tbl = build_subject_table(results_df)
    tbl.to_csv(
        os.path.join(RESULTS_DIR, 'subject_condition_table.csv'),
        index=False, encoding='utf-8-sig')
    print(f'  → {RESULTS_DIR}/subject_condition_table.csv')

    # ── Step 3: 시각화
    print('\n[Step 3] 시각화 생성...')
    run_all_visualizations(results_df, stats_df, FIGS_DIR)

    # ── Step 4: 핵심 결과 요약 출력
    print('\n' + '=' * 60)
    print('  핵심 결과 요약')
    print('=' * 60)

    summaries = [
        ('케이던스 (steps/min)',       'cadence_steps_per_min'),
        ('Shank 착지 충격량 (peak g)', 'shank_mean_peak_g'),
        ('Shank 충격량 (Resultant RMS)', 'shank_resultant_rms_m_s2'),
        ('Step CV% (일관성)',          'step_interval_cv_pct'),
        ('골반 Pitch SD (수직 안정성)', 'pelvis_pitch_sd_deg'),
        ('Ankle DF/PF ROM (°)',        'ankle_dp_pf_rom_deg'),
        ('Ankle Mean Dorsiflexion (°)', 'ankle_mean_dorsiflexion_peak_deg'),
        ('Ankle Mean Plantarflexion (°)', 'ankle_mean_plantarflexion_peak_deg'),
    ]

    for label, col in summaries:
        if col not in results_df.columns:
            continue
        pivot = results_df.pivot_table(
            col, 'subject', 'condition_label', aggfunc='first')
        print(f'\n  ▶ {label}')
        print(pivot.round(2).to_string())

    # 통계 요약
    print('\n  ▶ 통계 검정 요약 (p < 0.05 = *):')
    cols = ['comparison', 'metric', 'mean_diff', 'pct_change', 'effect_size_d', 'p_value', 'sig']
    cols_exist = [c for c in cols if c in stats_df.columns]
    print(stats_df[cols_exist].to_string(index=False))

    print('\n' + '=' * 60)
    print('  완료! 결과 파일:')
    print(f'    {RESULTS_DIR}/')
    print(f'    {FIGS_DIR}/')
    print('=' * 60)


if __name__ == '__main__':
    main()
