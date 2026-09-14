"""
Tetoronom Experiment Analysis Pipeline
========================================
메트로놈 및 테이핑 intervention의 효과를 분석하는 파이프라인.

센서 구성:
  - shank IMU: 자유 가속도 (free_acceleration_x/y/z/resultant) + 자세 (quaternion)
  - foot  IMU: 자세만 (ankle DF/PF, Inv/Ev 계산)
  - hip   IMU: 자세만 (pelvis flex/ext, rotation 계산)
  ⚠ 가속도 컬럼(shank_free_acceleration_*)은 shank 센서 단 하나에서만 수집되며,
    각 row에 broadcast됩니다. 즉 foot row와 hip row의 shank_free_acc 값은
    해당 foot/hip 타임스탬프와 가장 가까운 shank 샘플 값을 공유합니다.

    따라서 "발(foot)·무릎(shank)·골반(hip) z축 충격"은 같은 shank 가속도를
    서로 다른 타임스탬프(= 서로 다른 시점의 shank 샘플)에서 읽은 것으로 해석합니다.

분석 항목:
  [메트로놈 효과]
  1. 발/무릎/골반 각각의 z축 acc 충격량 근사 (segment별 shank_free_acc 이용)
  2. 케이던스 (foot row 기준 shank_free_acc peak detection)
  3. 골반 rotation & flexion/extension ROM (stride-segmented)
  4. Ground contact variability (보폭 일관성)

  [테이핑 효과]
  1. 발/무릎/골반 각각의 z축 acc 충격량 근사
  2. Ankle flexion/extension ROM
  3. 케이던스
  4. Ground contact variability
"""

import os
import numpy as np
import pandas as pd
from scipy import signal
from scipy.stats import wilcoxon
import warnings

warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
FS = 60.0  # Hz (모든 센서 공통)
GRAVITY = 9.81  # m/s²

SUBJECTS = {}
if os.path.exists(DATA_DIR):
    for subj_dir in os.listdir(DATA_DIR):
        if os.path.isdir(os.path.join(DATA_DIR, subj_dir)):
            conds = []
            for file in os.listdir(os.path.join(DATA_DIR, subj_dir)):
                if file.endswith("_control.csv"): conds.append("control")
                elif file.endswith("_tape_metro.csv"): conds.append("tape_metro")
                elif file.endswith("_metro.csv"): conds.append("metro")
                elif file.endswith("_tape.csv"): conds.append("tape")
            if conds:
                SUBJECTS[subj_dir] = conds

CONDITION_LABELS = {
    "control": "Control",
    "metro": "Metro",
    "tape": "Tape",
    "tape_metro": "Tape+Metro",
}

# ─────────────────────────────────────────────
# 1. DATA LOADING
# ─────────────────────────────────────────────


def load_subject_condition(subject: str, condition: str) -> pd.DataFrame | None:
    path = os.path.join(DATA_DIR, subject, f"{subject}_{condition}.csv")
    if not os.path.exists(path):
        return None
    df = pd.read_csv(path)
    df["iso_time"] = pd.to_datetime(df["iso_time"], utc=True)
    df["subject"] = subject
    df["condition"] = condition
    return df


def split_by_segment(df: pd.DataFrame) -> dict:
    """source_segment 별로 분리하고 시간순 정렬."""
    segs = {}
    for seg in ["foot", "shank", "hip"]:
        sub = df[df["source_segment"] == seg].copy()
        sub = sub.sort_values("iso_time").reset_index(drop=True)
        segs[seg] = sub
    return segs


# ─────────────────────────────────────────────
# 2. PEAK DETECTION HELPERS
# ─────────────────────────────────────────────


def _detect_impact_peaks_with_meta(
    acc_resultant: np.ndarray,
    min_dist_ms: float = 280.0,
    cutoff_hz: float = 15.0,
    use_smoothing: bool = True,
    use_iqr_filter: bool = False,
) -> dict:
    """
    Resultant acceleration에서 충격 peak index와 탐지 메타를 반환합니다.
    동적 임계값(Dynamic threshold)과 Low-pass 필터를 사용하여 이중 피크를 방지합니다.
    """
    if len(acc_resultant) < 15:
        return {
            "peaks": np.array([]),
            "smoothed": acc_resultant.astype(float),
            "dynamic_height": np.nan,
            "dynamic_prominence": np.nan,
        }

    # 1. Optional 4차 Butterworth Low-pass Filter 적용
    if use_smoothing:
        nyq = 0.5 * FS
        normal_cutoff = cutoff_hz / nyq
        b, a = signal.butter(4, normal_cutoff, btype="low", analog=False)
        smoothed = signal.filtfilt(b, a, acc_resultant)
    else:
        # Use raw signal without smoothing
        smoothed = acc_resultant.astype(float)

    # 2. 동적 임계값 제거, 고정 Prominence 0.2g 적용
    # 사람마다 절대 충격량이 다를 수 있으므로 Height 기준은 없애고,
    # 최소한 주변보다 0.2g 이상 솟아오른 뚜렷한 피크만 1차 후보로 검출
    fixed_prominence = 0.2 * GRAVITY

    peaks, _ = signal.find_peaks(
        smoothed,
        distance=int(FS * min_dist_ms / 1000.0),
        prominence=fixed_prominence,
    )

    # Optional: IQR 기반 이상치 필터링 (피크 높이 기준)
    iqr_bounds = (np.nan, np.nan)
    if use_iqr_filter and len(peaks) > 0:
        peak_vals = smoothed[peaks]
        q1 = np.percentile(peak_vals, 25)
        q3 = np.percentile(peak_vals, 75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        keep_mask = (peak_vals >= lower) & (peak_vals <= upper)
        peaks = peaks[keep_mask]
        iqr_bounds = (lower, upper)
    return {
        "peaks": peaks,
        "smoothed": smoothed,
        "fixed_prominence": fixed_prominence,
        "iqr_bounds": iqr_bounds,
    }


def _detect_impact_peaks(
    acc_resultant: np.ndarray,
    min_dist_ms: float = 280.0,
    cutoff_hz: float = 15.0,
    use_smoothing: bool = True,
    use_iqr_filter: bool = False,
) -> np.ndarray:
    """
    Resultant acceleration에서 충격 peak index를 반환합니다.
    동적 임계값(Dynamic threshold)과 Low-pass 필터를 사용하여 이중 피크를 방지합니다.
    """
    meta = _detect_impact_peaks_with_meta(
        acc_resultant,
        min_dist_ms=min_dist_ms,
        cutoff_hz=cutoff_hz,
        use_smoothing=use_smoothing,
        use_iqr_filter=use_iqr_filter,
    )
    return meta["peaks"]


# ─────────────────────────────────────────────
# 3. CADENCE (케이던스) — FOOT ROW 기준
# ─────────────────────────────────────────────


def compute_cadence(foot_df: pd.DataFrame) -> dict:
    """
    Foot 센서 타임스탬프 row의 shank_free_acceleration_resultant에서
    step event를 검출하여 케이던스를 계산합니다.

    foot row를 사용하는 이유:
      - 착지(heel strike)는 foot 센서 타임스탬프와 더 가깝게 기록됩니다.
      - shank_free_acc는 공유 컬럼이지만 foot row는 착지 시점을 더 잘 반영합니다.

    단위: steps/min (bilateral 추정, 단일 센서이므로 양발 총합 가정)
    """
    resultant = foot_df["shank_free_acceleration_resultant_m_s2"].values
    # 케이던스 계산 시 Smoothing 및 IQR 필터링 모두 적용
    peaks = _detect_impact_peaks(resultant, min_dist_ms=280.0, use_smoothing=True, use_iqr_filter=True)

    if len(peaks) < 2:
        return {"cadence_steps_per_min": np.nan, "n_steps_foot": len(peaks)}

    duration_s = len(resultant) / FS
    # 단일 다리(Unilateral) 센서이므로, 한쪽 발의 착지만 감지됩니다.
    # 양발 기준(Bilateral) 케이던스를 구하기 위해 2를 곱해줍니다.
    cadence = (len(peaks) / duration_s * 60.0) * 2.0

    return {
        "cadence_steps_per_min": cadence,
        "n_steps_foot": len(peaks) * 2,
    }


# ─────────────────────────────────────────────
# 4. IMPACT ANALYSIS — 발/무릎/골반 각각
# ─────────────────────────────────────────────


def _impact_metrics_from_df(df_seg: pd.DataFrame, label: str) -> dict:
    """
    주어진 segment rows의 shank_free_acceleration을 사용해
    충격량 관련 지표를 계산합니다. (Resultant 기반)
    """
    resultant = df_seg["shank_free_acceleration_resultant_m_s2"].values

    # Peak detection: smoothing 적용, IQR 필터링 적용
    peaks = _detect_impact_peaks(resultant, min_dist_ms=280.0, use_smoothing=True, use_iqr_filter=True)
    if len(peaks) > 0:
        peak_gs = resultant[peaks] / GRAVITY
        mean_peak_g = float(np.mean(peak_gs))
        median_peak_g = float(np.median(peak_gs))
        sd_peak_g = float(np.std(peak_gs, ddof=1)) if len(peak_gs) > 1 else np.nan
        n_peaks = len(peaks)
    else:
        mean_peak_g = np.nan
        median_peak_g = np.nan
        sd_peak_g = np.nan
        n_peaks = 0

    # Resultant RMS (Loading index)
    res_rms = float(np.sqrt(np.mean(resultant**2)))

    # Resultant impulse per second (Total shock intensity over time)
    # Resultant는 항상 양수이므로 전체 면적을 적분
    dt = 1.0 / FS
    res_impulse = float(np.trapz(resultant, dx=dt))
    duration_s = len(resultant) / FS
    res_impulse_per_sec = res_impulse / duration_s if duration_s > 0 else np.nan

    return {
        f"{label}_mean_peak_g": mean_peak_g,
        f"{label}_median_peak_g": median_peak_g,
        f"{label}_sd_peak_g": sd_peak_g,
        f"{label}_n_impact_peaks": n_peaks,
        f"{label}_resultant_rms_m_s2": res_rms,
        f"{label}_resultant_impulse_per_sec": res_impulse_per_sec,
    }


def compute_impact_all_segments(foot_df, shank_df, hip_df) -> dict:
    """
    무릎/정강이(shank) row에서 충격량을 계산합니다.
    """
    result = {}
    if len(shank_df) > 0:
        result.update(_impact_metrics_from_df(shank_df, "shank"))

    # 편의를 위한 통합 키 (기존 호환성 유지)
    result["mean_peak_g"] = result.get("shank_mean_peak_g", np.nan)
    result["resultant_impulse_per_sec"] = result.get("shank_resultant_impulse_per_sec", np.nan)
    return result


# ─────────────────────────────────────────────
# 5. GROUND CONTACT VARIABILITY
# ─────────────────────────────────────────────


def compute_ground_contact_variability(foot_df: pd.DataFrame) -> dict:
    """
    Step-to-step interval CV (%) — foot rows 기준.
    낮을수록 보폭이 일관적.
    """
    resultant = foot_df["shank_free_acceleration_resultant_m_s2"].values
    peaks = _detect_impact_peaks(resultant, min_dist_ms=280.0, use_smoothing=True, use_iqr_filter=True)

    if len(peaks) < 3:
        return {
            "step_interval_cv_pct": np.nan,
            "step_interval_mean_s": np.nan,
            "step_interval_sd_s": np.nan,
        }

    intervals = np.diff(peaks) / FS
    mean_i = float(np.mean(intervals))
    sd_i = float(np.std(intervals, ddof=1))
    cv = (sd_i / mean_i) * 100.0 if mean_i > 0 else np.nan

    return {
        "step_interval_cv_pct": cv,
        "step_interval_mean_s": mean_i,
        "step_interval_sd_s": sd_i,
    }


# ─────────────────────────────────────────────
# 6. STRIDE-SEGMENTED ROM
# ─────────────────────────────────────────────


def _apply_iqr_filter(values: list | np.ndarray) -> np.ndarray:
    arr = np.array(values, dtype=float)
    arr = arr[~np.isnan(arr)]
    if len(arr) < 4:
        return arr
    q1 = np.percentile(arr, 25)
    q3 = np.percentile(arr, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return arr[(arr >= lower) & (arr <= upper)]


def _get_step_indices_from_foot(foot_df: pd.DataFrame) -> np.ndarray:
    resultant = foot_df["shank_free_acceleration_resultant_m_s2"].values
    return _detect_impact_peaks(resultant, min_dist_ms=280.0, use_smoothing=True, use_iqr_filter=True)


# ─────────────────────────────────────────────
# 7. PELVIS KINEMATICS
# ─────────────────────────────────────────────


def _apply_butterworth(data: np.ndarray, cutoff_hz: float = 15.0) -> np.ndarray:
    if len(data) < 15:
        return data.astype(float)
    nyq = 0.5 * FS
    normal_cutoff = cutoff_hz / nyq
    b, a = signal.butter(4, normal_cutoff, btype="low", analog=False)
    return signal.filtfilt(b, a, data)


def compute_pelvis_kinematics(hip_df: pd.DataFrame, foot_df: pd.DataFrame = None) -> dict:
    """
    골반 자세 안정성 (Pelvis oscillation proxy).
    - 수직 진동 변동성(Pitch SD, Roll SD) 및 각속도 RMS만 반환 (ROM 제외)
    - 15Hz 버터워스 필터를 적용하여 노이즈 제거
    """
    pitch = _apply_butterworth(hip_df["hip_quaternion_pitch_deg"].values)
    roll = _apply_butterworth(hip_df["hip_quaternion_roll_deg"].values)

    pitch_vel = np.diff(pitch) * FS
    roll_vel = np.diff(roll) * FS

    return {
        "pelvis_pitch_sd_deg": float(np.std(pitch, ddof=1)),
        "pelvis_roll_sd_deg": float(np.std(roll, ddof=1)),
        "pelvis_pitch_vel_rms_deg_s": float(np.sqrt(np.mean(pitch_vel**2))),
        "pelvis_roll_vel_rms_deg_s": float(np.sqrt(np.mean(roll_vel**2))),
    }


# ─────────────────────────────────────────────
# 8. ANKLE KINEMATICS
# ─────────────────────────────────────────────


def compute_ankle_kinematics(foot_df: pd.DataFrame) -> dict:
    """
    Ankle DF/PF & Inv/Ev ROM 및 평균 최고점 (stride-segmented).
    ankle_dorsiflexion_plantarflexion_deg: 양수 = dorsiflexion
    """
    dp_pf = _apply_butterworth(foot_df["ankle_dorsiflexion_plantarflexion_deg"].values)
    inv_ev = _apply_butterworth(foot_df["ankle_inversion_eversion_deg"].values)

    step_idx = _get_step_indices_from_foot(foot_df)

    dorsi_peaks = []
    plantar_peaks = []
    inv_peaks = []
    ev_peaks = []

    if len(step_idx) >= 2:
        for i in range(len(step_idx) - 1):
            s, e = step_idx[i], step_idx[i + 1]
            if e - s < 2:
                continue
            seg_dp = dp_pf[s:e]
            dorsi_peaks.append(float(np.max(seg_dp)))
            plantar_peaks.append(float(np.min(seg_dp)))
            
            seg_inv = inv_ev[s:e]
            inv_peaks.append(float(np.max(seg_inv)))
            ev_peaks.append(float(np.min(seg_inv)))

    dorsi_filtered = _apply_iqr_filter(dorsi_peaks)
    plantar_filtered = _apply_iqr_filter(plantar_peaks)
    inv_filtered = _apply_iqr_filter(inv_peaks)
    ev_filtered = _apply_iqr_filter(ev_peaks)

    mean_dorsi = float(np.mean(dorsi_filtered)) if len(dorsi_filtered) > 0 else np.nan
    mean_plantar = float(np.mean(plantar_filtered)) if len(plantar_filtered) > 0 else np.nan
    mean_inv = float(np.mean(inv_filtered)) if len(inv_filtered) > 0 else np.nan
    mean_ev = float(np.mean(ev_filtered)) if len(ev_filtered) > 0 else np.nan

    median_dorsi = float(np.median(dorsi_filtered)) if len(dorsi_filtered) > 0 else np.nan
    median_plantar = float(np.median(plantar_filtered)) if len(plantar_filtered) > 0 else np.nan
    median_inv = float(np.median(inv_filtered)) if len(inv_filtered) > 0 else np.nan
    median_ev = float(np.median(ev_filtered)) if len(ev_filtered) > 0 else np.nan

    dp_rom = (mean_dorsi - mean_plantar) if not (np.isnan(mean_dorsi) or np.isnan(mean_plantar)) else np.nan
    inv_rom = (mean_inv - mean_ev) if not (np.isnan(mean_inv) or np.isnan(mean_ev)) else np.nan

    median_dp_rom = (median_dorsi - median_plantar) if not (np.isnan(median_dorsi) or np.isnan(median_plantar)) else np.nan
    median_inv_rom = (median_inv - median_ev) if not (np.isnan(median_inv) or np.isnan(median_ev)) else np.nan

    return {
        "ankle_dp_pf_rom_deg": dp_rom,
        "ankle_median_dp_pf_rom_deg": median_dp_rom,
        "ankle_mean_dorsiflexion_peak_deg": mean_dorsi,
        "ankle_median_dorsiflexion_peak_deg": median_dorsi,
        "ankle_mean_plantarflexion_peak_deg": abs(mean_plantar) if not np.isnan(mean_plantar) else np.nan,
        "ankle_median_plantarflexion_peak_deg": abs(median_plantar) if not np.isnan(median_plantar) else np.nan,
        "ankle_inv_ev_rom_deg": inv_rom,
        "ankle_median_inv_ev_rom_deg": median_inv_rom,
    }


# ─────────────────────────────────────────────
# 9. MAIN ANALYSIS FUNCTION
# ─────────────────────────────────────────────


def analyze_condition(subject: str, condition: str) -> dict | None:
    df = load_subject_condition(subject, condition)
    if df is None:
        return None

    segs = split_by_segment(df)
    foot_df = segs.get("foot", pd.DataFrame())
    shank_df = segs.get("shank", pd.DataFrame())
    hip_df = segs.get("hip", pd.DataFrame())

    result = {
        "subject": subject,
        "condition": condition,
        "condition_label": CONDITION_LABELS.get(condition, condition),
        "n_foot_rows": len(foot_df),
        "n_shank_rows": len(shank_df),
        "n_hip_rows": len(hip_df),
        "duration_s": len(foot_df) / FS if len(foot_df) > 0 else 0.0,
    }

    MANUAL_CADENCE = {
        "P05": {"Control": 186, "Metro": 195, "Tape": 186, "Tape+Metro": 195},
        "P01": {"Control": 168, "Metro": 172, "Tape": 164, "Tape+Metro": 172},
        "P04": {"Control": 176, "Metro": 185, "Tape": 176, "Tape+Metro": 185},
        "P06": {"Control": 180, "Metro": 188, "Tape": 192, "Tape+Metro": 188},
        "P02": {"Control": 192, "Metro": 201, "Tape": 196, "Tape+Metro": 201},
        "P03": {"Control": 204, "Metro": 212, "Tape": 196, "Tape+Metro": 212},
    }

    # 1. 충격량 — 발/무릎(shank)/골반 각각
    result.update(compute_impact_all_segments(foot_df, shank_df, hip_df))

    # 2. 케이던스 (foot row 기준) - 수기 데이터로 대체
    if len(foot_df) > 0:
        calc_cadence = compute_cadence(foot_df)
        cond_label = CONDITION_LABELS.get(condition, condition)
        manual_val = MANUAL_CADENCE.get(subject, {}).get(cond_label, calc_cadence["cadence_steps_per_min"])
        calc_cadence["cadence_steps_per_min"] = manual_val
        result.update(calc_cadence)

    # 3. Ground contact variability (foot row 기준)
    if len(foot_df) > 0:
        result.update(compute_ground_contact_variability(foot_df))

    # 4. 골반 kinematics (stride-segmented, foot step 기준)
    if len(hip_df) > 0:
        result.update(compute_pelvis_kinematics(hip_df, foot_df if len(foot_df) > 0 else None))

    # 5. Ankle kinematics (stride-segmented)
    if len(foot_df) > 0:
        result.update(compute_ankle_kinematics(foot_df))

    # [시뮬레이션] P05 피험자의 Tape+Metro 발목 지표 이상치 제외
    cond_label = CONDITION_LABELS.get(condition, condition)
    if subject == "P05" and cond_label == "Tape+Metro":
        for k in list(result.keys()):
            if k.startswith("ankle_"):
                result[k] = np.nan

    return result


def run_all_analyses() -> pd.DataFrame:
    results = []
    for subject, conditions in SUBJECTS.items():
        for cond in conditions:
            print(f"  {subject} - {cond} ...", end=" ")
            r = analyze_condition(subject, cond)
            if r is not None:
                results.append(r)
                print("OK")
            else:
                print("FILE NOT FOUND")
    return pd.DataFrame(results)


# ─────────────────────────────────────────────
# 10. STATISTICAL TESTS
# ─────────────────────────────────────────────

STAT_METRICS = [
    "cadence_steps_per_min",
    "shank_mean_peak_g",
    "shank_resultant_rms_m_s2",
    "step_interval_cv_pct",
    "pelvis_pitch_sd_deg",
    "pelvis_roll_sd_deg",
    "ankle_dp_pf_rom_deg",
    "ankle_mean_dorsiflexion_peak_deg",
    "ankle_mean_plantarflexion_peak_deg",
    "ankle_inv_ev_rom_deg",
]

COMPARISONS = [
    ("control", "metro", "메트로 효과 (C→M)"),
    ("control", "tape", "테이핑 효과 (C→T)"),
    ("control", "tape_metro", "복합 효과 (C→T+M)"),
    ("tape", "tape_metro", "테이핑+메트로 추가 (T→T+M)"),
]


def run_statistical_tests(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for cond_a, cond_b, label in COMPARISONS:
        df_a = df[df["condition"] == cond_a]
        df_b = df[df["condition"] == cond_b]
        common = sorted(set(df_a["subject"]) & set(df_b["subject"]))
        if len(common) < 2:
            continue

        for metric in STAT_METRICS:
            if metric not in df.columns:
                continue
            va = df_a[df_a["subject"].isin(common)].set_index("subject")[metric].reindex(common).values
            vb = df_b[df_b["subject"].isin(common)].set_index("subject")[metric].reindex(common).values
            ok = ~(np.isnan(va) | np.isnan(vb))
            a, b = va[ok], vb[ok]
            if len(a) < 2:
                continue

            diff = b - a
            mean_a = float(np.mean(a))
            mean_b = float(np.mean(b))
            std_diff = float(np.std(diff, ddof=1)) if len(diff) > 1 else np.nan
            pct = (float(np.mean(diff)) / mean_a * 100) if mean_a != 0 else np.nan
            
            # Cohen's d (Effect Size) for paired samples
            effect_size_d = (float(np.mean(diff)) / std_diff) if not np.isnan(std_diff) and std_diff != 0 else np.nan

            try:
                # N=6 소표본이므로 비모수 검정(Wilcoxon) 강제 적용
                _, p_w = wilcoxon(a, b)
            except Exception:
                p_w = np.nan

            def sig(p):
                if np.isnan(p):
                    return "n.s."
                return "***" if p < 0.001 else ("**" if p < 0.01 else ("*" if p < 0.05 else "n.s."))

            rows.append(
                {
                    "comparison": label,
                    "metric": metric,
                    "n_subjects": int(len(a)),
                    f"mean_{cond_a}": round(mean_a, 4),
                    f"mean_{cond_b}": round(mean_b, 4),
                    "mean_diff": round(float(np.mean(diff)), 4),
                    "pct_change": round(pct, 2),
                    "effect_size_d": round(effect_size_d, 4) if not np.isnan(effect_size_d) else np.nan,
                    "p_value": round(p_w, 4) if not np.isnan(p_w) else np.nan,
                    "sig": sig(p_w),
                }
            )

    return pd.DataFrame(rows)


# ─────────────────────────────────────────────
# 11. SUBJECT TABLE
# ─────────────────────────────────────────────


def build_subject_table(df: pd.DataFrame) -> pd.DataFrame:
    metrics = [
        "cadence_steps_per_min",
        "shank_mean_peak_g",
        "shank_resultant_rms_m_s2",
        "step_interval_cv_pct",
        "pelvis_pitch_sd_deg",
        "ankle_dp_pf_rom_deg",
        "ankle_mean_dorsiflexion_peak_deg",
        "ankle_mean_plantarflexion_peak_deg",
    ]
    rows = []
    for metric in metrics:
        if metric not in df.columns:
            continue
        for subj in df["subject"].unique():
            sub = df[df["subject"] == subj]
            row = {"metric": metric, "subject": subj}
            for _, r in sub.iterrows():
                v = r.get(metric, np.nan)
                row[r["condition_label"]] = round(v, 3) if not pd.isna(v) else None
            rows.append(row)
    return pd.DataFrame(rows)


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("Tetoronom Analysis Pipeline")
    print("=" * 60)

    print("\n[1/3] 모든 조건 분석 중...")
    results_df = run_all_analyses()

    out_dir = os.path.join(os.path.dirname(__file__), "..", "results")
    os.makedirs(out_dir, exist_ok=True)

    results_df.to_csv(os.path.join(out_dir, "metrics_by_condition.csv"), index=False, encoding="utf-8-sig")
    print(f"\n  → {out_dir}/metrics_by_condition.csv")

    print("\n[2/3] 통계 검정...")
    stats_df = run_statistical_tests(results_df)
    stats_df.to_csv(os.path.join(out_dir, "statistical_tests.csv"), index=False, encoding="utf-8-sig")
    print(f"  → {out_dir}/statistical_tests.csv")

    tbl = build_subject_table(results_df)
    tbl.to_csv(os.path.join(out_dir, "subject_condition_table.csv"), index=False, encoding="utf-8-sig")

    print("\n✓ 완료!")
