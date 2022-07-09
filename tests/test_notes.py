import mongomock
import pytest
import os
from dotenv import load_dotenv
from typing import Dict
from db.db_client import DatabaseClient

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_client = DatabaseClient(db_uri, db_name)

# DATABASE MOCK PREPARATION ------------------------------
mock_collection = mongomock.MongoClient().db.collections
documents = [
    {
        "_id": 1,
        "title": "First entry",
        "date": "2022-06-28T15:00:00.000+00:00",
        "categories":
        [
            "category0",
            "category1"
        ],
        "content":"content"
    },
    {
        "_id": 2,
        "title": "Second entry",
        "date": "2022-06-28T15:00:00.000+00:00",
        "categories":
        [
            "category0",
            "category1"
        ],
        "content": "content"
    }
]
mock_collection.insert_many(documents)
# END OF DATABASE MOCK PREPARATION -----------------------

@pytest.mark.parametrize(
    "expected_notes", [
        [
            {
                "_id": 1,
                "title": "First entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "categories":
                [
                    "category0",
                    "category1"
                ],
                "content":"content"
            },
            {
                "_id": 2,
                "title": "Second entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "categories":
                [
                    "category0",
                    "category1"
                ],
                "content": "content"
            }
        ]
    ]
)
def test_get_notes(expected_notes: list) -> None:
    notes = []
    result = db_client.db_find_all(mock_collection)

    for sample in result:
        notes.append(sample)

    assert notes == expected_notes

@pytest.mark.parametrize(
    "expected_note", [
        [
            {
                "_id": 2,
                "title": "Second entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "categories":
                [
                    "category0",
                    "category1"
                ],
                "content": "content"
            }
        ]
    ]
)
def test_get_notes(expected_note: list) -> None:
    result = db_client.db_find_one(mock_collection, {
            "_id" : 2
        })

    assert result == expected_note[0]
