"""
Control → Metro / Tape / Tape+Metro 변화율 bar chart + 피험자별 실측값 표 figure 생성

변화율 계산 방식: 그룹 평균 (mean_target - mean_ctrl) / |mean_ctrl| × 100
(statistical_tests.csv의 pct_change 컬럼을 직접 사용하여 보고서 수치와 일치)
"""

import os
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings

warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# 한글 폰트 설정
# ─────────────────────────────────────────────


def _setup_korean_font():
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
    return "DejaVu Sans"


KOREAN_FONT = _setup_korean_font()

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
    }
)

# ─────────────────────────────────────────────
# 설정
# ─────────────────────────────────────────────

METRICS = [
    "shank_mean_peak_g",
    "step_interval_cv_pct",
    "pelvis_pitch_sd_deg",
    "pelvis_roll_sd_deg",
    "ankle_dp_pf_rom_deg",
    "ankle_mean_dorsiflexion_peak_deg",
    "ankle_mean_plantarflexion_peak_deg",
]

METRIC_LABELS = {
    "shank_mean_peak_g": "정강이 평균 충격 피크 (g)",
    "step_interval_cv_pct": "보폭 간격 변동계수 (%)",
    "pelvis_pitch_sd_deg": "골반 Pitch SD (°)",
    "pelvis_roll_sd_deg": "골반 Roll SD (°)",
    "ankle_dp_pf_rom_deg": "발목 DF/PF ROM (°)",
    "ankle_mean_dorsiflexion_peak_deg": "발목 배굴 피크 (°)",
    "ankle_mean_plantarflexion_peak_deg": "발목 저굴 피크 (°)",
}

# statistical_tests.csv의 comparison 컬럼 값과 일치해야 함
SIG_COMPARISON_LABEL = {
    "Metro": "메트로 효과 (C→M)",
    "Tape": "테이핑 효과 (C→T)",
    "Tape+Metro": "복합 효과 (C→T+M)",
}

CONDITIONS = ["Control", "Metro", "Tape", "Tape+Metro"]
COND_SHORT  = ["Control", "Metro", "Tape", "T+M"]

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
METRICS_CSV = os.path.join(ROOT, "results", "metrics_by_condition.csv")
STATS_CSV   = os.path.join(ROOT, "results", "statistical_tests.csv")
OUT_DIR     = os.path.join(ROOT, "results", "figures")


# ─────────────────────────────────────────────
# 데이터 로드 헬퍼
# ─────────────────────────────────────────────


def load_stats(target_condition):
    """stats CSV에서 pct_change, sig, n_subjects 딕셔너리 반환."""
    stats = pd.read_csv(STATS_CSV)
    label = SIG_COMPARISON_LABEL[target_condition]
    sub = stats[stats["comparison"] == label].set_index("metric")
    return (
        sub["pct_change"].to_dict(),
        sub["sig"].to_dict(),
        sub["n_subjects"].to_dict(),
    )


# ─────────────────────────────────────────────
# 변화율 bar chart
# ─────────────────────────────────────────────


def plot_change_rate(target_condition, out_path):
    fp       = fm.FontProperties(family=KOREAN_FONT)
    fp_title = fm.FontProperties(family=KOREAN_FONT, size=12)

    pct_map, sig_map, n_map = load_stats(target_condition)

    pct_vals = [pct_map.get(m, 0.0) for m in METRICS]
    x_pos    = np.arange(len(METRICS))
    x_labels = [METRIC_LABELS[m] for m in METRICS]

    fig, ax = plt.subplots(figsize=(10, 6))

    colors = ["#2E86AB" if v >= 0 else "#E84855" for v in pct_vals]
    ax.bar(x_pos, pct_vals, color=colors, alpha=0.82, edgecolor="white", linewidth=0.8, width=0.55)
    ax.axhline(0, color="black", linewidth=0.9, zorder=2)

    val_range = max(abs(max(pct_vals)), abs(min(pct_vals))) if pct_vals else 1.0
    offset    = val_range * 0.08

    for i, (m, val) in enumerate(zip(METRICS, pct_vals)):
        sig      = sig_map.get(m, "n.s.")
        sig_str  = " *" if sig == "*" else ""
        label_str = f"{val:+.1f}%{sig_str}"
        va = "bottom" if val >= 0 else "top"
        y  = val + offset if val >= 0 else val - offset
        ax.text(i, y, label_str, va=va, ha="center", fontsize=8.5, color="#222222", fontproperties=fp)

    ax.set_xticks(x_pos)
    ax.set_xticklabels(x_labels, fontproperties=fp, fontsize=9, rotation=20, ha="right")
    ax.set_ylabel("변화율 (%)", fontproperties=fp, fontsize=10)
    ax.grid(axis="y", linestyle="--", alpha=0.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ns = [n_map.get(m, 0) for m in METRICS]
    n_display = max(set(ns), key=ns.count) if ns else "?"

    title_map = {
        "Metro":      f"Control → Metro 종합 변화율 (N={n_display}, 그룹 평균 기준)",
        "Tape":       f"Control → Tape 종합 변화율 (N={n_display}, 그룹 평균 기준)",
        "Tape+Metro": f"Control → Tape+Metro 종합 변화율 (N={n_display}, 그룹 평균 기준)",
    }
    ax.set_title(title_map[target_condition], fontproperties=fp_title, fontweight="bold", pad=14)

    y_min, y_max = ax.get_ylim()
    margin = max(abs(y_min), abs(y_max)) * 0.3
    ax.set_ylim(y_min - margin, y_max + margin)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"저장: {out_path}")


# ─────────────────────────────────────────────
# 피험자별 실측값 표 figure
# ─────────────────────────────────────────────


def plot_subject_tables(df, out_path):
    """7개 지표 × 피험자별 실측값 + 그룹 평균 + 변화율 표 (4×2 grid)."""
    fp       = fm.FontProperties(family=KOREAN_FONT, size=7.5)
    fp_hdr   = fm.FontProperties(family=KOREAN_FONT, size=8, weight="bold")
    fp_bold  = fm.FontProperties(family=KOREAN_FONT, size=7.5, weight="bold")
    fp_title = fm.FontProperties(family=KOREAN_FONT, size=9.5, weight="bold")

    subjects = df[df["condition_label"] == "Control"]["subject"].tolist()

    stats = pd.read_csv(STATS_CSV)

    def get_pct(comparison_label, metric):
        row = stats[(stats["comparison"] == comparison_label) & (stats["metric"] == metric)]
        return float(row["pct_change"].values[0]) if len(row) > 0 else None

    nrows_grid, ncols_grid = 4, 2
    fig, axes = plt.subplots(nrows_grid, ncols_grid, figsize=(20, 30), facecolor="white")

    for idx, metric in enumerate(METRICS):
        r, c = divmod(idx, ncols_grid)
        ax = axes[r][c]
        ax.axis("off")

        col_labels = ["피험자"] + COND_SHORT
        cell_text  = []

        # 피험자 행
        for subj in subjects:
            row = [subj]
            for cond in CONDITIONS:
                rows = df[(df["subject"] == subj) & (df["condition_label"] == cond)]
                if len(rows) == 0:
                    row.append("N/A")
                else:
                    val = rows[metric].values[0]
                    row.append("N/A" if pd.isna(val) else f"{val:.2f}")
            cell_text.append(row)

        # 그룹 평균 행
        mean_row = ["그룹 평균"]
        for cond in CONDITIONS:
            vals = df[df["condition_label"] == cond][metric].dropna()
            mean_row.append(f"{vals.mean():.2f}" if len(vals) > 0 else "N/A")
        cell_text.append(mean_row)

        # 변화율 행 3개 (C→M, C→T, C→T+M)
        for comp_label, cond_name, short in [
            (SIG_COMPARISON_LABEL["Metro"],      "Metro",      "Metro"),
            (SIG_COMPARISON_LABEL["Tape"],       "Tape",       "Tape"),
            (SIG_COMPARISON_LABEL["Tape+Metro"], "Tape+Metro", "T+M"),
        ]:
            pct_val  = get_pct(comp_label, metric)
            row      = [f"C→{short} %", "-", "-", "-", "-"]
            cond_col = CONDITIONS.index(cond_name) + 1  # +1 for subject col
            row[cond_col] = f"{pct_val:+.1f}%" if pct_val is not None else "N/A"
            cell_text.append(row)

        # 테이블 생성
        t = ax.table(
            cellText=cell_text,
            colLabels=col_labels,
            cellLoc="center",
            loc="center",
            bbox=[0, 0, 1, 1],
        )
        t.auto_set_font_size(False)

        n_subj  = len(subjects)
        n_cols  = len(col_labels)

        # 헤더 행
        for j in range(n_cols):
            cell = t[(0, j)]
            cell.set_facecolor("#1e40af")
            cell.get_text().set_color("white")
            cell.get_text().set_fontproperties(fp_hdr)

        # 피험자 행 (교대 배경)
        for i in range(1, n_subj + 1):
            bg = "#ffffff" if i % 2 == 1 else "#f0f4f8"
            for j in range(n_cols):
                cell = t[(i, j)]
                cell.set_facecolor(bg)
                cell.get_text().set_fontproperties(fp)

        # 그룹 평균 행
        mean_row_idx = n_subj + 1
        for j in range(n_cols):
            cell = t[(mean_row_idx, j)]
            cell.set_facecolor("#dbeafe")
            cell.get_text().set_fontproperties(fp_bold)

        # 변화율 행 3개
        pct_row_bg = ["#fef9c3", "#dcfce7", "#fce7f3"]
        pct_cond_cols = [2, 3, 4]  # Metro, Tape, T+M 열 인덱스
        for pi in range(3):
            row_idx  = n_subj + 2 + pi
            cond_col = pct_cond_cols[pi]
            for j in range(n_cols):
                cell = t[(row_idx, j)]
                cell.set_facecolor(pct_row_bg[pi])
                cell.get_text().set_fontproperties(fp)
            # 변화율 값 셀 볼드
            pct_cell = t[(row_idx, cond_col)]
            pct_cell.get_text().set_fontproperties(fp_bold)

        ax.set_title(METRIC_LABELS[metric], fontproperties=fp_title, pad=5)

    # 마지막 빈 subplot 숨김
    axes[-1][-1].axis("off")

    fig.suptitle(
        "피험자별 지표 실측값 전체 정리 (N=6, 조건별)",
        fontproperties=fm.FontProperties(family=KOREAN_FONT, size=13, weight="bold"),
        y=1.005,
    )
    fig.tight_layout(pad=1.5)
    fig.savefig(out_path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"저장: {out_path}")


# ─────────────────────────────────────────────
# 메인
# ─────────────────────────────────────────────

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    df = pd.read_csv(METRICS_CSV)

    plot_change_rate("Metro",      os.path.join(OUT_DIR, "change_rate_ctrl_metro.png"))
    plot_change_rate("Tape",       os.path.join(OUT_DIR, "change_rate_ctrl_tape.png"))
    plot_change_rate("Tape+Metro", os.path.join(OUT_DIR, "change_rate_ctrl_tapemetro.png"))
    plot_subject_tables(df,            os.path.join(OUT_DIR, "subject_values_table.png"))
