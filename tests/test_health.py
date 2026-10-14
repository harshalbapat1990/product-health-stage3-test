import pytest

from src.health import (
    HealthMetrics,
    calculate_health_score,
    classify_health,
)


def test_healthy_project():
    metrics = HealthMetrics(
        build_success_rate=1.0,
        test_pass_rate=1.0,
        open_bug_count=0,
    )

    assert calculate_health_score(metrics) == 100.0


def test_project_with_open_bugs():
    metrics = HealthMetrics(
        build_success_rate=1.0,
        test_pass_rate=1.0,
        open_bug_count=3,
    )

    assert calculate_health_score(metrics) == 94.0


def test_health_classification():
    assert classify_health(90) == "healthy"
    assert classify_health(70) == "warning"
    assert classify_health(40) == "critical"


def test_invalid_health_score():
    with pytest.raises(ValueError):
        classify_health(120)


def test_negative_bug_count_does_not_increase_score():
    metrics = HealthMetrics(
        build_success_rate=1.0,
        test_pass_rate=1.0,
        open_bug_count=-5,
    )

    assert calculate_health_score(metrics) == 100.0

from src.health import health_summary


def test_health_summary():
    result = health_summary(50)

    assert result["score"] == 50
    assert result["status"] == "critical"
    assert result["requires_attention"] is True