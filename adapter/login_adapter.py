import os
from typing import Optional
from dotenv import load_dotenv
from db.db_client import DatabaseClient
import schemas.schemas

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_USERS"]
db_client = DatabaseClient(db_uri, db_name)


def login(username: str) -> Optional[schemas.schemas.User]:
    collection = db_client.db_connection(db_collection_name)

    user = db_client.db_find_one(collection, {
        "user": username
    })

    if user:
        mappedUser = schemas.schemas.User(
            username=user["user"],
            password=user["password"],
            photo=user["photo"]
            if type(user["photo"]) is not None else None)
    else:
        mappedUser = None

    return mappedUser
