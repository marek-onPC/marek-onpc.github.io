import json
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

from helpers.db_client import DatabaseClient
from schemas import CheatSheetID, CheatSheetSchema


load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_CHEAT_SHEETS"]
db_client = DatabaseClient(db_uri, db_name)


def get_cheat_sheets():
    cheat_sheets = []
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_find_all(collection)

    for sample in result:
        if sample["_id"]:  
            sample["id"] = sample["_id"]
            del sample["_id"]

        cheat_sheets.append(sample)
        cheat_sheets.reverse()

    return json.dumps(cheat_sheets, default=str)


def get_cheat_sheet(cheat_sheet_id: CheatSheetID):
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_find_one(collection, {
        "_id" : ObjectId(cheat_sheet_id)
    })

    if result["_id"]:  
        result["id"] = result["_id"]
        del result["_id"]

    return json.dumps(result, default=str)


def create_cheat_sheet(cheat_sheet_data: CheatSheetSchema):
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_add(collection, {
        "title": cheat_sheet_data.title,
        "category": cheat_sheet_data.category,
        "content": cheat_sheet_data.content
    })

    return json.dumps(result, default=str)


def patch_cheat_sheet(cheat_sheet_data: CheatSheetSchema):
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_update(collection, {
        "_id": cheat_sheet_data.id,
        "title": cheat_sheet_data.title,
        "category": cheat_sheet_data.category,
        "content": cheat_sheet_data.content
    })

    return json.dumps(result, default=str)
