from typing import List

import mongomock
import pytest
from bson import ObjectId

from helpers.db_client import DatabaseClient
from schemas import CheatSheetContent, CheatSheetSchema, UpdateCheatSheetSchema

db_uri = "DB_URI"
db_name = "DB_NAME"
db_client = DatabaseClient(db_uri, db_name)

# DATABASE MOCK PREPARATION ------------------------------
mock_collection = mongomock.MongoClient().db.collections
documents = [
    {
        "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
        "title": "First entry",
        "language": "typescript",
        "is_published": True,
        "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
    },
    {
        "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
        "title": "Second entry",
        "language": "python",
        "is_published": True,
        "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
    }
]
mock_collection.insert_many(documents)
# END OF DATABASE MOCK PREPARATION -----------------------

@pytest.mark.parametrize(
    "expected_cheat_sheets", [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "title": "First entry",
                "language": "typescript",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}]
            },
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}]
            }
        ]
    ]
)
def test_get_cheat_sheets(expected_cheat_sheets: List) -> None:
    cheat_sheets = []
    result = db_client.db_find_all(mock_collection, {})

    for sample in result:
        cheat_sheets.append(sample)

    assert cheat_sheets == expected_cheat_sheets


@pytest.mark.parametrize(
    "expected_cheat_sheet", [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}]
            }
        ]
    ]
)
def test_get_cheat_sheet(expected_cheat_sheet: List) -> None:
    result = db_client.db_find_one(mock_collection, {
            "_id" : ObjectId("62edd29215f7ccf1b7a44b87")
        })

    assert result == expected_cheat_sheet[0]


@pytest.mark.parametrize(
    "cheat_sheet_to_update, update_content", [
        pytest.param(
            "62edd29215f7ccf1b7a44b86",
            {
                "title": "New first entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "Card", "content": "Content"}]
            }
        )
    ]
)
@pytest.mark.parametrize(
    "expected_result", [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "title": "New first entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "Card", "content": "Content"}]
            },
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}]
            }
        ]
    ]
)
def test_db_update_cheat_sheet(cheat_sheet_to_update: str, update_content: dict, expected_result: List) -> None:
    db_client.db_update(mock_collection, cheat_sheet_to_update, update_content)

    cheat_sheets = []
    result = db_client.db_find_all(mock_collection, {})

    for sample in result:
        cheat_sheets.append(sample)

    assert cheat_sheets == expected_result


@pytest.mark.parametrize(
    "cheat_sheet_to_add", [
        {
            "title": "Third entry",
            "language": "typescript",
            "is_published": False,
        }
    ]
)
@pytest.mark.parametrize(
    "expected_result", [
        {
            "title": "Third entry",
            "language": "typescript",
            "is_published": False,
        }
    ]
)
def test_db_add_cheat_sheet(cheat_sheet_to_add: dict, expected_result: List) -> None:
    db_client.db_add(mock_collection, cheat_sheet_to_add)
    cheat_sheets = []
    result = db_client.db_find_all(mock_collection, {})

    for sample in result:
        cheat_sheets.append(sample)

    assert cheat_sheets[2]["title"] == expected_result["title"]
    assert cheat_sheets[2]["language"] == expected_result["language"]
    assert cheat_sheets[2]["is_published"] == expected_result["is_published"]
