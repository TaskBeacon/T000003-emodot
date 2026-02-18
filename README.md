# Emotional Dot-Probe Task (EmoDot)

![Maturity: piloted](https://img.shields.io/badge/Maturity-piloted-16a34a?style=flat-square&labelColor=111827)

| Field | Value |
|---|---|
| Name | Emotional Dot-Probe Task (EmoDot) |
| Version | v1.1.0 |
| URL / Repository | https://github.com/TaskBeacon/T000003-emodot |
| Short Description | Emotional/neutral face-pair dot-probe task for attentional bias and EEG |
| Created By | Zhipeng Cao (zhipeng30@foxmail.com) |
| Date Updated | 2026-02-17 |
| PsyFlow Version | 0.1.9 |
| PsychoPy Version | 2025.1.1 |
| Modality | Behavior/EEG |
| Language | Chinese |
| Voice Name | zh-CN-YunyangNeural |

## 1. Task Overview

EmoDot presents face pairs followed by a left/right dot target.
Participants respond with `f/j` to indicate target side.

## 2. Task Flow

### Block-Level Flow

- Load config, runtime mode, triggers, window, and stimuli.
- Present instructions, then run block/trial loops from `main.py`.
- Save behavioral outputs and close runtime resources.

### Trial-Level Flow

- `pre_face_fixation`: fixation onset.
- `face_pair_preview`: emotional/neutral face pair display.
- `dot_probe_response`: dot-probe response window with key capture.

## Runtime Modes

- Human (default): `python main.py`
- QA: `python main.py qa --config config/config_qa.yaml`
- Scripted sim: `python main.py sim --config config/config_scripted_sim.yaml`
- Sampler sim: `python main.py sim --config config/config_sampler_sim.yaml`

## 3. Configuration Summary

- `config/config.yaml`: base human run profile
- `config/config_qa.yaml`: QA/dev profile (20-trial smoke run)
- `config/config_scripted_sim.yaml`: scripted simulation profile
- `config/config_sampler_sim.yaml`: sampler simulation profile

## Assets and Copyright Workaround

Original emotional face stimuli are not committed because of copyright constraints.
This repo includes placeholder BMP assets for QA/sim/contract validation only.

See `assets/README.md` for:
- placeholder naming contract (`HF*`, `HM*`, `NEF*`, `NEM*`, `SAF*`, `SAM*`)
- how to replace placeholders with licensed task stimuli
- expected path/location requirements

## Outputs

- Human: `outputs/human/`
- QA: `outputs/qa/`
- Scripted sim: `outputs/sim/`
- Sampler sim: `outputs/sim_sampler/`

## Task Notes

- Trigger config uses structured schema: `triggers.map/driver/policy/timing`.
- Trial responder context is wired in `src/run_trial.py` via `set_trial_context(...)`.
- Task-specific sampler is in `responders/task_sampler.py`.

### Runtime Context Phases
| Phase Label | Meaning |
|---|---|
| `pre_face_fixation` | pre face fixation stage in `src/run_trial.py` responder context. |
| `face_pair_preview` | face pair preview stage in `src/run_trial.py` responder context. |
| `dot_probe_response` | dot probe response stage in `src/run_trial.py` responder context. |

## 4. Methods (for academic publication)

Participants view emotional/neutral face pairs followed by a lateralized dot probe and respond with `f/j` to indicate probe side. Each trial uses a fixation stage, a face-pair preview stage, and a response stage for probe discrimination. The paradigm targets attentional bias quantification under controlled visual timing and trigger-synchronized execution.

