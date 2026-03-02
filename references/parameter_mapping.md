# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| `condition_tokens` | `task.conditions` | 20 tokens: emotion-order (`PN/NP/SN/NS/NN`) x gender (`F/M`) x target side (`L/R`) | `W4213002248` | Dot-probe core contrast requires emotion-pair exposure followed by lateral probe discrimination. | `adapted` | Task extends classic threat-neutral mapping to multi-emotion and gender-factorized labels. |
| `trial_count_human` | `task.total_blocks`, `task.trial_per_block`, `task.total_trials` | Human `3 x 60 = 180` | `W2768274310` | Reliability concerns in dot-probe tasks motivate larger trial counts for stable bias indices. | `inferred` | Trial count is higher than many brief clinical variants; document in methods section. |
| `trial_count_qa_sim` | `config_qa/task.total_trials`, `config_scripted_sim/task.total_trials`, `config_sampler_sim/task.total_trials` | QA/sim `20` | `W2768274310` | Validation runs may use reduced counts that are not intended for inferential analysis. | `inferred` | Keep as engineering profile only. |
| `response_mapping` | `task.left_key`, `task.right_key`, `task.key_list` | `left=f`, `right=j` | `W2125651023` | Dot-probe requires explicit left/right probe localization response. | `inferred` | Keys are config-defined and portable across hardware/language contexts. |
| `fixation_duration` | `timing.fixation_duration` | Human `[0.8, 1.0]`; QA/sim `[0.2, 0.3]` | `W2125651023` | Pre-cue fixation stabilizes gaze before face-pair onset. | `adapted` | QA/sim shortened for runtime. |
| `cue_duration` | `timing.cue_duration` | Human `0.5s`; QA/sim `0.15s` | `W2125651023` | Face-pair presentation duration modulates measured attentional bias effects. | `adapted` | Human value aligns with common 500 ms dot-probe variants. |
| `interval_duration` | `timing.interval_duration` | Human `[0.4, 0.6]`; QA/sim `[0.08, 0.12]` | `W2172073901` | Probe-timing window affects observed bias direction/strength. | `adapted` | Inter-stimulus interval is implementation-specific and should be reported. |
| `target_duration` | `timing.target_duration` | Human `1.0s`; QA/sim `0.35s` | `W2125651023` | Bounded probe response window is standard for RT-based bias metrics. | `adapted` | Short QA/sim window is not analysis-grade. |
| `condition_generation` | `main.py -> BlockUnit.generate_conditions()` | Built-in even-weight condition schedule (no explicit weights) | `W1989756802` | Balanced condition coverage is needed for interpretable bias contrasts. | `inferred` | If weighted sampling is introduced later, it should be explicit in config. |
| `asset_sampling` | `src/utils.py -> AssetPool.draw(...)` | Within-category shuffled draw, pool refill when exhausted | `W2172073901` | Repeated face exposure can influence attentional effects; stimulus variation should be controlled. | `inferred` | Current policy reduces immediate repetition but allows reuse after pool exhaustion. |
| `trigger_scheme` | `triggers.map` | Condition-specific `*_cue_onset` and `*_target_onset` plus response/timeout/exp markers | `W4213002248` | Stage-specific event coding is required for ERP/EEG alignment in response-time paradigms. | `inferred` | Trigger taxonomy is implementation-specific but audit-friendly. |
