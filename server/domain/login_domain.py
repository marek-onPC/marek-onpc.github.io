import logging
import os
from typing import Any, Optional

from dotenv import load_dotenv
from fastapi import HTTPException

from helpers.authentication import Authentication
from helpers.db_client import DatabaseClient
from schemas import AuthenticationDetails, LoginToken, User, Username

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_USERS"]
db_client = DatabaseClient(db_uri, db_name, db_collection_name).connection()

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


def login(auth_details: AuthenticationDetails) -> LoginToken:
    if auth_details.grant_type != "password":
        raise HTTPException(status_code=400, detail="Invalid grant type")

    user = get_user(username=auth_details.username)

    if user is None:
        raise HTTPException(status_code=401, detail="Wrong user")

    if not authentication.verify_password(
        password=auth_details.password, hashed_password=user.password
    ):
        raise HTTPException(status_code=401, detail="Wrong password")

    token, expiry = authentication.encode_jwt(user.username)

    return LoginToken(token=token, expiry=expiry.timestamp())
