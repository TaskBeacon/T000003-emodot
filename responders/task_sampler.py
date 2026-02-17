from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from psyflow.sim.contracts import Action, Observation, SessionInfo


@dataclass
class TaskSamplerResponder:
    continue_key: str = "space"
    key_left: str = "f"
    key_right: str = "j"
    p_correct: float = 0.9
    rt_mean_s: float = 0.3
    rt_sd_s: float = 0.05
    rt_min_s: float = 0.12

    def __post_init__(self) -> None:
        self._rng: Any = None
        self.p_correct = max(0.0, min(1.0, float(self.p_correct)))
        self.rt_mean_s = float(self.rt_mean_s)
        self.rt_sd_s = max(1e-6, float(self.rt_sd_s))
        self.rt_min_s = max(0.01, float(self.rt_min_s))

    def start_session(self, session: SessionInfo, rng: Any) -> None:
        self._rng = rng

    def on_feedback(self, fb: Any) -> None:
        return None

    def end_session(self) -> None:
        return None

    def _sample_rt(self) -> float:
        if self._rng is None:
            return self.rt_mean_s
        return max(self.rt_min_s, float(self._rng.normal(self.rt_mean_s, self.rt_sd_s)))

    def act(self, obs: Observation) -> Action:
        valid_keys = list(obs.valid_keys or [])
        phase = str(obs.phase or "").strip().lower()

        if not valid_keys:
            return Action(key=None, rt_s=None, meta={"source": "emodot_sampler", "reason": "no_valid_keys"})

        if phase in {"instruction_text", "block_feedback", "goodbye", "instruction", "block"}:
            key = self.continue_key if self.continue_key in valid_keys else valid_keys[0]
            return Action(key=key, rt_s=0.25, meta={"source": "emodot_sampler", "outcome": "continue"})

        if phase != "target":
            return Action(key=None, rt_s=None, meta={"source": "emodot_sampler", "outcome": "non_target"})

        factors = dict(obs.task_factors or {})
        target_pos = str(factors.get("target_position", "")).strip().lower()
        if target_pos not in {"left", "right"}:
            cond = str(obs.condition_id or "").upper()
            if cond.endswith("_L"):
                target_pos = "left"
            elif cond.endswith("_R"):
                target_pos = "right"

        expected = self.key_left if target_pos == "left" else self.key_right
        if expected not in valid_keys:
            expected = valid_keys[0]
        wrong = self.key_right if expected == self.key_left else self.key_left
        if wrong not in valid_keys:
            wrong = valid_keys[0]

        if self._rng is not None and float(self._rng.random()) > self.p_correct:
            return Action(key=wrong, rt_s=self._sample_rt(), meta={"source": "emodot_sampler", "outcome": "error"})

        return Action(key=expected, rt_s=self._sample_rt(), meta={"source": "emodot_sampler", "outcome": "correct"})
