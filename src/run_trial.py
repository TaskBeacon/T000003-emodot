from functools import partial
from pathlib import Path

from psyflow import StimUnit, set_trial_context

from src import assign_stim_from_condition

# trial stages in contract order: cue -> anticipation -> target -> feedback
_TRIAL_COUNTER = 0


def _next_trial_id() -> int:
    global _TRIAL_COUNTER
    _TRIAL_COUNTER += 1
    return _TRIAL_COUNTER


def _deadline_s(value) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, (list, tuple)) and value:
        try:
            return float(max(value))
        except Exception:
            return None
    return None


def run_trial(
    win,
    kb,
    settings,
    condition,
    stim_bank,
    asset_pool,
    trigger_runtime=None,
    block_id=None,
    block_idx=None,
):
    """Run one emotional dot-probe trial."""
    trial_id = _next_trial_id()
    condition_id = str(condition)
    trial_data = {"condition": condition_id}
    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    trial_info = assign_stim_from_condition(condition_id, asset_pool)
    left_asset = str(Path("assets") / trial_info["left_stim"])
    right_asset = str(Path("assets") / trial_info["right_stim"])
    left_stim = stim_bank.rebuild("left_stim", image=left_asset)
    right_stim = stim_bank.rebuild("right_stim", image=right_asset)
    target_position = str(trial_info["target_position"])
    correct_key = settings.left_key if target_position == "left" else settings.right_key

    # cue
    cue_unit = make_unit(unit_label="fixation").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        cue_unit,
        trial_id=trial_id,
        phase="cue",
        deadline_s=_deadline_s(settings.fixation_duration),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "fixation", "block_idx": block_idx},
        stim_id="fixation",
    )
    cue_unit.show(duration=settings.fixation_duration, onset_trigger=settings.triggers.get("fixation_onset")).to_dict(trial_data)

    # anticipation
    anticipation_unit = make_unit(unit_label="cues").add_stim(left_stim).add_stim(right_stim)
    set_trial_context(
        anticipation_unit,
        trial_id=trial_id,
        phase="anticipation",
        deadline_s=_deadline_s(settings.cue_duration),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "face_pair", "block_idx": block_idx},
        stim_id=f"{condition_id}_faces",
        stim_features={"left_asset": left_asset, "right_asset": right_asset},
    )
    anticipation_unit.show(
        duration=settings.cue_duration,
        onset_trigger=settings.triggers.get(f"{condition_id}_cue_onset"),
    ).to_dict(trial_data)

    make_unit(unit_label="interval").add_stim(stim_bank.get("fixation")).show(duration=settings.interval_duration).to_dict(trial_data)

    # target
    target_stim = stim_bank.get(f"{target_position}_target")
    target_unit = make_unit(unit_label="target").add_stim(target_stim)
    set_trial_context(
        target_unit,
        trial_id=trial_id,
        phase="target",
        deadline_s=_deadline_s(settings.target_duration),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=condition_id,
        task_factors={
            "condition": condition_id,
            "stage": "target",
            "target_position": target_position,
            "correct_key": correct_key,
            "block_idx": block_idx,
        },
        stim_id=f"{target_position}_target",
    )
    target_unit.capture_response(
        keys=settings.key_list,
        correct_keys=correct_key,
        duration=settings.target_duration,
        onset_trigger=settings.triggers.get(f"{condition_id}_target_onset"),
        response_trigger=settings.triggers.get("key_press"),
        timeout_trigger=settings.triggers.get("no_response"),
        terminate_on_response=True,
    )
    target_unit.to_dict(trial_data)

    # feedback
    make_unit(unit_label="feedback").show(duration=0.0).to_dict(trial_data)
    return trial_data
