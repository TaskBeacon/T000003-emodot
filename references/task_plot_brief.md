# Task Plot Brief

Task: Emotional Dot-Probe Task (EmoDot)

Goal measured: attentional bias to emotional face cues.

Primary evidence:
- `README.md`: task overview, flow, timing, and response mapping.
- `config/config.yaml`: condition list, stimuli, keys, timing, and block/trial counts.
- `src/run_trial.py`: participant-visible trial sequence and response scoring.
- `src/utils.py`: condition token decoding into face-pair emotion order, gender pool, and target side.

Conditions:
- Positive-neutral face pair: `PN` / `NP`; positive face can appear left or right, neutral face on the other side.
- Sad-neutral face pair: `SN` / `NS`; sad face can appear left or right, neutral face on the other side.
- Neutral-neutral face pair: `NN`; neutral faces appear on both sides as a control condition.
- Gender pools are female (`F`) and male (`M`) variants.
- Probe side is encoded by `L` or `R`; left probe uses key `f`, right probe uses key `j`.

Trial phases:
- Fixation: `+`, jittered 0.8-1.0 s.
- Face pair preview: two schematic faces shown left and right, 0.5 s.
- Inter-stimulus interval: `+`, jittered 0.4-0.6 s.
- Dot probe response: white dot/circle appears left or right, up to 1.0 s; press `f` for left, `j` for right.

Block context:
- Human profile: 3 blocks, 60 trials per block, 180 trials total.
- Conditions span 20 tokens across emotion order, gender pool, and probe side.

Image simplification:
- Use three representative rows: Positive-Neutral, Sad-Neutral, Neutral-Neutral.
- Show left/right probe variants inside the final probe-response screen rather than drawing every condition token.
- Use schematic face icons, not realistic or copyrighted faces.
