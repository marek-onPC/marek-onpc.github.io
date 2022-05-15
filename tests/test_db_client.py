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
        "user": "john",
        "hashedPassword": "$2b$12$jwzb6rl2uspKNkJqNhv.z.kC36N.F3tQ5JzfywEgp422hufoHc7/C",
        # password is "password"
    },
    {
        "_id": 2,
        "user": "mark",
        "hashedPassword": "$2b$12$jwzb6rl2uspKNkJqNhv.z.kC36N.F3tQ5JzfywEgp422hufoHc7/C",    },
    {
        "_id": 3,
        "user": "george",
        "hashedPassword": "$2b$12$jwzb6rl2uspKNkJqNhv.z.kC36N.F3tQ5JzfywEgp422hufoHc7/C",    }
]
mock_collection.insert_many(documents)
# END OF DATABASE MOCK PREPARATION -----------------------

@pytest.mark.parametrize(
    "user_to_find", [
        {
            "user": "george"
        },
        {
            "user": "john"
        },
        {
            "user": "mark"
        },
    ]
)
def test_db_find_one(user_to_find: Dict) -> None:
    result = db_client.db_find_one(mock_collection, user_to_find)

    assert result["user"] == user_to_find["user"]
