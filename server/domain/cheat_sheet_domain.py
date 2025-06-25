import os
from typing import Literal, Optional

from bson.objectid import ObjectId
from dotenv import load_dotenv

from helpers.db_client import DatabaseClient
from schemas import (
    CheatSheetContent,
    CheatSheetID,
    CheatSheetSchema,
    MongoDelete,
    MongoInsert,
    MongoUpdate,
    UnsavedCheatSheetSchema,
    UpdateCheatSheetSchema,
)

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_CHEAT_SHEETS"]
db_client = DatabaseClient(db_uri, db_name).connection()[db_collection_name]


def _serialize_cards(cards: list[CheatSheetContent]) -> list[dict]:
    serialized = []

    for card in cards:
        serialized.append({"subtitle": card.subtitle, "content": card.content})

    return serialized


def _fiters_to_bson(
    is_published__list: Optional[list[Literal[True, False]]] = None
) -> dict:
    bson_filters = []

    if is_published__list:
        is_published_bson = {"is_published": {"$in": is_published__list}}
        bson_filters.append(is_published_bson)

    if bson_filters:
        return {"$and": bson_filters}
    else:
        return {}


def get_cheat_sheets(
    is_published__list: Optional[list[Literal[True, False]]] = None
) -> list[CheatSheetSchema] | None:
    filters = _fiters_to_bson(is_published__list=is_published__list)
    cheat_sheets = []

    result = db_client.find(filters)

    if result is None:
        return None

    for entry in result:
        cheat_sheet = CheatSheetSchema(
            id=CheatSheetID(str(entry.get("_id"))),
            cards=entry.get("cards", None),
            title=entry.get("title"),
            language=entry.get("language", None),
            is_published=entry.get("is_published", None),
        )

        cheat_sheets.append(cheat_sheet)

    cheat_sheets.reverse()

    return cheat_sheets


def get_cheat_sheet(cheat_sheet_id: CheatSheetID) -> CheatSheetSchema | None:
    result = db_client.find_one({"_id": ObjectId(cheat_sheet_id)})

    if result is None:
        return None

    cheat_sheet = CheatSheetSchema(
        id=CheatSheetID(str(result.get("_id"))),
        cards=result.get("cards", None),
        title=result.get("title"),
        language=result.get("language", None),
        is_published=result.get("is_published", None),
    )

    return cheat_sheet


def create_cheat_sheet(cheat_sheet_data: UnsavedCheatSheetSchema) -> MongoInsert:
    inserted = db_client.insert_one(
        {
            "title": cheat_sheet_data.title,
            "language": cheat_sheet_data.language,
            "is_published": cheat_sheet_data.is_published,
        },
    )

    return MongoInsert(id=str(inserted.inserted_id))


def patch_cheat_sheet(id: str, cheat_sheet_data: UpdateCheatSheetSchema) -> MongoUpdate:
    result = db_client.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "title": cheat_sheet_data.title,
                "language": cheat_sheet_data.language,
                "cards": (
                    _serialize_cards(cheat_sheet_data.cards)
                    if cheat_sheet_data.cards
                    else []
                ),
                "is_published": cheat_sheet_data.is_published,
            }
        },
    )

    return MongoUpdate(acknowledged=result.acknowledged)


def delete_cheat_sheet(id: str) -> MongoDelete:
    result = db_client.delete_one({"_id": ObjectId(id)})

    return MongoDelete(acknowledged=result.acknowledged)
