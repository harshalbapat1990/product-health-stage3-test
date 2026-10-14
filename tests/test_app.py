from src.app import get_project_health


def test_project_health_report():
    report = get_project_health()

    assert report["project"] == "Product Health Sandbox"
    assert 0 <= report["score"] <= 100
    assert report["status"] in {"healthy", "warning", "critical"}


def test_project_health_has_expected_fields():
    report = get_project_health()

    assert set(report.keys()) == {"project", "score", "status"}