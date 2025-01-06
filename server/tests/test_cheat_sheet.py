from typing import Any, List

import mongomock
import pytest
from bson import ObjectId
from mongomock import Collection

from helpers.db_client import DatabaseClient

db_uri = "DB_URI"
db_name = "DB_NAME"
db_client = DatabaseClient(db_uri, db_name)

# DATABASE MOCK PREPARATION ------------------------------
mock_collection: Collection = mongomock.MongoClient().db.collections
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
    },
]
mock_collection.insert_many(documents)
# END OF DATABASE MOCK PREPARATION -----------------------


def _clear_test_db() -> None:
    mock_collection.delete_many({})
    mock_collection.insert_many(documents)


def _remove_objectid(doc: Any) -> Any:
    """Remove the ObjectId field from the document."""
    doc_copy = doc.copy()  # To avoid modifying the original document
    if "_id" in doc_copy:
        del doc_copy["_id"]
    return doc_copy


@pytest.mark.parametrize(
    "expected_cheat_sheets",
    [
        [
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
            },
        ]
    ],
)
def test_get_cheat_sheets(expected_cheat_sheets: List) -> None:
    cheat_sheets = []
    result = db_client.db_find_all(mock_collection, {})

    for sample in result:
        cheat_sheets.append(sample)

    assert cheat_sheets == expected_cheat_sheets


@pytest.mark.parametrize(
    "expected_cheat_sheet",
    [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
            }
        ]
    ],
)
def test_get_cheat_sheet(expected_cheat_sheet: List) -> None:
    result = db_client.db_find_one(
        mock_collection, {"_id": ObjectId("62edd29215f7ccf1b7a44b87")}
    )

    assert result == expected_cheat_sheet[0]


@pytest.mark.parametrize(
    "cheat_sheet_to_update, update_content",
    [
        pytest.param(
            "62edd29215f7ccf1b7a44b86",
            {
                "title": "New first entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "Card", "content": "Content"}],
            },
        )
    ],
)
@pytest.mark.parametrize(
    "expected_result",
    [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "title": "New first entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "Card", "content": "Content"}],
            },
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
            },
        ]
    ],
)
def test_db_update_cheat_sheet(
    cheat_sheet_to_update: str, update_content: dict, expected_result: List
) -> None:
    db_client.db_update(mock_collection, cheat_sheet_to_update, update_content)

    cheat_sheets = []
    result = db_client.db_find_all(mock_collection, {})

    for sample in result:
        cheat_sheets.append(sample)

    assert cheat_sheets == expected_result
    _clear_test_db()


@pytest.mark.parametrize(
    "cheat_sheet_to_add",
    [
        {
            "title": "Third entry",
            "language": "typescript",
            "is_published": False,
        }
    ],
)
@pytest.mark.parametrize(
    "expected_result",
    [
        [
            {
                "title": "First entry",
                "language": "typescript",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
            },
            {
                "title": "Second entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
            },
            {
                "title": "Third entry",
                "language": "typescript",
                "is_published": False,
            },
        ]
    ],
)
def test_db_add_cheat_sheet(
    cheat_sheet_to_add: dict, expected_result: List[dict]
) -> None:
    db_client.db_add(mock_collection, cheat_sheet_to_add)
    cheat_sheets = []
    result = db_client.db_find_all(mock_collection, {})

    for sample in result:
        cheat_sheets.append(_remove_objectid(sample))

    assert cheat_sheets == expected_result
