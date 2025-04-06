from unittest import mock
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app
from schemas import (
    CheatSheetContent,
    CheatSheetSchema,
    UnsavedCheatSheetSchema,
    UpdateCheatSheetSchema,
    Username,
)
from view.cheat_sheet_view import authentication

client = TestClient(app)


def _mock_auth_wrapper() -> Username:
    return Username("test_user")


@pytest.mark.parametrize(
    "cheat_sheets, expected_cheat_sheets, filter, expected_filter",
    [
        pytest.param(
            [
                CheatSheetSchema(
                    title="Second entry",
                    language="python",
                    is_published=True,
                    cards=[
                        CheatSheetContent(
                            subtitle="card_subtitle", content="card_content"
                        )
                    ],
                    id="62edd29215f7ccf1b7a44b87",
                ),
            ],
            [
                {
                    "title": "Second entry",
                    "language": "python",
                    "is_published": True,
                    "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                    "id": "62edd29215f7ccf1b7a44b87",
                },
            ],
            None,
            [True],
        ),
        pytest.param(
            [
                CheatSheetSchema(
                    title="Second entry",
                    language="python",
                    is_published=True,
                    cards=[
                        CheatSheetContent(
                            subtitle="card_subtitle", content="card_content"
                        )
                    ],
                    id="62edd29215f7ccf1b7a44b87",
                ),
            ],
            [
                {
                    "title": "Second entry",
                    "language": "python",
                    "is_published": True,
                    "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                    "id": "62edd29215f7ccf1b7a44b87",
                },
            ],
            {"is_published__list": "true"},
            [True],
        ),
        pytest.param(
            [
                CheatSheetSchema(
                    title="Second entry",
                    language="python",
                    is_published=True,
                    cards=[
                        CheatSheetContent(
                            subtitle="card_subtitle", content="card_content"
                        )
                    ],
                    id="62edd29215f7ccf1b7a44b87",
                ),
            ],
            [
                {
                    "title": "Second entry",
                    "language": "python",
                    "is_published": True,
                    "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                    "id": "62edd29215f7ccf1b7a44b87",
                },
            ],
            {"is_published__list": "false"},
            [True],
        ),
        pytest.param(
            [
                CheatSheetSchema(
                    title="Second entry",
                    language="python",
                    is_published=True,
                    cards=[
                        CheatSheetContent(
                            subtitle="card_subtitle", content="card_content"
                        )
                    ],
                    id="62edd29215f7ccf1b7a44b87",
                ),
            ],
            [
                {
                    "title": "Second entry",
                    "language": "python",
                    "is_published": True,
                    "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                    "id": "62edd29215f7ccf1b7a44b87",
                },
            ],
            {"is_published__list": "false,true"},
            [True],
        ),
    ],
)
@mock.patch("domain.cheat_sheet_domain.get_cheat_sheets")
def test_get_cheat_sheets__non_authorized(
    mock_get_cheat_sheets: MagicMock,
    cheat_sheets: list[CheatSheetSchema],
    expected_cheat_sheets: list[dict],
    filter: dict | None,
    expected_filter: list[bool],
) -> None:
    mock_get_cheat_sheets.return_value = cheat_sheets

    response = client.get("/api/cheat_sheets", params=filter)
    assert response.status_code == 200
    assert response.json() == expected_cheat_sheets
    mock_get_cheat_sheets.assert_called_with(is_published__list=expected_filter)


@pytest.mark.parametrize(
    "cheat_sheets, expected_cheat_sheets, filter, expected_filter",
    [
        pytest.param(
            [
                CheatSheetSchema(
                    title="Second entry",
                    language="python",
                    is_published=True,
                    cards=[
                        CheatSheetContent(
                            subtitle="card_subtitle", content="card_content"
                        )
                    ],
                    id="62edd29215f7ccf1b7a44b87",
                ),
            ],
            [
                {
                    "title": "Second entry",
                    "language": "python",
                    "is_published": True,
                    "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                    "id": "62edd29215f7ccf1b7a44b87",
                },
            ],
            None,
            [True],
        ),
        pytest.param(
            [
                CheatSheetSchema(
                    title="Second entry",
                    language="python",
                    is_published=True,
                    cards=[
                        CheatSheetContent(
                            subtitle="card_subtitle", content="card_content"
                        )
                    ],
                    id="62edd29215f7ccf1b7a44b87",
                ),
            ],
            [
                {
                    "title": "Second entry",
                    "language": "python",
                    "is_published": True,
                    "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                    "id": "62edd29215f7ccf1b7a44b87",
                },
            ],
            {"is_published__list": "true"},
            [True],
        ),
        pytest.param(
            [
                CheatSheetSchema(
                    title="First entry",
                    language="typescript",
                    is_published=False,
                    cards=[
                        CheatSheetContent(
                            subtitle="card_subtitle", content="card_content"
                        )
                    ],
                    id="62edd29215f7ccf1b7a44b86",
                ),
            ],
            [
                {
                    "title": "First entry",
                    "language": "typescript",
                    "is_published": False,
                    "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                    "id": "62edd29215f7ccf1b7a44b86",
                }
            ],
            {"is_published__list": "false"},
            [False],
        ),
        pytest.param(
            [
                CheatSheetSchema(
                    title="Second entry",
                    language="python",
                    is_published=True,
                    cards=[
                        CheatSheetContent(
                            subtitle="card_subtitle", content="card_content"
                        )
                    ],
                    id="62edd29215f7ccf1b7a44b87",
                ),
                CheatSheetSchema(
                    title="First entry",
                    language="typescript",
                    is_published=False,
                    cards=[
                        CheatSheetContent(
                            subtitle="card_subtitle", content="card_content"
                        )
                    ],
                    id="62edd29215f7ccf1b7a44b86",
                ),
            ],
            [
                {
                    "title": "Second entry",
                    "language": "python",
                    "is_published": True,
                    "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                    "id": "62edd29215f7ccf1b7a44b87",
                },
                {
                    "title": "First entry",
                    "language": "typescript",
                    "is_published": False,
                    "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                    "id": "62edd29215f7ccf1b7a44b86",
                },
            ],
            {"is_published__list": "false,true"},
            [False, True],
        ),
    ],
)
@mock.patch("domain.cheat_sheet_domain.get_cheat_sheets")
def test_get_cheat_sheets__authorized(
    mock_get_cheat_sheets: MagicMock,
    cheat_sheets: list[CheatSheetSchema],
    expected_cheat_sheets: list[dict],
    filter: dict | None,
    expected_filter: list[bool],
) -> None:
    app.dependency_overrides[authentication.optional_auth_wrapper] = _mock_auth_wrapper
    mock_get_cheat_sheets.return_value = cheat_sheets

    response = client.get("/api/cheat_sheets", params=filter)
    assert response.status_code == 200
    assert response.json() == expected_cheat_sheets
    mock_get_cheat_sheets.assert_called_with(is_published__list=expected_filter)

    app.dependency_overrides = {}


@pytest.mark.parametrize(
    "cheat_sheet, expected_cheat_sheet",
    [
        pytest.param(
            CheatSheetSchema(
                title="Second entry",
                language="python",
                is_published=True,
                cards=[
                    CheatSheetContent(subtitle="card_subtitle", content="card_content")
                ],
                id="62edd29215f7ccf1b7a44b87",
            ),
            {
                "title": "Second entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                "id": "62edd29215f7ccf1b7a44b87",
            },
            id="Published CS, return cheat sheet for non-authorized user",
        ),
        pytest.param(
            CheatSheetSchema(
                title="Second entry",
                language="python",
                is_published=False,
                cards=[
                    CheatSheetContent(subtitle="card_subtitle", content="card_content")
                ],
                id="62edd29215f7ccf1b7a44b87",
            ),
            None,
            id="Unpublished CS, return None for non-authorized user",
        ),
    ],
)
@mock.patch("domain.cheat_sheet_domain.get_cheat_sheet")
def test_get_cheat_sheet_by_id__non_authorized(
    mock_get_cheat_sheet: MagicMock,
    cheat_sheet: CheatSheetSchema,
    expected_cheat_sheet: dict,
) -> None:
    mock_get_cheat_sheet.return_value = cheat_sheet

    response = client.get("/api/cheat_sheets/62edd29215f7ccf1b7a44b87")
    assert response.status_code == 200
    assert response.json() == expected_cheat_sheet
    mock_get_cheat_sheet.assert_called_with(cheat_sheet_id="62edd29215f7ccf1b7a44b87")


@pytest.mark.parametrize(
    "cheat_sheet, expected_cheat_sheet",
    [
        pytest.param(
            CheatSheetSchema(
                title="Second entry",
                language="python",
                is_published=True,
                cards=[
                    CheatSheetContent(subtitle="card_subtitle", content="card_content")
                ],
                id="62edd29215f7ccf1b7a44b87",
            ),
            {
                "title": "Second entry",
                "language": "python",
                "is_published": True,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                "id": "62edd29215f7ccf1b7a44b87",
            },
            id="Published CS, return cheat sheet for authorized user",
        ),
        pytest.param(
            CheatSheetSchema(
                title="Second entry",
                language="python",
                is_published=False,
                cards=[
                    CheatSheetContent(subtitle="card_subtitle", content="card_content")
                ],
                id="62edd29215f7ccf1b7a44b87",
            ),
            {
                "title": "Second entry",
                "language": "python",
                "is_published": False,
                "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
                "id": "62edd29215f7ccf1b7a44b87",
            },
            id="Unpublished CS, return cheat sheet for authorized user",
        ),
    ],
)
@mock.patch("domain.cheat_sheet_domain.get_cheat_sheet")
def test_get_cheat_sheet_by_id__authorized(
    mock_get_cheat_sheet: MagicMock,
    cheat_sheet: CheatSheetSchema,
    expected_cheat_sheet: dict,
) -> None:
    app.dependency_overrides[authentication.optional_auth_wrapper] = _mock_auth_wrapper
    mock_get_cheat_sheet.return_value = cheat_sheet

    response = client.get("/api/cheat_sheets/62edd29215f7ccf1b7a44b87")
    assert response.status_code == 200
    assert response.json() == expected_cheat_sheet
    mock_get_cheat_sheet.assert_called_with(cheat_sheet_id="62edd29215f7ccf1b7a44b87")

    app.dependency_overrides = {}


def test_post_cheat_sheet__non_authorized() -> None:
    response = client.post(
        "/api/cheat_sheets",
        json={
            "title": "Second entry",
            "language": "python",
            "is_published": True,
            "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
        },
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}


@pytest.mark.parametrize(
    "unsaved_cheat_sheet, expected_cheat_sheet_id",
    [
        pytest.param(
            UnsavedCheatSheetSchema(
                title="Second entry",
                language="python",
                is_published=True,
                cards=[
                    CheatSheetContent(subtitle="card_subtitle", content="card_content")
                ],
            ),
            {"id": "62edd29215f7ccf1b7a44b87"},
            id="Create cheat sheet",
        ),
    ],
)
@mock.patch("domain.cheat_sheet_domain.create_cheat_sheet")
def test_post_cheat_sheet__authorized(
    mock_create_cheat_sheet: MagicMock,
    unsaved_cheat_sheet: UnsavedCheatSheetSchema,
    expected_cheat_sheet_id: dict,
) -> None:
    app.dependency_overrides[authentication.auth_wrapper] = _mock_auth_wrapper
    mock_create_cheat_sheet.return_value = expected_cheat_sheet_id

    response = client.post("/api/cheat_sheets", json=unsaved_cheat_sheet.model_dump())
    assert response.status_code == 200
    assert response.json() == expected_cheat_sheet_id
    mock_create_cheat_sheet.assert_called_with(cheat_sheet_data=unsaved_cheat_sheet)

    app.dependency_overrides = {}


def test_patch_cheat_sheet__non_authorized() -> None:
    response = client.patch(
        "/api/cheat_sheets/62edd29215f7ccf1b7a44b87",
        json={
            "title": "Second entry",
            "language": "python",
            "is_published": True,
            "cards": [{"subtitle": "card_subtitle", "content": "card_content"}],
        },
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}


@pytest.mark.parametrize(
    "cheat_sheet_data, expected_cheat_sheet",
    [
        pytest.param(
            UpdateCheatSheetSchema(
                title="Second entry",
                language="python",
                is_published=True,
                cards=[
                    CheatSheetContent(subtitle="card_subtitle", content="card_content")
                ],
            ),
            {"acknowledged": True},
            id="Update cheat sheet",
        ),
    ],
)
@mock.patch("domain.cheat_sheet_domain.patch_cheat_sheet")
def test_patch_cheat_sheet__authorized(
    mock_patch_cheat_sheet: MagicMock,
    cheat_sheet_data: UpdateCheatSheetSchema,
    expected_cheat_sheet: dict,
) -> None:
    app.dependency_overrides[authentication.auth_wrapper] = _mock_auth_wrapper
    mock_patch_cheat_sheet.return_value = expected_cheat_sheet

    response = client.patch(
        "/api/cheat_sheets/62edd29215f7ccf1b7a44b87",
        json=cheat_sheet_data.model_dump(),
    )
    assert response.status_code == 200
    assert response.json() == expected_cheat_sheet
    mock_patch_cheat_sheet.assert_called_with(
        id="62edd29215f7ccf1b7a44b87", cheat_sheet_data=cheat_sheet_data
    )

    app.dependency_overrides = {}


def test_delete_cheat_sheet__non_authorized() -> None:
    response = client.delete("/api/cheat_sheets/62edd29215f7ccf1b7a44b87")
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}


@pytest.mark.parametrize(
    "expected_result",
    [
        pytest.param({"acknowledged": True}, id="Delete cheat sheet"),
    ],
)
@mock.patch("domain.cheat_sheet_domain.delete_cheat_sheet")
def test_delete_cheat_sheet__authorized(
    mock_delete_cheat_sheet: MagicMock,
    expected_result: dict,
) -> None:
    app.dependency_overrides[authentication.auth_wrapper] = _mock_auth_wrapper
    mock_delete_cheat_sheet.return_value = expected_result

    response = client.delete("/api/cheat_sheets/62edd29215f7ccf1b7a44b87")
    assert response.status_code == 200
    assert response.json() == expected_result
    mock_delete_cheat_sheet.assert_called_with(id="62edd29215f7ccf1b7a44b87")

    app.dependency_overrides = {}
