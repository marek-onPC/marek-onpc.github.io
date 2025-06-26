import logging
import os
from typing import Any, Optional

from dotenv import load_dotenv
from fastapi import HTTPException

from helpers.authentication import Authentication, get_username_from_token
from helpers.db_client import DatabaseClient
from schemas import (
    AuthenticationDetails,
    AuthToken,
    PasswordAuthentication,
    RefreshTokenAuthentication,
    User,
    Username,
)

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_USERS"]
db_client = DatabaseClient(db_uri, db_name).connection()[db_collection_name]
authentication = Authentication()


def _bson_user_to_object(bson_document: Any) -> User:
    try:
        username = bson_document["user"]
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=400, detail=e)

    try:
        password = bson_document["password"]
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=400, detail=e)

    return User(username=username, password=password)


def get_user(username: Username) -> Optional[User]:
    user = db_client.find_one({"user": username})

    return _bson_user_to_object(bson_document=user) if user else None


def _credentials_flow(
    auth_details: PasswordAuthentication,
) -> AuthToken:
    user = get_user(username=auth_details.username)

    if user is None:
        raise HTTPException(status_code=401, detail="Wrong user")

    if not authentication.verify_password(
        password=auth_details.password, hashed_password=user.password
    ):
        raise HTTPException(status_code=401, detail="Wrong password")

    return authentication.encode_jwt(user.username)


def _refresh_token_flow(
    auth_details: RefreshTokenAuthentication,
) -> AuthToken:
    username = get_username_from_token(
        authentication=authentication, refresh_token=auth_details.refresh_token
    )
    user = get_user(username=username)

    if user is None:
        raise HTTPException(status_code=401, detail="Wrong user")

    return authentication.encode_jwt(user.username)


def get_token(auth_details: AuthenticationDetails) -> AuthToken:
    if isinstance(auth_details, PasswordAuthentication):
        return _credentials_flow(auth_details)

    if isinstance(auth_details, RefreshTokenAuthentication):
        return _refresh_token_flow(auth_details)
