import os
from typing import Dict
from dotenv import load_dotenv
from auth.authentication import Authentication
from db.db_client import DatabaseClient

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_USERS"]
db_client = DatabaseClient(db_uri, db_name)

authentication = Authentication()

def login(username: str) -> Dict | None:
    collection = db_client.db_connection(db_collection_name)

    user = db_client.db_find_one(collection, {
        "user": username
    })

    return user
