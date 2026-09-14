from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from analysis.pipeline import FS, GRAVITY, load_subject_condition, split_by_segment


SUBJECT = "오승민"
SUBJECT_LABEL = "O Seungmin"
CONDITION = "metro"
CONDITION_LABEL = "Metro"
CUTOFF_HZ = 15.0
MIN_DISTANCE_MS = 280.0
PROMINENCE_G = 0.2

OUT_DIR = ROOT / "results" / "figures" / "2026-06-17"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def _candidate_peak_heights_g() -> np.ndarray:
    df = load_subject_condition(SUBJECT, CONDITION)
    if df is None:
        raise FileNotFoundError(f"Missing data for {SUBJECT} / {CONDITION}")

    shank = split_by_segment(df)["shank"]
    acc = shank["shank_free_acceleration_resultant_m_s2"].to_numpy(dtype=float)

    nyquist = 0.5 * FS
    b, a = signal.butter(4, CUTOFF_HZ / nyquist, btype="low", analog=False)
    smoothed = signal.filtfilt(b, a, acc)

    candidates, _ = signal.find_peaks(
        smoothed,
        distance=int(FS * MIN_DISTANCE_MS / 1000.0),
        prominence=PROMINENCE_G * GRAVITY,
    )
    return smoothed[candidates] / GRAVITY


def make_figure() -> tuple[Path, Path]:
    peak_g = _candidate_peak_heights_g()
    q1 = np.percentile(peak_g, 25)
    q2 = np.percentile(peak_g, 50)
    q3 = np.percentile(peak_g, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    passed = (peak_g >= lower) & (peak_g <= upper)

    rng = np.random.default_rng(7)
    jitter = rng.normal(0.0, 0.035, size=len(peak_g))

    fig, ax = plt.subplots(figsize=(8, 8), facecolor="white")

    ax.axhspan(q1, q3, color="#DBEAFE", alpha=0.9, label="Middle 50%: IQR")
    ax.axhline(q1, color="#1D4ED8", linewidth=1.8)
    ax.axhline(q2, color="#111827", linewidth=1.8)
    ax.axhline(q3, color="#1D4ED8", linewidth=1.8)
    ax.axhline(lower, color="#EA580C", linewidth=1.6, linestyle="--")
    ax.axhline(upper, color="#EA580C", linewidth=1.6, linestyle="--")

    ax.scatter(
        np.full(np.sum(passed), 0.0) + jitter[passed],
        peak_g[passed],
        s=38,
        color="#2563EB",
        edgecolor="white",
        linewidth=0.45,
        alpha=0.92,
        zorder=3,
    )
    ax.scatter(
        np.full(np.sum(~passed), 0.0) + jitter[~passed],
        peak_g[~passed],
        s=15,
        color="#FACC15",
        edgecolor="#92400E",
        linewidth=0.5,
        alpha=0.6,
        zorder=4,
    )

    box_x0, box_x1 = 0.32, 0.55
    ax.fill_between([box_x0, box_x1], q1, q3, color="#93C5FD", alpha=0.75, edgecolor="#1D4ED8")
    ax.plot([box_x0, box_x1], [q2, q2], color="#111827", linewidth=2.1)
    ax.plot([(box_x0 + box_x1) / 2, (box_x0 + box_x1) / 2], [lower, q1], color="#374151", linewidth=1.4)
    ax.plot([(box_x0 + box_x1) / 2, (box_x0 + box_x1) / 2], [q3, upper], color="#374151", linewidth=1.4)
    ax.plot([box_x0 + 0.04, box_x1 - 0.04], [lower, lower], color="#374151", linewidth=1.4)
    ax.plot([box_x0 + 0.04, box_x1 - 0.04], [upper, upper], color="#374151", linewidth=1.4)

    label_box = dict(boxstyle="round,pad=0.22", fc="white", ec="none", alpha=0.92)
    text_x = 0.92
    ax.text(text_x, q1 - 0.08, f"Q1 = {q1:.2f} g", va="top", fontsize=11, color="#1D4ED8", bbox=label_box)
    ax.text(1.08, q2, f"Median = {q2:.2f} g", va="center", fontsize=11, color="#111827", bbox=label_box)
    ax.text(text_x, q3 + 0.08, f"Q3 = {q3:.2f} g", va="bottom", fontsize=11, color="#1D4ED8", bbox=label_box)
    ax.text(text_x, lower, f"Lower fence = Q1 - 1.5 x IQR = {lower:.2f} g", va="center", fontsize=10.5, color="#9A3412", bbox=label_box)
    ax.text(text_x, upper, f"Upper fence = Q3 + 1.5 x IQR = {upper:.2f} g", va="center", fontsize=10.5, color="#9A3412", bbox=label_box)

    ax.annotate(
        "",
        xy=(0.62, q3),
        xytext=(0.62, q1),
        arrowprops=dict(arrowstyle="<->", color="#1D4ED8", linewidth=1.7),
    )
    ax.text(
        0.66,
        (q1 + q3) / 2,
        f"IQR = Q3 - Q1\n= {iqr:.2f} g",
        fontsize=12,
        color="#1D4ED8",
        va="center",
        bbox=label_box,
    )

    ax.text(
        -0.17,
        lower - 0.17,
        "excluded",
        ha="center",
        va="top",
        fontsize=10,
        color="#92400E",
    )
    ax.text(
        -0.17,
        q2,
        "accepted",
        ha="center",
        va="center",
        fontsize=10,
        color="#2563EB",
    )
    ax.text(
        -0.17,
        upper + 0.17,
        "excluded",
        ha="center",
        va="bottom",
        fontsize=10,
        color="#92400E",
    )

    ax.set_title(
        f"IQR Filter Concept for Candidate Peak Heights\n{SUBJECT_LABEL} / {CONDITION_LABEL}",
        fontsize=17,
        fontweight="bold",
        pad=14,
    )
    ax.set_ylabel("Candidate peak height (g)", fontsize=12)
    ax.set_xlim(-0.32, 1.55)
    ax.set_xticks([])
    ax.grid(True, axis="y", color="#E5E7EB", linewidth=0.8)
    ax.spines["bottom"].set_visible(False)

    png_path = OUT_DIR / "iqr_filter_explanation_peak_heights.png"
    pdf_path = OUT_DIR / "iqr_filter_explanation_peak_heights.pdf"
    fig.savefig(png_path, dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(pdf_path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return png_path, pdf_path


if __name__ == "__main__":
    png, pdf = make_figure()
    print(png)
    print(pdf)
