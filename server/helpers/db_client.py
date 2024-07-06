from typing import Any, Dict
from bson import ObjectId
from gridfs import Collection
from pymongo import MongoClient
from schemas import ProjectSchema

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


    def db_add(self, collection: Collection, project_data: ProjectSchema) -> Any:
        result = collection.insert_one({
            "title" : project_data["title"],
            "project_type" : project_data["project_type"],
            "content" : project_data["content"]
        })

        return result


    def db_update(self, collection: Collection, project_data: ProjectSchema) -> Any:
        result = collection.update_one(
            { "_id" : ObjectId(project_data["_id"]) },
            { "$set" : 
                {
                    "title" : project_data["title"],
                    "project_type" : project_data["project_type"],
                    "content" : project_data["content"]
                }
            }
        )

        return result
