import json
import os
from dotenv import load_dotenv
from fastapi import Depends, APIRouter, HTTPException
from auth.authentication import Authentication
from db.db_client import DatabaseClient
from bson.objectid import ObjectId

from schemas.schemas import NoteSchema

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_NOTES"]
db_client = DatabaseClient(db_uri, db_name)

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.get("/note/{note_id}")
def get_note(note_id: str, username = Depends(authentication.auth_wrapper)):
    if username:
        collection = db_client.db_connection(db_collection_name)
        result = db_client.db_find_one(collection, {
            "_id" : ObjectId(note_id)
        })

        return json.dumps(result, default=str)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@router.post("/note")
def get_note(note_data: NoteSchema, username = Depends(authentication.auth_wrapper)):
    if username:
        if note_data._id == "":
            collection = db_client.db_connection(db_collection_name)

            result = db_client.db_add_note(collection, {
                "title": note_data.title,
                "categories": note_data.categories,
                "content": note_data.content
            })

            # ADD NEW POST
        else:
            # UPDATE POST
            print("update")

        return json.dumps(result, default=str)
    else:
        raise HTTPException(status_code=400, detail="Error during post add/edit")
