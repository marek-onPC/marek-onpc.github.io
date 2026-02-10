from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from schemas import LogEntry, MongoPagination, EventTypes,LogID, Username
from unittest.mock import MagicMock
from view.logs_view import authentication


client = TestClient(app)


def _mock_auth_wrapper() -> Username:
    return Username("test_user")


@patch("domain.logs_domain.get_logs")
def test_get_logs_success(mock_get_logs: MagicMock):
    app.dependency_overrides[authentication.auth_wrapper] = _mock_auth_wrapper
    mock_get_logs.return_value = [
        LogEntry(id=LogID("1"), event_type=EventTypes.CHEAT_SHEET_OPERATION,  message="Log 1", context={"timestamp": "2023-01-01T00:00:00Z"}),
        LogEntry(id=LogID("2"), event_type=EventTypes.LOGIN_OPERATION, message="Log 2", context={"timestamp": "2023-01-01T00:00:00Z"}),
    ]

    pagination_params = {
        "skip": 0,
        "limit": 10
    }

    response = client.get("/api/logs", params=pagination_params)

    assert response.status_code == 200
    assert response.json() == [
        {"id": "1", "event_type": "cheat_sheet_operation", "message": "Log 1", "context": {"timestamp": "2023-01-01T00:00:00Z"}, "user": None},
        {"id": "2", "event_type": "login_operation", "message": "Log 2", "context": {"timestamp": "2023-01-01T00:00:00Z"}, "user": None},
    ]
    mock_get_logs.assert_called_once_with(paginaton=MongoPagination(**pagination_params))
    app.dependency_overrides = {}

def test_get_logs_unauthorized():
    # Ensure no auth override so real auth runs and returns 403
    app.dependency_overrides.pop(authentication.auth_wrapper, None)

    # Define pagination parameters (MongoPagination uses skip/limit)
    pagination_params = {
        "skip": 0,
        "limit": 10
    }

    # Make the request and assert the exception
    response = client.get("/api/logs", params=pagination_params)
    assert response.status_code == 403
