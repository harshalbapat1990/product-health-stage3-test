"""Entry point for the Product Health Sandbox."""

from src.health import HealthMetrics, calculate_health_score, classify_health


def get_project_health() -> dict:
    """Return a sample project health report."""

    metrics = HealthMetrics(
        build_success_rate=0.95,
        test_pass_rate=0.90,
        open_bug_count=3,
    )

    score = calculate_health_score(metrics)

    return {
        "project": "Product Health Sandbox",
        "score": score,
        "status": classify_health(score),
    }


if __name__ == "__main__":
    print(get_project_health())

def get_project_metadata() -> dict:
    """Return representative project metadata."""

    return {
        "team": "Platform Engineering",
        "environment": "sandbox",
        "criticality": "medium",
    }