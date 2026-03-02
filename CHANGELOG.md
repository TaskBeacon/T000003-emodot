# CHANGELOG

All notable development changes for T000003-emodot are documented here.

## [1.1.3] - 2026-03-02

### Changed
- Renamed legacy face-pair runtime variable from `anticipation_unit` to `face_pair_unit` in `src/run_trial.py` for paradigm-aligned naming.
- Standardized `README.md` with recommended PsyFlow subsection headings:
  - `### Controller Logic`
  - `### a. Subject Info`
  - `### b. Window Settings`
  - `### c. Stimuli`
  - `### d. Timing`
- Updated task metadata in `taskbeacon.yaml`:
  - release tag `v1.1.3`
  - populated `cognitive_domain`
  - populated literature `evidence`
  - populated `maintainer`

### Removed
- Removed zero-duration terminal `feedback` marker from `src/run_trial.py`; trial now ends after `dot_probe_response`.

## [1.1.2] - 2026-02-23

### Changed
- Removed redundant `_TRIAL_COUNTER` and `_next_trial_id()` manually defined boilerplate in favor of native `psyflow.next_trial_id` synchronization.
- Removed redundant duration resolver (`_deadline_s()`) locally, since duration array parsing is now safely handled natively inside `set_trial_context(...)`.
- Refactored `src/run_trial.py` to maintain decoupled generalized tracking from `psyflow`.

## [1.1.1] - 2026-02-18

### Changed
- Refactored responder context phase names in `src/run_trial.py` to task-specific labels (removed generic MID-style phase naming).
- Updated stage comments in `src/run_trial.py` to phase-aligned labels for cleaner auditability.
- Updated `README.md` to keep runtime phase documentation aligned with the implemented trial context phases.

### Fixed
- Removed legacy stage comment patterns (`cue/anticipation/target/feedback`) from trial runtime code.

## [1.1.0] - 2026-02-17

### Added
- Added mode-aware `main.py` flow for human/qa/sim execution.
- Added split runtime configs:
  - `config/config.yaml`
  - `config/config_qa.yaml`
  - `config/config_scripted_sim.yaml`
  - `config/config_sampler_sim.yaml`
- Added task-local responder scaffold:
  - `responders/__init__.py`
  - `responders/README.md`
  - `responders/task_sampler.py`
- Added `outputs/.gitkeep` and standardized output folder handling.
- Added `assets/README.md` with placeholder asset and replacement guidance.

### Changed
- Refactored `src/run_trial.py` to include `set_trial_context(...)` and standardized stage tokens.
- Kept original trial structure (fixation -> face pair -> interval -> target) while adding simulation-compatible context/logging.
- Upgraded trigger config to structured schema (`triggers.map/driver/policy/timing`).
- Updated `taskbeacon.yaml` to declare contract adoption (`contracts.psyflow_taps: v0.1.0`).
- Updated `.gitignore` for standardized outputs and generated artifacts.
- Updated `README.md` metadata and runtime/config usage.

### Fixed
- Corrected timeout trigger key usage to `no_response` (consistent naming in config and trial code).

### Verified
- `psyflow-validate <task>` passes contract checks.
- `psyflow-qa <task> --config config/config_qa.yaml --no-maturity-update` passes.
- `python main.py sim --config config/config_scripted_sim.yaml` runs and writes sim artifacts.
