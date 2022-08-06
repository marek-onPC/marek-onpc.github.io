from bson import ObjectId
import mongomock
import pytest
import os
from dotenv import load_dotenv
from typing import Dict, List
from db.db_client import DatabaseClient
from schemas.schemas import NoteSchema

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_client = DatabaseClient(db_uri, db_name)

# DATABASE MOCK PREPARATION ------------------------------
mock_collection = mongomock.MongoClient().db.collections
documents = [
    {
        "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
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
        "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
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
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
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
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
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
def test_get_notes(expected_notes: List) -> None:
    notes = []
    result = db_client.db_find_all(mock_collection)

    for sample in result:
        notes.append(sample)

    assert notes == expected_notes


@pytest.mark.parametrize(
    "expected_note", [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
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
def test_get_note(expected_note: List) -> None:
    result = db_client.db_find_one(mock_collection, {
            "_id" : ObjectId("62edd29215f7ccf1b7a44b87")
        })

    assert result == expected_note[0]


@pytest.mark.parametrize(
    "note_to_update", [
        {
            "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
            "title": "New first entry",
            "date": "2022-06-28T15:00:00.000+00:00",
            "categories":
            [
                "category3",
                "category4"
            ],
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
                "categories":
                [
                    "category3",
                    "category4"
                ],
                "content": "new content"
            },
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
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
def test_db_update_note(note_to_update: NoteSchema, expected_result: List) -> None:
    db_client.db_update_note(mock_collection, note_to_update)

    notes = []
    result = db_client.db_find_all(mock_collection)

    for sample in result:
        notes.append(sample)

    print(notes)
    print("-----")
    print(expected_result)
    assert notes == expected_result


@pytest.mark.parametrize(
    "note_to_add", [
        {
            "title": "Third entry",
            "categories":
            [
                "category0",
                "category1"
            ],
            "content": "content"
        }
    ]
)
@pytest.mark.parametrize(
    "expected_result", [
        {
            "title": "Third entry",
            "categories":
            [
                "category0",
                "category1"
            ],
            "content": "content"
        }
    ]
)
def test_db_add_note(note_to_add: NoteSchema, expected_result: List) -> None:
    db_client.db_add_note(mock_collection, note_to_add)
    notes = []
    result = db_client.db_find_all(mock_collection)

    for sample in result:
        notes.append(sample)

    assert notes[2]["title"] == expected_result["title"]
    assert notes[2]["categories"] == expected_result["categories"]
    assert notes[2]["content"] == expected_result["content"]
