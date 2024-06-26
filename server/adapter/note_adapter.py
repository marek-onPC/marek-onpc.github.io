import json
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

from server.db.db_client import DatabaseClient
from server.schemas.schemas import NoteSchema


load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_NOTES"]
db_client = DatabaseClient(db_uri, db_name)


def get_notes():
    notes = []
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_find_all(collection)

    for sample in result:
        if sample["_id"]:  
            sample["id"] = sample["_id"]
            del sample["_id"]

        notes.append(sample)
        notes.reverse()

    return json.dumps(notes, default=str)


def get_note_by_id(note_id: str):
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_find_one(collection, {
        "_id" : ObjectId(note_id)
    })

    if result["_id"]:  
        result["id"] = result["_id"]
        del result["_id"]

    return json.dumps(result, default=str)


def post_new_note(note_data: NoteSchema):
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_add_note(collection, {
        "title": note_data.title,
        "categories": note_data.categories,
        "content": note_data.content
    })

    return json.dumps(result, default=str)


def update_note(note_data: NoteSchema):
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_update_note(collection, {
        "_id": note_data.id,
        "title": note_data.title,
        "categories": note_data.categories,
        "content": note_data.content
    })

    return json.dumps(result, default=str)
