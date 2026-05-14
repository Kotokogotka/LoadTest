import json
from pathlib import Path

from locust import LoadTestShape

from locustfiles.medium import MediumLoadUser  # noqa: F401


def _count_available_users() -> int:
    users_path = Path(__file__).resolve().parent.parent / "secrets" / "test_users.json"
    raw_users = json.loads(users_path.read_text(encoding="utf-8"))
    return len(raw_users)


class RampUntilDegradation(LoadTestShape):
    start_users = 10
    step_users = 5
    step_duration_seconds = 5 * 60
    spawn_rate = 1
    max_users = _count_available_users()

    warmup_seconds = 2 * 60
    min_requests_before_stop = 200
    stop_p95_ms = 3000
    stop_fail_ratio = 0.10
    consecutive_breach_limit = 15

    def __init__(self) -> None:
        super().__init__()
        self._breach_count = 0
        self._last_stage = -1

    def _current_target_users(self) -> int:
        stage = int(self.get_run_time() // self.step_duration_seconds)
        target = self.start_users + stage * self.step_users
        return min(target, self.max_users)

    def _is_degraded(self) -> tuple[bool, str | None]:
        total = self.runner.stats.total
        total_requests = self.runner.stats.num_requests

        if self.get_run_time() < self.warmup_seconds or total_requests < self.min_requests_before_stop:
            self._breach_count = 0
            return False, None

        p95 = total.get_response_time_percentile(0.95)
        fail_ratio = total.fail_ratio

        if p95 >= self.stop_p95_ms or fail_ratio >= self.stop_fail_ratio:
            self._breach_count += 1
        else:
            self._breach_count = 0

        if self._breach_count >= self.consecutive_breach_limit:
            reason = (
                f"Auto-stop: p95={p95}ms, fail_ratio={fail_ratio:.2%}, "
                f"users={self.get_current_user_count()}, requests={total_requests}"
            )
            return True, reason

        return False, None

    def tick(self):
        if self.runner is None:
            return None

        should_stop, reason = self._is_degraded()
        if should_stop:
            print(reason)
            return None

        stage = int(self.get_run_time() // self.step_duration_seconds)
        if stage != self._last_stage:
            self._last_stage = stage
            print(
                f"Stage {stage + 1}: target_users={self._current_target_users()}, "
                f"spawn_rate={self.spawn_rate}/s"
            )

        return self._current_target_users(), self.spawn_rate
