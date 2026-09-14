"""
Tetoronom Visualization Module
================================
분석 결과를 시각화합니다. (흰색 배경, 한글 지원)

생성 플롯:
  1. 메트로놈 효과 대시보드
  2. 메트로놈 보폭 일관성
  3. 테이핑 효과 대시보드
  4. 발/무릎/골반별 충격량 비교
  5. 전체 조건 overview
  6. 피험자별 개인 프로파일
  7. 통계 검정 히트맵
"""

import os
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
from matplotlib.gridspec import GridSpec
import warnings

warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# 한글 폰트 설정 (macOS: AppleGothic / Apple SD Gothic Neo)
# ─────────────────────────────────────────────


def _setup_korean_font():
    """macOS에서 사용 가능한 한글 폰트를 찾아 설정합니다."""
    candidates = [
        "Apple SD Gothic Neo",
        "AppleGothic",
        "Nanum Gothic",
        "NanumGothic",
        "Malgun Gothic",
    ]
    available = {f.name for f in fm.fontManager.ttflist}
    for name in candidates:
        if name in available:
            matplotlib.rcParams["font.family"] = name
            matplotlib.rcParams["axes.unicode_minus"] = False
            return name
    # 직접 경로 시도
    direct_paths = [
        "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    ]
    for path in direct_paths:
        if os.path.exists(path):
            try:
                prop = fm.FontProperties(fname=path)
                matplotlib.rcParams["font.family"] = prop.get_name()
                matplotlib.rcParams["axes.unicode_minus"] = False
                return prop.get_name()
            except Exception:
                pass
    return "DejaVu Sans"  # fallback (한글 깨질 수 있음)


KOREAN_FONT = _setup_korean_font()

# ─────────────────────────────────────────────
# STYLE CONFIG (흰색 배경)
# ─────────────────────────────────────────────

CONDITION_COLORS = {
    "Control": "#2E86AB",
    "Metro": "#E84855",
    "Tape": "#3BB273",
    "Tape+Metro": "#7B2FBE",
}

CONDITION_ORDER = ["Control", "Metro", "Tape", "Tape+Metro"]

SUBJECTS_KO = {
    "P01": "P01",
    "P02": "P02",
    "P03": "P03",
    "P04": "P04",
    "P05": "P05",
    "P06": "P06",
}

plt.rcParams.update(
    {
        "figure.facecolor": "white",
        "axes.facecolor": "#F8F9FA",
        "axes.edgecolor": "#CCCCCC",
        "axes.labelcolor": "#333333",
        "axes.titlecolor": "#111111",
        "xtick.color": "#555555",
        "ytick.color": "#555555",
        "text.color": "#333333",
        "grid.color": "#DDDDDD",
        "grid.linestyle": "--",
        "grid.alpha": 0.7,
        "font.size": 10,
        "legend.facecolor": "white",
        "legend.edgecolor": "#CCCCCC",
        "figure.dpi": 150,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.unicode_minus": False,
    }
)

# 한글 폰트 재적용 (rcParams 업데이트 후)
matplotlib.rcParams["font.family"] = KOREAN_FONT
matplotlib.rcParams["axes.unicode_minus"] = False


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────


def _bar_group(ax, results_df, metric, title, ylabel, conditions=None, note=None):
    """그룹 바 차트 그리기."""
    if conditions is None:
        conditions = CONDITION_ORDER

    subjects = sorted(results_df["subject"].unique())
    n_s = len(subjects)
    n_c = len(conditions)
    x = np.arange(n_s)
    width = 0.75 / n_c

    ymax = 0.0
    for i, cond in enumerate(conditions):
        vals = []
        for subj in subjects:
            row = results_df[(results_df["subject"] == subj) & (results_df["condition_label"] == cond)]
            val = row[metric].values[0] if len(row) > 0 and not pd.isna(row[metric].values[0]) else np.nan
            vals.append(val)
        offset = (i - n_c / 2 + 0.5) * width
        bars = ax.bar(
            x + offset,
            vals,
            width=width * 0.88,
            color=CONDITION_COLORS.get(cond, "#888888"),
            alpha=0.85,
            label=cond,
            edgecolor="white",
            linewidth=0.8,
        )
        valid_vals = [v for v in vals if not (isinstance(v, float) and np.isnan(v))]
        if valid_vals:
            ymax = max(ymax, max(valid_vals))

    # y limit with headroom
    ax.set_ylim(0, ymax * 1.22 if ymax > 0 else 1)

    # 값 레이블 다시 그리기
    for i, cond in enumerate(conditions):
        vals = []
        for subj in subjects:
            row = results_df[(results_df["subject"] == subj) & (results_df["condition_label"] == cond)]
            val = row[metric].values[0] if len(row) > 0 and not pd.isna(row[metric].values[0]) else np.nan
            vals.append(val)
        offset = (i - n_c / 2 + 0.5) * width
        for j, val in enumerate(vals):
            if not np.isnan(val):
                ax.text(
                    x[j] + offset,
                    val + ymax * 0.02,
                    f"{val:.1f}",
                    ha="center",
                    va="bottom",
                    fontsize=6.5,
                    color="#333333",
                    fontproperties=fm.FontProperties(family=KOREAN_FONT),
                )

    ax.set_xticks(x)
    ax.set_xticklabels(
        [SUBJECTS_KO.get(s, s) for s in subjects],
        fontsize=9,
        fontproperties=fm.FontProperties(family=KOREAN_FONT),
    )
    ax.set_title(
        title,
        fontsize=10,
        fontweight="bold",
        pad=6,
        fontproperties=fm.FontProperties(family=KOREAN_FONT),
    )
    ax.set_ylabel(
        ylabel,
        fontsize=8,
        fontproperties=fm.FontProperties(family=KOREAN_FONT),
    )
    ax.legend(fontsize=7, loc="upper right", prop=fm.FontProperties(family=KOREAN_FONT, size=7))
    ax.grid(axis="y", alpha=0.5)


def _save(fig, path):
    fig.savefig(path, bbox_inches="tight", facecolor="white", dpi=150)
    plt.close(fig)
    print(f"  → {path}")


def plot_peak_detection_example(out_dir, subject="P04", condition="control", segment="shank", start_sec=0.0, duration_sec=20.0):
    """피크 검출 예시 (raw/smoothed/threshold/peaks)."""
    from pipeline import (
        load_subject_condition,
        split_by_segment,
        _detect_impact_peaks_with_meta,
        FS,
        GRAVITY,
        CONDITION_LABELS,
    )

    df = load_subject_condition(subject, condition)
    if df is None:
        print(f"  → peak 예시 스킵 (데이터 없음): {subject} / {condition}")
        return

    segs = split_by_segment(df)
    seg_df = segs.get(segment, pd.DataFrame())
    if len(seg_df) == 0:
        print(f"  → peak 예시 스킵 (segment 없음): {segment}")
        return

    resultant = seg_df["shank_free_acceleration_resultant_m_s2"].values
    # Disable smoothing for peak detection example to show raw-peak behavior
    meta = _detect_impact_peaks_with_meta(resultant, use_smoothing=False)
    peaks = meta["peaks"]
    smoothed = meta["smoothed"]

    start_idx = int(start_sec * FS)
    end_idx = int((start_sec + duration_sec) * FS)
    end_idx = min(len(resultant), end_idx)
    if end_idx <= start_idx + 1:
        print("  → peak 예시 스킵 (구간 길이 부족)")
        return

    t = (np.arange(start_idx, end_idx) / FS) - start_sec
    raw_win = resultant[start_idx:end_idx]
    smooth_win = smoothed[start_idx:end_idx]

    window_peaks = peaks[(peaks >= start_idx) & (peaks < end_idx)]
    peak_times = (window_peaks / FS) - start_sec
    peak_vals = smoothed[window_peaks] if len(window_peaks) > 0 else np.array([])

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(t, raw_win, color="#95A5A6", linewidth=1.0, alpha=0.6, label="Raw")
    ax.plot(t, smooth_win, color="#2980B9", linewidth=1.4, label="Processed (no smoothing)")
    if len(window_peaks) > 0:
        ax.scatter(peak_times, peak_vals, color="#E74C3C", s=30, label="Detected Peaks")

    cond_label = CONDITION_LABELS.get(condition, condition)
    title = f"피크 검출 예시: {subject} / {cond_label} / {segment} (0-{duration_sec:.0f}s)"
    ax.set_title(
        title,
        fontsize=12,
        fontweight="bold",
        fontproperties=fm.FontProperties(family=KOREAN_FONT, size=12),
    )
    ax.set_xlabel("Time (s)", fontsize=9, fontproperties=fm.FontProperties(family=KOREAN_FONT))
    ax.set_ylabel("Resultant Acc (m/s^2)", fontsize=9, fontproperties=fm.FontProperties(family=KOREAN_FONT))
    ax.legend(fontsize=8, loc="upper right", prop=fm.FontProperties(family=KOREAN_FONT, size=8))
    ax.grid(alpha=0.5)

    subject_code = SUBJECTS_KO.get(subject, subject)
    fname = f"peak_detection_{subject_code}_{condition}_{segment}_{int(duration_sec)}s.png"
    _save(fig, os.path.join(out_dir, fname))


# ─────────────────────────────────────────────
# PLOT 1: 메트로놈 효과
# ─────────────────────────────────────────────


def plot_metronome_effects(results_df, out_dir):
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle(
        "메트로놈 Intervention 효과 분석\n(Control vs Metro vs Tape+Metro)",
        fontsize=14,
        fontweight="bold",
        y=0.98,
        fontproperties=fm.FontProperties(family=KOREAN_FONT, size=14),
    )
    gs = GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.35)
    conds = ["Control", "Metro", "Tape+Metro"]

    ax1 = fig.add_subplot(gs[0, 0])
    _bar_group(ax1, results_df, "cadence_steps_per_min", "케이던스", "steps/min", conds)

    ax2 = fig.add_subplot(gs[0, 1])
    _bar_group(ax2, results_df, "shank_mean_peak_g", "착지 충격 (Shank Peak g)", "g", conds)

    ax3 = fig.add_subplot(gs[1, 0])
    _bar_group(ax3, results_df, "pelvis_pitch_sd_deg", "골반 수직 안정성 (Pitch SD)", "°", conds)

    ax4 = fig.add_subplot(gs[1, 1])
    _bar_group(ax4, results_df, "pelvis_roll_sd_deg", "골반 좌우 안정성 (Roll SD)", "°", conds)

    _save(fig, os.path.join(out_dir, "plot_metronome_effects.png"))


# ─────────────────────────────────────────────
# PLOT 2: 메트로놈 보폭 일관성
# ─────────────────────────────────────────────


def plot_metronome_variability(results_df, out_dir):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(
        "메트로놈 효과: 보폭 일관성 (Ground Contact Variability)",
        fontsize=12,
        fontweight="bold",
        fontproperties=fm.FontProperties(family=KOREAN_FONT, size=12),
    )
    conds = ["Control", "Metro", "Tape+Metro"]
    _bar_group(ax1, results_df, "step_interval_cv_pct", "Step Interval CV (%)\n낮을수록 일관성 높음", "CV (%)", conds)
    _bar_group(ax2, results_df, "step_interval_sd_s", "Step Interval SD\n낮을수록 일관성 높음", "SD (s)", conds)
    _save(fig, os.path.join(out_dir, "plot_metronome_variability.png"))


# ─────────────────────────────────────────────
# PLOT 3: 테이핑 효과
# ─────────────────────────────────────────────


def plot_taping_effects(results_df, out_dir):
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle(
        "테이핑 Intervention 효과 분석\n(Control vs Tape vs Tape+Metro)",
        fontsize=14,
        fontweight="bold",
        y=0.98,
        fontproperties=fm.FontProperties(family=KOREAN_FONT, size=14),
    )
    gs = GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.35)
    conds = ["Control", "Tape", "Tape+Metro"]

    ax1 = fig.add_subplot(gs[0, 0])
    _bar_group(ax1, results_df, "shank_mean_peak_g", "착지 충격 (Shank Peak g)", "g", conds)

    ax2 = fig.add_subplot(gs[0, 1])
    _bar_group(ax2, results_df, "ankle_dp_pf_rom_deg", "Ankle DF/PF ROM", "°", conds)

    ax3 = fig.add_subplot(gs[1, 0])
    _bar_group(ax3, results_df, "cadence_steps_per_min", "케이던스", "steps/min", conds)

    ax4 = fig.add_subplot(gs[1, 1])
    _bar_group(ax4, results_df, "step_interval_cv_pct", "Ground Contact Variability (CV%)", "CV (%)", conds)

    _save(fig, os.path.join(out_dir, "plot_taping_effects.png"))


# ─────────────────────────────────────────────
# PLOT 4: 발/무릎/골반별 충격량 비교 (제거됨 - Shank만 분석하므로 생략)
# ─────────────────────────────────────────────


# ─────────────────────────────────────────────
# PLOT 5: 전체 overview
# ─────────────────────────────────────────────


def plot_all_conditions_overview(results_df, out_dir):
    fig = plt.figure(figsize=(18, 14))
    fig.suptitle(
        "전체 조건 비교 — 주요 지표",
        fontsize=15,
        fontweight="bold",
        y=0.99,
        fontproperties=fm.FontProperties(family=KOREAN_FONT, size=15),
    )
    gs = GridSpec(3, 3, figure=fig, hspace=0.55, wspace=0.40)

    metrics_cfg = [
        ("cadence_steps_per_min", "케이던스", "steps/min"),
        ("shank_mean_peak_g", "착지 충격 Peak g\n(Shank)", "g"),
        ("shank_resultant_rms_m_s2", "Shank Resultant RMS", "m/s²"),
        ("step_interval_cv_pct", "Step CV%\n(보폭 일관성)", "CV (%)"),
        ("pelvis_pitch_sd_deg", "골반 수직 안정성\n(Pitch SD)", "°"),
        ("pelvis_roll_sd_deg", "골반 좌우 안정성\n(Roll SD)", "°"),
        ("ankle_mean_dorsiflexion_peak_deg", "Ankle 평균 Dorsiflexion", "°"),
        ("ankle_dp_pf_rom_deg", "Ankle DF/PF ROM", "°"),
        ("ankle_mean_plantarflexion_peak_deg", "Ankle 평균 Plantarflexion", "°"),
    ]

    for idx, (metric, title, ylabel) in enumerate(metrics_cfg):
        r, c = divmod(idx, 3)
        ax = fig.add_subplot(gs[r, c])
        if metric in results_df.columns:
            _bar_group(ax, results_df, metric, title, ylabel, CONDITION_ORDER)
        else:
            ax.text(0.5, 0.5, "N/A", ha="center", va="center", transform=ax.transAxes)
            ax.set_title(title, fontproperties=fm.FontProperties(family=KOREAN_FONT))

    patches = [mpatches.Patch(color=CONDITION_COLORS[l], label=l) for l in CONDITION_ORDER]
    fig.legend(
        handles=patches, loc="lower center", ncol=4, fontsize=10, bbox_to_anchor=(0.5, -0.02), prop=fm.FontProperties(family=KOREAN_FONT, size=10)
    )

    _save(fig, os.path.join(out_dir, "plot_all_conditions_overview.png"))


# ─────────────────────────────────────────────
# PLOT 6: 피험자별 프로파일
# ─────────────────────────────────────────────


def plot_individual_profiles(results_df, out_dir):
    metrics = [
        ("cadence_steps_per_min", "케이던스 (steps/min)"),
        ("shank_mean_peak_g", "Peak g (Shank) - 평균"),
        ("shank_median_peak_g", "Peak g (Shank) - 중앙값"),
        ("step_interval_cv_pct", "Step CV%"),
        ("pelvis_pitch_sd_deg", "골반 수직 안정성 (Pitch SD)"),
        ("pelvis_roll_sd_deg", "골반 측면 안정성 (Roll SD)"),
        ("ankle_dp_pf_rom_deg", "Ankle DF/PF ROM (°) - 평균 피크차"),
        ("ankle_median_dp_pf_rom_deg", "Ankle DF/PF ROM (°) - 중앙 피크차"),
        ("ankle_mean_dorsiflexion_peak_deg", "Ankle Dorsiflexion (°) - 평균"),
        ("ankle_median_dorsiflexion_peak_deg", "Ankle Dorsiflexion (°) - 중앙값"),
        ("ankle_mean_plantarflexion_peak_deg", "Ankle Plantarflexion (°) - 평균"),
        ("ankle_median_plantarflexion_peak_deg", "Ankle Plantarflexion (°) - 중앙값"),
    ]

    custom_order = ["Control", "Tape", "Metro", "Tape+Metro"]
    cond_x = {l: i for i, l in enumerate(custom_order)}
    
    unique_subjs = sorted(results_df["subject"].unique())
    color_palette = ["#E67E22", "#1ABC9C", "#C0392B", "#9B59B6", "#3498DB", "#34495E", "#F1C40F"]
    marker_palette = ["o", "s", "^", "D", "v", "P", "X"]
    
    colors = {subj: color_palette[i % len(color_palette)] for i, subj in enumerate(unique_subjs)}
    markers = {subj: marker_palette[i % len(marker_palette)] for i, subj in enumerate(unique_subjs)}

    for metric, title in metrics:
        if metric not in results_df.columns:
            continue
            
        fig, ax = plt.subplots(figsize=(8, 6))
        
        for subj in unique_subjs:
            sub = results_df[results_df["subject"] == subj]
            xs, ys = [], []
            for cond_label in custom_order:
                r = sub[sub["condition_label"] == cond_label]
                if len(r) > 0:
                    v = r[metric].values[0]
                    if not pd.isna(v):
                        xs.append(cond_x[cond_label])
                        ys.append(v)
            if xs:
                ax.plot(
                    xs,
                    ys,
                    marker=markers.get(subj, "o"),
                    color=colors.get(subj, "#555555"),
                    linewidth=2.5,
                    markersize=10,
                    label=SUBJECTS_KO.get(subj, subj),
                    alpha=0.85,
                )
        
        ax.set_xticks(range(len(custom_order)))
        ax.set_xticklabels(
            custom_order,
            fontsize=12,
            fontproperties=fm.FontProperties(family=KOREAN_FONT, size=12),
        )
        ax.set_title(
            f"피험자별 개인 프로파일: {title}",
            fontsize=14,
            fontweight="bold",
            fontproperties=fm.FontProperties(family=KOREAN_FONT, size=14),
        )
        ax.grid(True, alpha=0.4)
        ax.legend(fontsize=10, prop=fm.FontProperties(family=KOREAN_FONT, size=10), bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        _save(fig, os.path.join(out_dir, f"plot_spaghetti_{metric}.png"))
        plt.close(fig)


# ─────────────────────────────────────────────
# PLOT 7: 통계 검정 히트맵
# ─────────────────────────────────────────────

METRIC_LABELS_KO = {
    "cadence_steps_per_min": "케이던스",
    "shank_mean_peak_g": "무릎 Peak g",
    "shank_resultant_rms_m_s2": "무릎 Resultant RMS",
    "step_interval_cv_pct": "Step CV%",
    "pelvis_pitch_sd_deg": "골반 Pitch SD",
    "pelvis_roll_sd_deg": "골반 Roll SD",
    "ankle_dp_pf_rom_deg": "Ankle DF/PF ROM",
    "ankle_mean_dorsiflexion_peak_deg": "Ankle 평균 Dorsiflexion",
    "ankle_mean_plantarflexion_peak_deg": "Ankle 평균 Plantarflexion",
    "ankle_inv_ev_rom_deg": "Ankle Inv/Ev ROM",
}


def plot_statistics_heatmap(stats_df, out_dir):
    if stats_df.empty:
        print("  통계 데이터 없음.")
        return

    pivot_p = stats_df.pivot_table(index="metric", columns="comparison", values="p_value", aggfunc="first")
    pivot_c = stats_df.pivot_table(index="metric", columns="comparison", values="pct_change", aggfunc="first")

    pivot_p.index = [METRIC_LABELS_KO.get(m, m) for m in pivot_p.index]
    pivot_c.index = [METRIC_LABELS_KO.get(m, m) for m in pivot_c.index]

    fp = fm.FontProperties(family=KOREAN_FONT)

    # 1. p-value heatmap (개별 큰 사이즈)
    fig_p, ax1 = plt.subplots(figsize=(12, max(8, len(pivot_p) * 0.8)))
    pv = pivot_p.values.astype(float)
    im1 = ax1.imshow(pv, cmap="RdYlGn_r", vmin=0, vmax=0.1, aspect="auto")
    ax1.set_xticks(range(len(pivot_p.columns)))
    ax1.set_xticklabels(pivot_p.columns, rotation=25, ha="right", fontsize=12, fontproperties=fp)
    ax1.set_yticks(range(len(pivot_p.index)))
    ax1.set_yticklabels(pivot_p.index, fontsize=12, fontproperties=fp)
    ax1.set_title("p-value (Wilcoxon Test)\n녹색=유의, 빨강=비유의", fontsize=16, fontweight="bold", fontproperties=fm.FontProperties(family=KOREAN_FONT, size=16))
    for i in range(pv.shape[0]):
        for j in range(pv.shape[1]):
            v = pv[i, j]
            if not np.isnan(v):
                sig = "***" if v < 0.001 else ("**" if v < 0.01 else ("*" if v < 0.05 else "n.s."))
                ax1.text(j, i, f"{v:.3f}\n{sig}", ha="center", va="center", fontsize=11, fontweight="bold", color="black")
    plt.colorbar(im1, ax=ax1, shrink=0.85)
    plt.tight_layout()
    _save(fig_p, os.path.join(out_dir, "plot_statistics_heatmap_pvalue.png"))
    plt.close(fig_p)

    # 2. % change heatmap (개별 큰 사이즈)
    fig_c, ax2 = plt.subplots(figsize=(12, max(8, len(pivot_c) * 0.8)))
    cv = pivot_c.values.astype(float)
    vmax = np.nanmax(np.abs(cv)) if not np.all(np.isnan(cv)) else 10
    im2 = ax2.imshow(cv, cmap="RdBu_r", vmin=-vmax, vmax=vmax, aspect="auto")
    ax2.set_xticks(range(len(pivot_c.columns)))
    ax2.set_xticklabels(pivot_c.columns, rotation=25, ha="right", fontsize=12, fontproperties=fp)
    ax2.set_yticks(range(len(pivot_c.index)))
    ax2.set_yticklabels(pivot_c.index, fontsize=12, fontproperties=fp)
    ax2.set_title("% 변화량\n파랑=증가, 빨강=감소", fontsize=16, fontweight="bold", fontproperties=fm.FontProperties(family=KOREAN_FONT, size=16))
    for i in range(cv.shape[0]):
        for j in range(cv.shape[1]):
            v = cv[i, j]
            if not np.isnan(v):
                ax2.text(j, i, f"{v:+.1f}%", ha="center", va="center", fontsize=11, fontweight="bold", color="black")
    plt.colorbar(im2, ax=ax2, shrink=0.85)
    plt.tight_layout()
    _save(fig_c, os.path.join(out_dir, "plot_statistics_heatmap_pctchange.png"))
    plt.close(fig_c)


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────


def run_all_visualizations(results_df: pd.DataFrame, stats_df: pd.DataFrame, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    print(f"  폰트: {KOREAN_FONT}")

    print("\n[시각화] 메트로놈 효과...")
    plot_metronome_effects(results_df, out_dir)
    plot_metronome_variability(results_df, out_dir)

    print("\n[시각화] 테이핑 효과...")
    plot_taping_effects(results_df, out_dir)

    # 삭제됨: plot_impact_by_segment, plot_impact_peak_histograms, plot_z_impulse_by_segment

    print("\n[시각화] 피크 검출 예시...")
    plot_peak_detection_example(out_dir)

    print("\n[시각화] 전체 overview...")
    plot_all_conditions_overview(results_df, out_dir)

    print("\n[시각화] 피험자별 프로파일...")
    plot_individual_profiles(results_df, out_dir)

    print("\n[시각화] 통계 검정 히트맵...")
    plot_statistics_heatmap(stats_df, out_dir)

    print("\n* 모든 시각화 완료!")


if __name__ == "__main__":
    base = os.path.join(os.path.dirname(__file__), "..")
    results_df = pd.read_csv(os.path.join(base, "results", "metrics_by_condition.csv"))
    stats_df = pd.read_csv(os.path.join(base, "results", "statistical_tests.csv"))
    run_all_visualizations(results_df, stats_df, os.path.join(base, "results", "figures"))
