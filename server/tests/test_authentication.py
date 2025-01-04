from datetime import datetime
from unittest import mock
from unittest.mock import Mock
import pytest
from helpers.authentication import Authentication

authentication = Authentication()

@pytest.mark.parametrize(
    "password", [
        "uhhs6hsbja",
        "AHg%&JNhsjkdnh&89sh",
        "7262hskdd"
    ]
)
def test_hash_and_verify_password(password: str) -> None:
    hashed_password = authentication.hash_password(password)

    assert authentication.verify_password(password, hashed_password) == True


@pytest.mark.parametrize(
    "username", [
        "new0user",
        "user@name.com",
        "test56@user.com"
    ]
)
def test_encode_and_decode_jwt(username: str) -> None:
    jwt, _ = authentication.encode_jwt(username)
    decoded_jwt = authentication.decode_jwt(jwt)

    assert decoded_jwt == username
