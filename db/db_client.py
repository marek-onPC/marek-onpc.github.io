from typing import Any, Dict
from bson import ObjectId
from gridfs import Collection
from pymongo import MongoClient
from fastapi import UploadFile

from schemas.schemas import NoteSchema

class DatabaseClient:
    def __init__(self, db_uri: str, db_name: str) -> None:
        self.db_uri = db_uri
        self.db_name = db_name


    def db_connection(self, collection_name: str) -> Collection:
        client = MongoClient(self.db_uri,  tls=True, tlsAllowInvalidCertificates=True)
        database = client[self.db_name]
        collection = database[collection_name]

        return collection


    def db_find_one(self, collection: Collection, item_to_find: Dict) -> Any:
        result = collection.find_one(item_to_find)

        return result


    def db_find_all(self, collection: Collection) -> Any:
        result = collection.find()

        return result


    def db_add_note(self, collection: Collection, note_data: NoteSchema) -> Any:
        result = collection.insert_one({
            "title" : note_data["title"],
            "categories" : note_data["categories"],
            "content" : note_data["content"]
        })

        return result


    def db_update_note(self, collection: Collection, note_data: NoteSchema) -> Any:
        result = collection.update_one(
            { "_id" : ObjectId(note_data["_id"]) },
            { "$set" : 
                {
                    "title" : note_data["title"],
                    "categories" : note_data["categories"],
                    "content" : note_data["content"]
                }
            }
        )

        return result


    def db_update_user_photo(self, collection: Collection, user: str, photo: UploadFile) -> Any:
        result = collection.update_one(
            { "user" : user },
            { "$set" : 
                {
                    "photo" : photo,
                }
            }
        )

        return result