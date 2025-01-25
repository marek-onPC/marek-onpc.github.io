from unittest import mock
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app
from schemas import CheatSheetContent, CheatSheetSchema, Username
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
def test_cheat_sheets__non_authorized(
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
def test_cheat_sheets__authorized(
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
