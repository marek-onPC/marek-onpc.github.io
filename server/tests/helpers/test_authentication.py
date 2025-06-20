import pytest

from helpers.authentication import Authentication
from schemas import Password, Username

authentication = Authentication()


@pytest.mark.parametrize(
    "password",
    [Password("uhhs6hsbja"), Password("AHg%&JNhsjkdnh&89sh"), Password("7262hskdd")],
)
def test_hash_and_verify_password(password: Password) -> None:
    hashed_password = authentication.hash_password(password)

    assert authentication.verify_password(password, hashed_password) is True


@pytest.mark.parametrize(
    "username",
    [Username("new0user"), Username("user@name.com"), Username("test56@user.com")],
)
def test_encode_and_decode_jwt(username: Username) -> None:
    jwt = authentication.encode_jwt(username)
    decoded_jwt = authentication.decode_jwt(jwt.access_token)

    assert decoded_jwt == username
