from bson import ObjectId
import mongomock
import pytest
from typing import List
from helpers.db_client import DatabaseClient
from schemas import CheatSheetSchema

db_uri = "DB_URI"
db_name = "DB_NAME"
db_client = DatabaseClient(db_uri, db_name)

# DATABASE MOCK PREPARATION ------------------------------
mock_collection = mongomock.MongoClient().db.collections
documents = [
    {
        "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
        "title": "First entry",
        "date": "2022-06-28T15:00:00.000+00:00",
        "language": "MAIN",
        "content":"content"
    },
    {
        "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
        "title": "Second entry",
        "date": "2022-06-28T15:00:00.000+00:00",
        "language": "MINOR",
        "content": "content"
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
                "date": "2022-06-28T15:00:00.000+00:00",
                "language": "MAIN",
                "content":"content"
            },
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "language": "MINOR",
                "content": "content"
            }
        ]
    ]
)
def test_get_cheat_sheets(expected_cheat_sheets: List) -> None:
    cheat_sheets = []
    result = db_client.db_find_all(mock_collection)

    for sample in result:
        cheat_sheets.append(sample)

    assert cheat_sheets == expected_cheat_sheets


@pytest.mark.parametrize(
    "expected_cheat_sheet", [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "language": "MINOR",
                "content": "content"
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
    "cheat_sheet_to_update", [
        {
            "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
            "title": "New first entry",
            "date": "2022-06-28T15:00:00.000+00:00",
            "language": "MINOR",
            "content": "new content"
        },
    ]
)
@pytest.mark.parametrize(
    "expected_result", [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "title": "New first entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "language": "MINOR",
                "content": "new content"
            },
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "language": "MINOR",
                "content": "content"
            }
        ]
    ]
)
def test_db_update_cheat_sheet(cheat_sheet_to_update: CheatSheetSchema, expected_result: List) -> None:
    db_client.db_update(mock_collection, cheat_sheet_to_update)

    cheat_sheets = []
    result = db_client.db_find_all(mock_collection)

    for sample in result:
        cheat_sheets.append(sample)

    assert cheat_sheets == expected_result


@pytest.mark.parametrize(
    "cheat_sheet_to_add", [
        {
            "title": "Third entry",
            "language": "MAIN",
            "content": "content"
        }
    ]
)
@pytest.mark.parametrize(
    "expected_result", [
        {
            "title": "Third entry",
            "language": "MAIN",
            "content": "content"
        }
    ]
)
def test_db_add_cheat_sheet(cheat_sheet_to_add: CheatSheetSchema, expected_result: List) -> None:
    db_client.db_add(mock_collection, cheat_sheet_to_add)
    cheat_sheets = []
    result = db_client.db_find_all(mock_collection)

    for sample in result:
        cheat_sheets.append(sample)

    assert cheat_sheets[2]["title"] == expected_result["title"]
    assert cheat_sheets[2]["language"] == expected_result["language"]
    assert cheat_sheets[2]["content"] == expected_result["content"]
