# Task Plot Review

Review checklist source: `E:/Taskbeacon/skills/task-plot/references/review_checklist.md`.

Generated image:
- `E:/Taskbeacon/T000003-emodot/task_flow.png`

## Evidence Match

- Pass: task is labeled as Emotional Dot-Probe Task (EmoDot).
- Pass: representative rows cover the configured emotion-pair families: Positive-Neutral (`PN` / `NP`), Sad-Neutral (`SN` / `NS`), and Neutral-Neutral (`NN`).
- Pass: row notes preserve the female/male gender-pool variants without expanding all 20 condition tokens.
- Pass: phase order matches `src/run_trial.py`: fixation, face-pair preview, inter-stimulus interval, dot-probe response.
- Pass: timing labels match config: 0.8-1.0 s fixation, 0.5 s face pair, 0.4-0.6 s ISI, and up to 1.0 s probe response.
- Pass: response mapping is correct: left dot uses `f`, right dot uses `j`.

## Visual Quality

- Pass: text is readable at normal preview size.
- Pass: rows and arrows clearly show temporal order.
- Pass: schematic face icons are used instead of realistic or copyrighted face photos.
- Pass: gray screen boxes, row separators, and restrained condition colors match the TaskBeacon figure style.
- Pass: the image model did not generate its own logo, watermark, or brand text.
- Pass: the fixed TaskBeacon logo lockup was applied in post-processing and appears borderless in the top-right corner without overlapping timeline content.
- Pass: README embeds `![Task Flow](task_flow.png)` under `## 2. Task Flow`.

## Decision

Accepted first generation from the upgraded `task-plot` skill template and fixed logo overlay workflow. No regeneration required.
