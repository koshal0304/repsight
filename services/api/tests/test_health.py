"""E0-T03: the API answers the ALB health checks (02 §8.5.1)."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.mark.parametrize("path", ["/healthz", "/readyz"])
def test_health_checks_return_200(path: str) -> None:
    response = TestClient(app).get(path)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
