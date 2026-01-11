from datetime import datetime, timedelta, timezone
from unittest import mock
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app
from schemas import AuthToken, EventTypes

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
            AuthToken(
                access_token="xxx.yyy.zzz",
                token_type="Bearer",
                expires_in=EXIRY.timestamp().as_integer_ratio()[0],
                refresh_token="xxx.yyy.zzz",
            ),
            {
                "access_token": "xxx.yyy.zzz",
                "token_type": "Bearer",
                "expires_in": EXIRY.timestamp().as_integer_ratio()[0],
                "refresh_token": "xxx.yyy.zzz",
            },
        ),
    ],
)
@mock.patch("domain.login_domain.get_token")
@mock.patch("view.login_view.send_log_event")
def test_login(
    mock_send_log_event: MagicMock,
    mock_domain_login: MagicMock,
    payload: dict,
    token: AuthToken,
    expected_token: dict,
) -> None:
    mock_send_log_event.return_value = None
    mock_domain_login.return_value = token

    response = client.post("/api/login", json=payload)
    assert response.status_code == 200
    assert response.json() == expected_token

    assert mock_send_log_event.call_count == 2
    mock_send_log_event.assert_has_calls(
        [
            mock.call(
                event_type=EventTypes.LOGIN_OPERATION,
                message="Login attempt via password",
                user="user@test.com",
                context={"status": "started", "grant_type": "password"},
            ),
            mock.call(
                event_type=EventTypes.LOGIN_OPERATION,
                message="Login attempt via password",
                user="user@test.com",
                context={"status": "successful", "grant_type": "password"},
            ),
        ]
    )


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
                            "PasswordAuthentication",
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
                            "PasswordAuthentication",
                            "username",
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
                            "RefreshTokenAuthentication",
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
                            "RefreshTokenAuthentication",
                            "refresh_token",
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
                            "PasswordAuthentication",
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
                            "PasswordAuthentication",
                            "password",
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
                            "RefreshTokenAuthentication",
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
                            "RefreshTokenAuthentication",
                            "refresh_token",
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
                            "PasswordAuthentication",
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
                            "PasswordAuthentication",
                            "password",
                        ],
                        "msg": "Field required",
                        "type": "missing",
                    },
                    {
                        "ctx": {
                            "expected": "<AllowedGrandTypes.REFRESH_TOKEN: 'refresh_token'>",
                        },
                        "input": "password",
                        "loc": [
                            "body",
                            "RefreshTokenAuthentication",
                            "grant_type",
                        ],
                        "msg": "Input should be <AllowedGrandTypes.REFRESH_TOKEN: "
                        "'refresh_token'>",
                        "type": "literal_error",
                    },
                    {
                        "input": {
                            "grant_type": "password",
                        },
                        "loc": [
                            "body",
                            "RefreshTokenAuthentication",
                            "refresh_token",
                        ],
                        "msg": "Field required",
                        "type": "missing",
                    },
                ],
            },
        ),
    ],
)
@mock.patch("view.login_view.send_log_event")
def test_login__errors(
    mock_send_log_event: MagicMock, payload: dict, expected_error: dict
) -> None:
    mock_send_log_event.return_value = None

    response = client.post("/api/login", json=payload)
    assert response.status_code == 422
    assert response.json() == expected_error

    assert mock_send_log_event.call_count == 0
