from typing import Literal

import pytest

from helpers.serializers import bool_list_serializer


@pytest.mark.parametrize(
    "list_as_string, expected_result",
    [["true,false", [True, False]]],
)
def test_bool_list_serializer(
    list_as_string: str, expected_result: list[Literal[True, False]]
) -> None:
    result = bool_list_serializer(list_as_string)

    assert result == expected_result


@pytest.mark.parametrize(
    "list_as_string, expected_result",
    [[None, [True]]],
)
def test_bool_list_serializer__empty_list(
    list_as_string: None, expected_result: list[Literal[True, False]]
) -> None:
    result = bool_list_serializer(list_as_string)

    assert result == expected_result
