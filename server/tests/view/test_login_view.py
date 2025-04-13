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
            {
                "grant_type": "password",
                "username": "user@test.com",
                "password": "password",
            },
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
                        "input": {
                            "password": "password",
                        },
                        "loc": [
                            "body",
                            "grant_type",
                        ],
                        "msg": "Field required",
                        "type": "missing",
                    },
                    {
                        "input": {
                            "password": "password",
                        },
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
                        "input": {
                            "username": "user@test.com",
                        },
                        "loc": [
                            "body",
                            "grant_type",
                        ],
                        "msg": "Field required",
                        "type": "missing",
                    },
                    {
                        "input": {
                            "username": "user@test.com",
                        },
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
        pytest.param(
            {"grant_type": "password"},
            {
                "detail": [
                    {
                        "input": {
                            "grant_type": "password",
                        },
                        "loc": [
                            "body",
                            "username",
                        ],
                        "msg": "Field required",
                        "type": "missing",
                    },
                    {
                        "input": {
                            "grant_type": "password",
                        },
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
