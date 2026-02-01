import os

from dotenv import load_dotenv

from helpers.db_client import DatabaseClient
from schemas import LogEntry, LogID, MongoPagination

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_LOGGING"]
db_client = DatabaseClient(db_uri, db_name).connection()[db_collection_name]


def get_logs(paginaton: MongoPagination = MongoPagination()) -> list[LogEntry] | None:
    logs = []

    result = db_client.find(
        {},
        skip=paginaton.skip,
        limit=paginaton.limit,
    ).sort("timestamp", -1)

    if result is None:
        return None

    for entry in result:
        log = LogEntry(
            id=LogID(str(entry.get("_id"))),
            event_type=entry.get("event_type"),
            message=entry.get("message"),
            user=entry.get("user"),
            context=entry.get("context"),
        )

        logs.append(log)

    logs.reverse()

    return logs
