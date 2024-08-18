from bson import ObjectId
import mongomock
import pytest
from typing import List
from helpers.db_client import DatabaseClient
from schemas import ProjectSchema

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
        "project_type": "MAIN",
        "content":"content"
    },
    {
        "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
        "title": "Second entry",
        "date": "2022-06-28T15:00:00.000+00:00",
        "project_type": "MINOR",
        "content": "content"
    }
]
mock_collection.insert_many(documents)
# END OF DATABASE MOCK PREPARATION -----------------------

@pytest.mark.parametrize(
    "expected_projects", [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "title": "First entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "project_type": "MAIN",
                "content":"content"
            },
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "project_type": "MINOR",
                "content": "content"
            }
        ]
    ]
)
def test_get_projects(expected_projects: List) -> None:
    projects = []
    result = db_client.db_find_all(mock_collection)

    for sample in result:
        projects.append(sample)

    assert projects == expected_projects


@pytest.mark.parametrize(
    "expected_project", [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "project_type": "MINOR",
                "content": "content"
            }
        ]
    ]
)
def test_get_project(expected_project: List) -> None:
    result = db_client.db_find_one(mock_collection, {
            "_id" : ObjectId("62edd29215f7ccf1b7a44b87")
        })

    assert result == expected_project[0]


@pytest.mark.parametrize(
    "project_to_update", [
        {
            "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
            "title": "New first entry",
            "date": "2022-06-28T15:00:00.000+00:00",
            "project_type": "MINOR",
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
                "project_type": "MINOR",
                "content": "new content"
            },
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "date": "2022-06-28T15:00:00.000+00:00",
                "project_type": "MINOR",
                "content": "content"
            }
        ]
    ]
)
def test_db_update_project(project_to_update: ProjectSchema, expected_result: List) -> None:
    db_client.db_update(mock_collection, project_to_update)

    projects = []
    result = db_client.db_find_all(mock_collection)

    for sample in result:
        projects.append(sample)

    assert projects == expected_result


@pytest.mark.parametrize(
    "project_to_add", [
        {
            "title": "Third entry",
            "project_type": "MAIN",
            "content": "content"
        }
    ]
)
@pytest.mark.parametrize(
    "expected_result", [
        {
            "title": "Third entry",
            "project_type": "MAIN",
            "content": "content"
        }
    ]
)
def test_db_add_project(project_to_add: ProjectSchema, expected_result: List) -> None:
    db_client.db_add(mock_collection, project_to_add)
    projects = []
    result = db_client.db_find_all(mock_collection)

    for sample in result:
        projects.append(sample)

    assert projects[2]["title"] == expected_result["title"]
    assert projects[2]["project_type"] == expected_result["project_type"]
    assert projects[2]["content"] == expected_result["content"]
