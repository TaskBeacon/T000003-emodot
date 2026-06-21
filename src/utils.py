import os
import random
from collections import defaultdict
from typing import Any, Dict, List


class AssetPool:
    def __init__(self, stim_list: Dict[str, List[str]], seed: int = 42):
        self.rng = random.Random(int(seed))
        self.original = stim_list
        self.pool = {k: [] for k in stim_list}  # working pools start empty

    def draw(self, key: str) -> str:
        """Draw one stimulus from the specified key pool."""
        if not self.pool[key]:
            self.pool[key] = self.original[key][:]
            self.rng.shuffle(self.pool[key])
        return self.pool[key].pop()


def get_stim_list_from_assets(asset_dir: str = "./assets") -> dict:
    stim_list = defaultdict(list)
    for file in os.listdir(asset_dir):
        if file.lower().endswith(".bmp"):
            name = file.upper()
            if name.startswith("HF"):
                stim_list["P_F"].append(file)
            elif name.startswith("HM"):
                stim_list["P_M"].append(file)
            elif name.startswith("NEF"):
                stim_list["N_F"].append(file)
            elif name.startswith("NEM"):
                stim_list["N_M"].append(file)
            elif name.startswith("SAF"):
                stim_list["S_F"].append(file)
            elif name.startswith("SAM"):
                stim_list["S_M"].append(file)
    return dict(stim_list)


def assign_stim_from_condition(condition: str, asset_pool: AssetPool) -> dict:
    """
    Assigns left/right faces to a given condition label using the AssetPool.

    Parameters:
    -----------
    condition : str
        A condition label, e.g., 'PN_F_L', 'SN_M_R', etc.
    asset_pool : AssetPool
        An instance of the AssetPool class with loaded stimuli.

    Returns:
    --------
    dict with keys: condition, left_stim, right_stim, target_position
    """
    emotion, gender, target = condition.split("_")

    if emotion == "PN":
        left_key, right_key = "P_" + gender, "N_" + gender
    elif emotion == "NP":
        left_key, right_key = "N_" + gender, "P_" + gender
    elif emotion == "SN":
        left_key, right_key = "S_" + gender, "N_" + gender
    elif emotion == "NS":
        left_key, right_key = "N_" + gender, "S_" + gender
    elif emotion == "NN":
        left_key = right_key = "N_" + gender
    else:
        raise ValueError(f"Unknown emotion code: {emotion}")

    left_stim = asset_pool.draw(left_key)
    right_stim = asset_pool.draw(right_key)

    return {
        "condition": condition,
        "left_stim": left_stim,
        "right_stim": right_stim,
        "target_position": "left" if target == "L" else "right",
    }


def generate_emodot_conditions(
    n_trials: int,
    condition_labels: list[Any] | None = None,
    *,
    seed: int = 0,
    stim_list: dict[str, list[str]] | None = None,
) -> list[tuple[str, str, str, str]]:
    """Build a block schedule with concrete face assets assigned."""
    labels = [str(label) for label in (condition_labels or [])]
    if not labels:
        raise ValueError("EmoDot condition_labels cannot be empty.")
    if not stim_list:
        raise ValueError("EmoDot condition generation requires a stim_list.")

    rng = random.Random(int(seed))
    scheduled_labels: list[str] = []
    while len(scheduled_labels) < int(n_trials):
        scheduled_labels.extend(labels)
    scheduled_labels = scheduled_labels[: int(n_trials)]
    rng.shuffle(scheduled_labels)

    asset_pool = AssetPool(stim_list, seed=int(seed))
    scheduled: list[tuple[str, str, str, str]] = []
    for condition_id in scheduled_labels:
        trial_info = assign_stim_from_condition(condition_id, asset_pool)
        scheduled.append(
            (
                str(trial_info["condition"]),
                str(trial_info["left_stim"]),
                str(trial_info["right_stim"]),
                str(trial_info["target_position"]),
            )
        )
    return scheduled


def emodot_condition_to_trial_info(condition: Any) -> dict[str, str]:
    """Decode a scheduled EmoDot condition tuple."""
    if isinstance(condition, (tuple, list)) and len(condition) >= 4:
        condition_id, left_stim, right_stim, target_position = condition[:4]
        return {
            "condition": str(condition_id),
            "left_stim": str(left_stim),
            "right_stim": str(right_stim),
            "target_position": str(target_position),
        }
    raise ValueError(f"Expected scheduled EmoDot condition tuple, got {condition!r}")
