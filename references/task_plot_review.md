# Task Plot Review

Review checklist source: `E:/Taskbeacon/skills/task-plot/references/review_checklist.md`.

## Evidence Match

- Pass: task name matches `Emotional Dot-Probe Task (EmoDot)`.
- Pass: rows match representative Positive-Neutral, Sad-Neutral, and Neutral-Neutral trial families.
- Pass: phase order matches `src/run_trial.py`: fixation, face pair, ISI, dot probe response.
- Pass: timing labels match config: 0.8-1.0 s fixation, 0.5 s face pair, 0.4-0.6 s ISI, up to 1.0 s probe.
- Pass: response mapping is correct: `f` for left dot and `j` for right dot.

## Visual Quality

- Pass: fixed title and `Construct: attentional bias / emotion` subtitle are centered in the header.
- Pass: fixed TaskBeacon logo lockup is borderless in the top-right corner and does not overlap content.
- Pass: face stimuli are schematic icons rather than realistic people or photos.
- Pass: text is readable and no generated extra title, subtitle, logo, watermark, people, or devices are present.
- Pass: `references/task_plot_timeline_raw.png` preserves the generated timeline before header/logo post-processing.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the first image under `## 2. Task Flow` is exactly `![Task Flow](task_flow.png)`.
- Pass: final image is saved at the task root as `task_flow.png`.
