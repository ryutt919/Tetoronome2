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
SEGMENT = "shank"
START_SEC = 0.0
DURATION_SEC = 5.0
CUTOFF_HZ = 15.0
MIN_DISTANCE_MS = 280.0
PROMINENCE_G = 0.2

OUT_DIR = ROOT / "results" / "figures" / "2026-06-17"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def butterworth_lowpass(values: np.ndarray, cutoff_hz: float = CUTOFF_HZ) -> np.ndarray:
    nyquist = 0.5 * FS
    normal_cutoff = cutoff_hz / nyquist
    b, a = signal.butter(4, normal_cutoff, btype="low", analog=False)
    return signal.filtfilt(b, a, values)


def detect_peak_sets(acc_resultant: np.ndarray) -> dict:
    smoothed = butterworth_lowpass(acc_resultant)
    min_distance_samples = int(FS * MIN_DISTANCE_MS / 1000.0)
    fixed_prominence = PROMINENCE_G * GRAVITY

    candidates, properties = signal.find_peaks(
        smoothed,
        distance=min_distance_samples,
        prominence=fixed_prominence,
    )

    peak_values = smoothed[candidates]
    q1 = np.percentile(peak_values, 25)
    q3 = np.percentile(peak_values, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    pass_mask = (peak_values >= lower) & (peak_values <= upper)

    return {
        "smoothed": smoothed,
        "candidates": candidates,
        "passed": candidates[pass_mask],
        "rejected": candidates[~pass_mask],
        "peak_values": peak_values,
        "pass_mask": pass_mask,
        "iqr_bounds": (lower, upper),
        "prominences": properties["prominences"],
    }


def make_figure() -> tuple[Path, Path]:
    df = load_subject_condition(SUBJECT, CONDITION)
    if df is None:
        raise FileNotFoundError(f"Missing data for {SUBJECT} / {CONDITION}")

    shank_df = split_by_segment(df)[SEGMENT]
    acc = shank_df["shank_free_acceleration_resultant_m_s2"].to_numpy(dtype=float)
    meta = detect_peak_sets(acc)

    raw_g = acc / GRAVITY
    smooth_g = meta["smoothed"] / GRAVITY
    lower_g, upper_g = [v / GRAVITY for v in meta["iqr_bounds"]]

    start_idx = int(START_SEC * FS)
    end_idx = min(len(acc), int((START_SEC + DURATION_SEC) * FS))
    t = np.arange(start_idx, end_idx) / FS - START_SEC

    candidates = meta["candidates"]
    passed = meta["passed"]
    rejected = meta["rejected"]

    in_window = (candidates >= start_idx) & (candidates < end_idx)
    candidates_window = candidates[in_window]
    passed_window = passed[(passed >= start_idx) & (passed < end_idx)]
    rejected_window = rejected[(rejected >= start_idx) & (rejected < end_idx)]

    fig = plt.figure(figsize=(16, 9), facecolor="white")
    gs = fig.add_gridspec(2, 1, height_ratios=[2.35, 1], hspace=0.24)
    ax = fig.add_subplot(gs[0])
    ax_iqr = fig.add_subplot(gs[1])

    ax.plot(t, raw_g[start_idx:end_idx], color="#9CA3AF", linewidth=1.0, alpha=0.72, label="Raw resultant acceleration")
    ax.plot(t, smooth_g[start_idx:end_idx], color="#111827", linewidth=1.7, label="Butterworth low-pass 15 Hz")
    ax.axhspan(lower_g, upper_g, color="#DBEAFE", alpha=0.28, label="IQR accepted peak-height range")

    ax.scatter(
        candidates_window / FS - START_SEC,
        smooth_g[candidates_window],
        s=40,
        color="#FACC15",
        edgecolor="#92400E",
        linewidth=0.55,
        zorder=5,
        label="Peak candidates: prominence + distance",
    )
    ax.scatter(
        passed_window / FS - START_SEC,
        smooth_g[passed_window],
        s=72,
        color="#2563EB",
        edgecolor="white",
        linewidth=0.8,
        zorder=6,
        label="Final peaks after IQR",
    )
    if len(rejected_window) > 0:
        ax.scatter(
            rejected_window / FS - START_SEC,
            smooth_g[rejected_window],
            s=92,
            facecolors="none",
            edgecolors="#B45309",
            linewidth=1.5,
            zorder=7,
            label="IQR-rejected candidates",
        )

    ax.set_title(
        f"\n{SUBJECT_LABEL} / {CONDITION_LABEL}, {START_SEC:.0f}-{START_SEC + DURATION_SEC:.0f}s window",
        fontsize=17,
        fontweight="bold",
        pad=12,
    )
    ax.set_ylabel("Resultant acceleration (g)", fontsize=11)
    ax.set_xlim(0, DURATION_SEC)
    ax.grid(True, axis="y", color="#E5E7EB", linewidth=0.8)

    order = np.arange(1, len(candidates) + 1)
    peak_values_g = meta["peak_values"] / GRAVITY
    pass_mask = meta["pass_mask"]
    reject_mask = ~pass_mask

    ax_iqr.axhspan(lower_g, upper_g, color="#DBEAFE", alpha=0.35)
    ax_iqr.axhline(lower_g, color="#2563EB", linestyle="--", linewidth=1.0)
    ax_iqr.axhline(upper_g, color="#2563EB", linestyle="--", linewidth=1.0)
    ax_iqr.scatter(
        order[reject_mask],
        peak_values_g[reject_mask],
        s=40,
        color="#FACC15",
        edgecolor="#92400E",
        linewidth=0.55,
        label="Rejected by IQR",
        zorder=5,
    )
    ax_iqr.scatter(
        order[pass_mask],
        peak_values_g[pass_mask],
        s=24,
        color="#2563EB",
        edgecolor="white",
        linewidth=0.35,
        label="Passed IQR",
        zorder=4,
    )

    ax_iqr.set_title(
        f"IQR filter on candidate peak heights: {len(candidates)} candidates -> {len(passed)} final peaks ({len(rejected)} rejected)",
        fontsize=12,
        loc="left",
        pad=7,
    )
    ax_iqr.set_xlabel("Peak candidate number across full trial", fontsize=10)
    ax_iqr.set_ylabel("Smoothed peak height (g)", fontsize=10)
    ax_iqr.grid(True, axis="y", color="#E5E7EB", linewidth=0.8)

    fig.text(
        0.01,
        0.012,
        "Pipeline: raw shank resultant acceleration -> 15 Hz Butterworth smoothing -> "
        "find_peaks(prominence >= 0.2 g, distance >= 280 ms) -> IQR filter on peak heights.",
        fontsize=9.5,
        color="#374151",
    )

    png_path = OUT_DIR / "preprocessing_peak_detection_osm_metro_0_25s.png"
    pdf_path = OUT_DIR / "preprocessing_peak_detection_osm_metro_0_25s.pdf"
    fig.savefig(png_path, dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(pdf_path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return png_path, pdf_path


if __name__ == "__main__":
    png, pdf = make_figure()
    print(png)
    print(pdf)
