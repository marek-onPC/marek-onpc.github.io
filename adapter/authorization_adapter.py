import os
from typing import Dict, Optional
from dotenv import load_dotenv
from db.db_client import DatabaseClient
from fastapi import UploadFile

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_USERS"]
db_client = DatabaseClient(db_uri, db_name)


def add_photo(username: str,  photo: UploadFile) -> Optional[Dict]:
    collection = db_client.db_connection(db_collection_name)
    user = db_client.db_update_user_photo(collection, username, photo.file.read())

    return user
