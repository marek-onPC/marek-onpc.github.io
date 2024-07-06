import os
import logging
from typing import Any, Optional
from dotenv import load_dotenv
from fastapi import HTTPException
from helpers.db_client import DatabaseClient
from schemas import User, Username

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_USERS"]
db_client = DatabaseClient(db_uri, db_name)


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
    collection = db_client.db_connection(db_collection_name)

    user = db_client.db_find_one(collection, {
        "user": username
    })

    return _bson_user_to_object(bson_document=user) if user else None
