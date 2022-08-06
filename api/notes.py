import json
import os
from dotenv import load_dotenv
from fastapi import Depends, APIRouter, HTTPException
from auth.authentication import Authentication
from db.db_client import DatabaseClient

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_NOTES"]
db_client = DatabaseClient(db_uri, db_name)

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.get("/notes")
def notes(username = Depends(authentication.auth_wrapper)):
    if username:
        notes = []
        collection = db_client.db_connection(db_collection_name)
        result = db_client.db_find_all(collection)

        for sample in result:
            if sample["_id"]:  
                sample["id"] = sample["_id"]
                del sample["_id"]

            notes.append(sample)

        return json.dumps(notes, default=str)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
