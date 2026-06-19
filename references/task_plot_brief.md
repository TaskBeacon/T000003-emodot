# Task Plot Brief

## Evidence Sources

- `README.md`
- `main.py`
- `config/config.yaml`
- `src/run_trial.py`
- `src/utils.py`

## Header

- Title: Emotional Dot-Probe Task (EmoDot)
- Construct: attentional bias / emotion

## Participant-Visible Flow

- Participants see fixation, a face pair, a fixation interval, then a dot probe.
- Probe side determines response key: `f` for left dot and `j` for right dot.
- Emotion-pair variants include positive-neutral, sad-neutral, and neutral-neutral trials.
- Face side and gender pool vary by condition token.

## Rows

- Positive-Neutral: representative PN / NP trials; positive and neutral faces swap left/right.
- Sad-Neutral: representative SN / NS trials; sad and neutral faces swap left/right.
- Neutral-Neutral: representative NN trials; both faces are neutral.

## Timings

- Fixation: 0.8-1.0 s.
- Face pair: 0.5 s.
- Inter-stimulus interval: 0.4-0.6 s.
- Dot probe response window: up to 1.0 s.

## Rendering Notes

- Use schematic face icons only, not realistic people or source photos.
- Show left/right probe mapping in the final screen.
- The generated raw image must contain only timeline content below a blank header band.
- The final title, `Construct: attentional bias / emotion` subtitle, and TaskBeacon logo are added by post-processing.
