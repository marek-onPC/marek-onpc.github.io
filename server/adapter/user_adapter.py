import os
from typing import Optional
from dotenv import load_dotenv
from helpers.db_client import DatabaseClient
from schemas import User

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_USERS"]
db_client = DatabaseClient(db_uri, db_name)


def get_user(username: str) -> Optional[User]:
    collection = db_client.db_connection(db_collection_name)

    user = db_client.db_find_one(collection, {
        "user": username
    })

    if user:
        mappedUser = User(
            username=user["user"],
            password=user["password"]
        )
    else:
        mappedUser = None

    return mappedUser
