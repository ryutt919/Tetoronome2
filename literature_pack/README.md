# Tetoronome Literature Pack

This folder is organized around the analysis goal: support, correct, or reject the current result interpretations using factual prior literature.

## Files

- `claim_audit.md`: Existing interpretation claims audited against the current results and literature.
- `evidence_matrix.csv`: Result-by-result mapping from our finding to corrected interpretation and supporting paper.
- `interpretation_directions.md`: Manuscript-ready interpretation directions with "avoid" phrases.
- `unsupported_claims.md`: Claims that should be removed or downshifted.
- `download_manifest.csv`: Official source URLs, local PDF status, and download notes.
- `completion_audit.md`: Requirement-by-requirement verification of this pack.

## Folder logic

- `01_direct_support`: papers directly or near-directly supporting result interpretation.
- `02_mechanistic_support`: papers supporting mechanism but not directly measuring this exact result.
- `03_contrast_evidence`: papers showing why our result differs from prior expectations or why old claims must be downshifted.
- `04_methods_imu_proxy`: IMU/proxy-method papers and notes.
- `99_link_only`: papers retained as official links because PDF download was blocked, paywalled, or not needed for a direct claim.

## Current downloaded PDFs

- `03_contrast_evidence/heiderscheit_2011_step_rate_running.pdf`
- `02_mechanistic_support/yong_2014_forefoot_rearfoot_emg.pdf`

Other papers remain link-only in `download_manifest.csv` where official download failed or where the paper should only be used as indirect/caution evidence. For those sources, `.url` shortcut files are placed in the relevant folders so they can be opened directly.

## Important integrity note

Two direct PMC PDF attempts returned small HTML challenge pages rather than real PDFs. Those invalid files were removed. The pack intentionally keeps those sources as official links instead of pretending they were downloaded.
