import os
from typing import Any, Dict
from dotenv import load_dotenv
from gridfs import Collection
from pymongo import MongoClient

load_dotenv()

class DatabaseClient:
    db_uri = os.environ["DB_URI"]
    db_name = os.environ["DB_NAME"]


    def db_connection(self, collection_name: str) -> Collection:
        client = MongoClient(self.db_uri,  tls=True, tlsAllowInvalidCertificates=True)
        database = client[self.db_name]
        collection = database[collection_name]

        return collection


    def db_find_one(self, collection_name: str, item_to_find: Dict) -> Any:
        collection = self.db_connection(collection_name)
        result = collection.find_one(item_to_find)

        return result
