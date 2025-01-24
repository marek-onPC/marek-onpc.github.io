from datetime import datetime, timedelta, timezone
from unittest import mock
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app
from schemas import LoginToken, Token

client = TestClient(app)

EXIRY = datetime.now(timezone.utc) + timedelta(days=0, hours=8)


@pytest.mark.parametrize(
    "payload, token, expected_token",
    [
        pytest.param(
            {"username": "user@test.com", "password": "password"},
            LoginToken(token=Token("xxx.yyy.zzz"), expiry=EXIRY.timestamp()),
            {"token": "xxx.yyy.zzz", "expiry": EXIRY.timestamp()},
        ),
    ],
)
@mock.patch("domain.login_domain.login")
def test_login(
    mock_domain_login: MagicMock, payload: dict, token: LoginToken, expected_token: dict
) -> None:
    mock_domain_login.return_value = token

    response = client.post("/api/login", json=payload)
    assert response.status_code == 200
    assert response.json() == expected_token


@pytest.mark.parametrize(
    "payload, expected_error",
    [
        pytest.param(
            {"password": "password"},
            {
                "detail": [
                    {
                        "input": None,
                        "loc": [
                            "body",
                            "username",
                        ],
                        "msg": "Field required",
                        "type": "missing",
                    },
                ],
            },
        ),
        pytest.param(
            {"username": "user@test.com"},
            {
                "detail": [
                    {
                        "input": None,
                        "loc": [
                            "body",
                            "password",
                        ],
                        "msg": "Field required",
                        "type": "missing",
                    },
                ],
            },
        ),
    ],
)
def test_login__errors(payload: dict, expected_error: dict) -> None:
    response = client.post("/api/login", json=payload)
    assert response.status_code == 422
    assert response.json() == expected_error
