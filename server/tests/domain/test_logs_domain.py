from unittest import mock

import pytest

from domain.logs_domain import get_logs
from schemas import EventTypes, LogEntry, LogID, MongoPagination


@pytest.fixture
def mock_db_client():
    with mock.patch("domain.logs_domain.db_client") as mocked_client:
        yield mocked_client


def test_get_logs_returns_logs(mock_db_client):
    # Arrange: domain uses sort("timestamp", -1) so MongoDB returns newest first
    mock_db_client.find.return_value.sort.return_value = [
        {
            "_id": "2",
            "event_type": "cheat_sheet_operation",
            "message": "Test log 2",
            "user": "user2",
            "context": {"key": "value2"},
            "timestamp": "2023-01-02T00:00:00Z",
        },
        {
            "_id": "1",
            "event_type": "login_operation",
            "message": "Test log 1",
            "user": "user1",
            "context": {"key": "value1"},
            "timestamp": "2023-01-01T00:00:00Z",
        },
    ]
    pagination = MongoPagination(skip=0, limit=2)

    # Act
    logs = get_logs(pagination)

    # Assert
    assert len(logs) == 2
    assert logs[0] == LogEntry(
        id=LogID("2"),
        event_type=EventTypes.CHEAT_SHEET_OPERATION,
        message="Test log 2",
        user="user2",
        context={"key": "value2"},
        timestamp="2023-01-02T00:00:00Z",
    )
    assert logs[1] == LogEntry(
        id=LogID("1"),
        event_type=EventTypes.LOGIN_OPERATION,
        message="Test log 1",
        user="user1",
        context={"key": "value1"},
        timestamp="2023-01-01T00:00:00Z",
    )


def test_get_logs_returns_none_when_no_logs(mock_db_client):
    # Arrange
    mock_db_client.find.return_value.sort.return_value = None
    pagination = MongoPagination(skip=0, limit=2)

    # Act
    logs = get_logs(pagination)

    # Assert
    assert logs is None


def test_get_logs_with_empty_result(mock_db_client):
    # Arrange
    mock_db_client.find.return_value.sort.return_value = []
    pagination = MongoPagination(skip=0, limit=2)

    # Act
    logs = get_logs(pagination)

    # Assert
    assert logs == []
