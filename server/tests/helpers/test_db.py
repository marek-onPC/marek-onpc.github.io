from helpers.db_client import DatabaseClient


def test_db_client_is_singleton() -> None:
    db_client = DatabaseClient("mongodb://localhost:27017", "test_db", "test_collection")
    new_db_client = DatabaseClient("mongodb://localhost:27017", "test_db", "test_collection")
    
    assert db_client is new_db_client, "DatabaseClient should be a singleton instance"
