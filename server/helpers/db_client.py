from typing import Any, Dict
from bson import ObjectId
from gridfs import Collection
from pymongo import MongoClient
from schemas import CheatSheetContent, MongoInsert, MongoUpdate

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


    def db_find_all(self, collection: Collection, filters: dict) -> Any:
        result = collection.find(filters)

        return result


    def db_add(self, collection: Collection, cheat_sheet_data: dict) -> MongoInsert:
        result = collection.insert_one({
            "title" : cheat_sheet_data.get("title"),
            "category" : cheat_sheet_data.get("category", None),
            "is_published" : cheat_sheet_data.get("is_published", None)
        })

        return MongoInsert(id=str(result.inserted_id))


    def __serialize_cards(self, cards: list[CheatSheetContent]) -> list[dict]:
        serialized = []

        for card in cards:
            serialized.append({
                "subtitle": card.subtitle,
                "content": card.content
            })

        return serialized


    def db_update(self, collection: Collection, id: str, cheat_sheet_data: dict) -> MongoUpdate:
        cards = cheat_sheet_data.get("cards", None)

        result = collection.update_one(
            { "_id" : ObjectId(id) },
            { "$set" : 
                {
                    "title" : cheat_sheet_data.get("title"),
                    "category" : cheat_sheet_data.get("category", None),
                    "cards" : self.__serialize_cards(cards) if cards else None,
                    "is_published" : cheat_sheet_data.get("is_published")
                }
            }
        )

        return MongoUpdate(acknowledged=result.acknowledged)


    def db_delete(self, collection: Collection, id: str) -> Any:
        result = collection.delete_one(
            { "_id" : ObjectId(id) }
        )

        return MongoUpdate(acknowledged=result.acknowledged)
