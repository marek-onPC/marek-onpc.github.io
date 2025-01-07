from typing import Any, List
from unittest import mock

import mongomock
import pytest
from bson import ObjectId
from mongomock import Collection

from domain.cheat_sheet_domain import (
    create_cheat_sheet,
    get_cheat_sheet,
    get_cheat_sheets,
    patch_cheat_sheet,
)
from schemas import (
    CheatSheetContent,
    CheatSheetSchema,
    UnsavedCheatSheetSchema,
    UpdateCheatSheetSchema,
)

db_name = "DB_NAME"
db_name = "DB_COLL"

# DATABASE MOCK PREPARATION ------------------------------
mock_collection: Collection = (
    mongomock.MongoClient().get_database(db_name).get_collection(db_name)
)
documents = [
    {
        "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
        "title": "First entry",
        "language": "typescript",
        "is_published": False,
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
            CheatSheetSchema(
                title="Second entry",
                language="python",
                is_published=True,
                cards=[
                    CheatSheetContent(subtitle="card_subtitle", content="card_content")
                ],
                id="62edd29215f7ccf1b7a44b87",
            ),
            CheatSheetSchema(
                title="First entry",
                language="typescript",
                is_published=False,
                cards=[
                    CheatSheetContent(subtitle="card_subtitle", content="card_content")
                ],
                id="62edd29215f7ccf1b7a44b86",
            ),
        ]
    ],
)
@mock.patch("domain.cheat_sheet_domain.db_client", mock_collection)
def test_get_cheat_sheets(expected_cheat_sheets: List[CheatSheetSchema]) -> None:
    result = get_cheat_sheets()

    assert result == expected_cheat_sheets


@pytest.mark.parametrize(
    "expected_cheat_sheet",
    [
        CheatSheetSchema(
            title="Second entry",
            language="python",
            is_published=True,
            cards=[CheatSheetContent(subtitle="card_subtitle", content="card_content")],
            id="62edd29215f7ccf1b7a44b87",
        ),
    ],
)
@mock.patch("domain.cheat_sheet_domain.db_client", mock_collection)
def test_get_cheat_sheet(expected_cheat_sheet: CheatSheetSchema) -> None:
    result = get_cheat_sheet(expected_cheat_sheet.id)

    assert result == expected_cheat_sheet


@pytest.mark.parametrize(
    "cheat_sheet_to_add",
    [
        UnsavedCheatSheetSchema(
            title="Third entry", language="typescript", is_published=False
        )
    ],
)
@pytest.mark.parametrize(
    "expected_result",
    [
        [
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "title": "First entry",
                "language": "typescript",
                "is_published": False,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
            },
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b87"),
                "title": "Second entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
            },
            {
                "_id": "TEMPORARY",
                "title": "Third entry",
                "language": "typescript",
                "is_published": False,
            },
        ]
    ],
)
@mock.patch("domain.cheat_sheet_domain.db_client", mock_collection)
def test_create_cheat_sheet(
    cheat_sheet_to_add: UnsavedCheatSheetSchema, expected_result: List[dict]
) -> None:
    result = create_cheat_sheet(cheat_sheet_to_add)
    expected_result[2]["_id"] = ObjectId(result.id)

    cursor = mock_collection.find()
    all_cheat_sheets = []

    for sheet in cursor:
        all_cheat_sheets.append(sheet)

    assert all_cheat_sheets == expected_result
    _clear_test_db()


@pytest.mark.parametrize(
    "id_to_update, update_content, before_update, expected_result",
    [
        pytest.param(
            "62edd29215f7ccf1b7a44b86",
            UpdateCheatSheetSchema(
                title="Updated first entry",
                language="svelte",
                is_published=False,
                cards=[
                    CheatSheetContent(subtitle="card_subtitle", content="card_content")
                ],
            ),
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "title": "First entry",
                "language": "typescript",
                "is_published": False,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
            },
            {
                "_id": ObjectId("62edd29215f7ccf1b7a44b86"),
                "title": "Updated first entry",
                "language": "svelte",
                "is_published": False,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
            },
        )
    ],
)
@mock.patch("domain.cheat_sheet_domain.db_client", mock_collection)
def test_patch_cheat_sheet(
    id_to_update: str,
    update_content: UpdateCheatSheetSchema,
    before_update: dict,
    expected_result: dict,
) -> None:

    sheet = mock_collection.find_one({"_id": ObjectId(id_to_update)})
    assert sheet == before_update

    result = patch_cheat_sheet(id_to_update, update_content)
    sheet = mock_collection.find_one({"_id": ObjectId(id_to_update)})

    assert result.acknowledged is True
    assert sheet == expected_result
    _clear_test_db()
