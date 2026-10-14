"""Simple project health calculations for sandbox testing."""

from dataclasses import dataclass


@dataclass
class HealthMetrics:
    """Metrics used to calculate a project health score."""

    build_success_rate: float
    test_pass_rate: float
    open_bug_count: int


def calculate_health_score(metrics: HealthMetrics) -> float:
    """
    Calculate a score between 0 and 100.

    Build success contributes 40%.
    Test pass rate contributes 40%.
    Open bugs contribute up to 20%.
    """

    build_score = _normalize_rate(metrics.build_success_rate) * 40
    test_score = _normalize_rate(metrics.test_pass_rate) * 40

    bug_score = max(0, 20 - max(0, metrics.open_bug_count) * 2)

    return round(build_score + test_score + bug_score, 2)


def _normalize_rate(rate: float) -> float:
    """Normalize a rate to the interval [0, 1]."""

    return min(1.0, max(0.0, rate))


def classify_health(score: float) -> str:
    """Return a label for a health score."""

    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 80:
        return "healthy"

    if score >= 60:
        return "warning"

    return "critical"