# EmoDot Assets

## Asset Policy

The committed BMP files are generated schematic face assets designed for the
TaskBeacon EmoDot implementation. They provide concrete positive, sad, and
neutral face-expression categories while avoiding restricted third-party face
image databases.

## Filename Contract

The task loader groups BMP files by filename prefix:

- `HF*` -> positive female
- `HM*` -> positive male
- `NEF*` -> neutral female
- `NEM*` -> neutral male
- `SAF*` -> sad female
- `SAM*` -> sad male

Keep at least one BMP per prefix so all configured conditions can run.

## Replacing With Study-Specific Stimuli

1. Copy approved study stimuli into this folder with the same prefix scheme.
2. Keep `.bmp` extension, or update `src/utils.py` if using a different format.
3. Re-run the task standard check, TAPS validation, QA, and simulations.

## Important

The generated assets are suitable for open, reproducible task execution and
pipeline validation. Studies requiring validated affective face databases should
replace them with approved materials and document that source in `references/`.
