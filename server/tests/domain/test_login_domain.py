from datetime import datetime, timedelta, timezone
from typing import Any
from unittest import mock

import mongomock
import pytest
from bson import ObjectId
from fastapi import HTTPException
from mongomock import Collection

from domain.login_domain import _bson_user_to_object, get_user, login
from helpers.authentication import Authentication
from schemas import (
    AllowedGrandTypes,
    AuthToken,
    Password,
    PasswordAuthentication,
    RefreshTokenAuthentication,
    User,
    Username,
)

db_name = "DB_NAME"
db_name = "DB_COLL"

authentication = Authentication()
raw_password = "uhhs6hsbja"
hashed_password = authentication.hash_password(Password(raw_password))

# DATABASE MOCK PREPARATION ------------------------------
mock_collection: Collection = (
    mongomock.MongoClient().get_database(db_name).get_collection(db_name)
)
documents = [
    {
        "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
        "user": "user@test.com",
        "password": hashed_password,
    },
]
mock_collection.insert_many(documents)
# END OF DATABASE MOCK PREPARATION -----------------------


def _clear_test_db() -> None:
    mock_collection.delete_many({})
    mock_collection.insert_many(documents)


_clear_test_db()


@pytest.mark.parametrize(
    "bson_user, expected_user_object",
    [
        pytest.param(
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "user": "user@test.com",
                "password": hashed_password,
            },
            User(username="user@test.com", password=hashed_password),
        )
    ],
)
def test_bson_user_to_object(bson_user: Any, expected_user_object: User) -> None:
    result = _bson_user_to_object(bson_user)

    assert result == expected_user_object


@pytest.mark.parametrize(
    "bson_user, expected_error",
    [
        pytest.param(
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "password": hashed_password,
            },
            "user",
        ),
        pytest.param(
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "user": "user@test.com",
            },
            "password",
        ),
    ],
)
def test_bson_user_to_object__errors(bson_user: Any, expected_error: str) -> None:
    with pytest.raises(HTTPException) as error:
        _bson_user_to_object(bson_user)

    assert isinstance(error.value.detail, KeyError)
    assert error.value.status_code == 400
    assert error.value.detail.args[0] == expected_error


@pytest.mark.parametrize(
    "username, expected_user_object",
    [
        pytest.param(
            Username("user@test.com"),
            User(username="user@test.com", password=hashed_password),
        ),
        pytest.param(Username("non_exists@test.com"), None),
    ],
)
@mock.patch("domain.login_domain.db_client", mock_collection)
def test_get_user(username: Username, expected_user_object: User | None) -> None:
    result = get_user(username)

    assert result == expected_user_object


@pytest.mark.parametrize(
    "auth_details, expected_username",
    [
        pytest.param(
            PasswordAuthentication(
                grant_type=AllowedGrandTypes.PASSWORD,
                username=Username("user@test.com"),
                password=raw_password,
            ),
            Username("user@test.com"),
        ),
    ],
)
@mock.patch("domain.login_domain.db_client", mock_collection)
def test_login(
    auth_details: PasswordAuthentication, expected_username: User | None
) -> None:
    expired_token_date = datetime.now(timezone.utc) + timedelta(
        days=0, hours=8, minutes=1
    )
    result = login(auth_details)

    assert isinstance(result, AuthToken)
    assert isinstance(result.access_token, str)
    assert isinstance(result.refresh_token, str)
    assert isinstance(result.token_type, str)
    assert result.expires_in < expired_token_date.timestamp()

    decoded_jwt = authentication.decode_jwt(result.access_token)

    assert decoded_jwt == expected_username


@pytest.mark.parametrize(
    "auth_details, expected_error",
    [
        pytest.param(
            PasswordAuthentication(
                grant_type=AllowedGrandTypes.PASSWORD,
                username=Username("non_exists@test.com"),
                password=raw_password,
            ),
            "Wrong user",
        ),
        pytest.param(
            PasswordAuthentication(
                grant_type=AllowedGrandTypes.PASSWORD,
                username=Username("user@test.com"),
                password="wrong_pass",
            ),
            "Wrong password",
        ),
    ],
)
@mock.patch("domain.login_domain.db_client", mock_collection)
def test_login__erorrs(
    auth_details: PasswordAuthentication, expected_error: str
) -> None:
    with pytest.raises(HTTPException) as error:
        login(auth_details)

    assert error.value.status_code == 401
    assert error.value.detail == expected_error


@pytest.mark.parametrize(
    "auth_details, expected_error",
    [
        pytest.param(
            RefreshTokenAuthentication(
                grant_type=AllowedGrandTypes.REFRESH_TOKEN,
                refresh_token="some_refresh_token",
            ),
            "Refresh token auth is not implemented yet",
        ),
    ],
)
@mock.patch("domain.login_domain.db_client", mock_collection)
def test_login__refresh_token_grant_type_error(
    auth_details: PasswordAuthentication, expected_error: str
) -> None:
    with pytest.raises(HTTPException) as error:
        login(auth_details)

    assert error.value.status_code == 422
    assert error.value.detail == expected_error
