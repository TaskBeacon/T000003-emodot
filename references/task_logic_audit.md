# Task Logic Audit: Emotional Dot-Probe Task (EmoDot)

## 1. Paradigm Intent

- Task: `emodot` (emotional dot-probe variant).
- Primary construct: attentional bias indexed by probe RT/accuracy after emotional face-pair cues.
- Manipulated factors:
  - face-pair ordering (`PN`, `NP`, `SN`, `NS`, `NN`)
  - face gender pool (`F`, `M`)
  - probe side (`L`, `R`).
- Dependent measures:
  - probe response key (`target_response`)
  - probe RT (`target_rt`)
  - hit/accuracy (`target_hit`)
  - no-response frequency.
- Key citations:
  - `W4213002248` (MacLeod et al., 1986)
  - `W1989756802` (Bar-Haim et al., 2007)
  - `W2125651023` (Mogg & Bradley, 1998)
  - `W2172073901` (Mogg et al., 2005)

## 2. Block/Trial Workflow

### Block Structure

- Human profile: `3` blocks x `60` trials.
- QA/sim profiles: `1` block x `20` trials.
- Condition generation:
  - Built-in `BlockUnit.generate_conditions(...)` with `task.conditions`.
  - No custom condition generator.
- Runtime-generated trial values:
  - Face asset pair is sampled per condition via `AssetPool` in `src/utils.py`.
  - Probe side is encoded in condition token suffix (`L`/`R`) and extracted in `assign_stim_from_condition(...)`.
  - Asset draw order is deterministic within session due `AssetPool(seed=settings.overall_seed)`.

### Trial State Machine

1. `pre_face_fixation`
- Onset trigger: `fixation_onset`.
- Stimuli: `fixation`.
- Valid keys: task response keys are present in context metadata, but no response capture in this stage.
- Timeout behavior: fixed/jittered fixation duration.
- Next state: `face_pair_preview`.

2. `face_pair_preview`
- Onset trigger: `{condition_id}_cue_onset`.
- Stimuli: left/right face images rebuilt from selected BMP assets.
- Valid keys: none captured.
- Timeout behavior: `cue_duration`.
- Next state: `inter_stimulus_interval`.

3. `inter_stimulus_interval`
- Onset trigger: none mapped explicitly.
- Stimuli: `fixation`.
- Valid keys: none captured.
- Timeout behavior: `interval_duration`.
- Next state: `dot_probe_response`.

4. `dot_probe_response`
- Onset trigger: `{condition_id}_target_onset`.
- Stimuli: `left_target` or `right_target`.
- Valid keys: `left_key`, `right_key`.
- Response triggers: `key_press`.
- Timeout trigger: `no_response`.
- Next state: trial end.

## 3. Condition Semantics

For each condition token (`{emotion}_{gender}_{target_side}`):

- Emotion order code:
  - `PN`: positive-left, neutral-right
  - `NP`: neutral-left, positive-right
  - `SN`: sad-left, neutral-right
  - `NS`: neutral-left, sad-right
  - `NN`: neutral-left, neutral-right
- Gender code:
  - `F` uses female face pools (`P_F`, `N_F`, `S_F`)
  - `M` uses male face pools (`P_M`, `N_M`, `S_M`)
- Target side code:
  - `L` -> probe on left, correct key = `left_key`
  - `R` -> probe on right, correct key = `right_key`.

Participant-facing text/stimulus source:

- Text source: `config/*.yaml -> stimuli.instruction_text`, `block_break`, `good_bye`.
- Why appropriate: centralizes participant wording and enables audit/review without code edits.
- Localization strategy: swap language in config stimuli while keeping `run_trial.py` logic unchanged.

## 4. Response and Scoring Rules

- Response mapping:
  - left probe -> `left_key` (default `f`)
  - right probe -> `right_key` (default `j`).
- Response key source: config (`task.left_key`, `task.right_key`, `task.key_list`).
- Missing-response policy:
  - if no response before `target_duration`, timeout trigger `no_response` is emitted.
- Correctness logic:
  - `capture_response(..., correct_keys=correct_key)` computes `target_hit`.
- Reward/penalty updates:
  - none; this task is accuracy/RT-based.
- Running metrics:
  - `main.py` computes block hit-rate summary for break screen display.

## 5. Stimulus Layout Plan

- Screen: fixation
  - Stimulus IDs: `fixation`
  - Position: center `(0, 0)`.
- Screen: face_pair_preview
  - Stimulus IDs: `left_stim`, `right_stim`
  - Positions: approximately `(-4.5, 0)` and `(4.5, 0)` deg
  - Size: approximately `(4.5, 5)` deg each.
- Screen: dot_probe_response
  - Stimulus IDs: `left_target` or `right_target`
  - Positions: approximately `(-4, 0)` or `(4, 0)` deg.
- Screen: text envelope
  - IDs: `instruction_text`, `block_break`, `good_bye`
  - Config-defined textbox/text formatting.

## 6. Trigger Plan

Stage-level triggers:

- `exp_onset`, `exp_end`, `block_onset`, `block_end`, `fixation_onset`, `key_press`, `no_response`.

Condition-level triggers:

- Each condition has paired cue/target onset triggers:
  - example: `PN_F_L_cue_onset`, `PN_F_L_target_onset`
  - ... through `NN_M_R_cue_onset`, `NN_M_R_target_onset`.

## 7. Architecture Decisions (Auditability)

- `main.py` uses one mode-aware flow for human/qa/sim.
- Task-specific helpers in `src/utils.py`:
  - `AssetPool` controls deterministic face sampling.
  - `assign_stim_from_condition` decodes condition token to concrete stimuli.
- Custom controller: no separate controller class; `BlockUnit` + helper functions are used.
- PsyFlow-native path sufficiency: built-in `BlockUnit` and `StimUnit` handle condition scheduling and response capture cleanly.
- Legacy compatibility branch: none explicit.

## 8. Inference Log

- Decision: include `NN` neutral-neutral conditions in addition to emotion-neutral contrasts.
  - Why inferred: variant design extends beyond minimal threat-neutral pairings.
  - Rationale: improves baseline/control contrasts in multi-emotion studies.

- Decision: use 180 human trials with 20-condition token space.
  - Why inferred: reliability concerns in dot-probe RT metrics often motivate larger samples.
  - Rationale: aligns with reliability discussion (`W2768274310`) while preserving balanced condition coverage.

- Decision: use positive/sad/neutral pools instead of only threat-neutral pools.
  - Why inferred: task variant targets broader emotional bias profile.
  - Rationale: compatible with face-based dot-probe family but should be explicitly justified in reporting.
