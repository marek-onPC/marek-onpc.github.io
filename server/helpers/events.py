import datetime
import os

from celery import Celery
from dotenv import load_dotenv
from typing_extensions import override

from helpers.db_client import DatabaseClient
from schemas import EventTypes

load_dotenv()
amqp_url = os.environ["AMQP_URL"]
celery_backend_db_url = os.environ["CELERY_BACKEND_DB_URI"]
db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_LOGGING"]
db_client = DatabaseClient(db_uri, db_name).connection()[db_collection_name]


FEATURE_ASYNC_LOGGING = os.environ.get("FEATURE_ASYNC_LOGGING", "False") == "True"
EVENT_LOG_EVENT = "server.tasks.log_event"
celery: Celery | None = None


def send_log_event(
    event_type: EventTypes, user: str | None, message: str, context: dict | None = None
): ...


if FEATURE_ASYNC_LOGGING:
    celery = Celery("logger", broker=amqp_url)

    # ----- LOG EVENT, asynchronous logging
    @override
    def send_log_event(
        event_type: EventTypes,
        user: str | None,
        message: str,
        context: dict | None = None,
    ):
        """
        This function is sending a async AMQP task 'log event' to store server logs in DB.

        If FEATURE_ASYNC_LOGGING flag is OFF, no log is send.
        """
        now = datetime.datetime.now(datetime.timezone.utc)

        if FEATURE_ASYNC_LOGGING:
            celery.send_task(
                EVENT_LOG_EVENT,
                args=[event_type, message, now.isoformat(), user, context],
            )
        else:
            print("FEATURE_ASYNC_LOGGING flag is OFF, no async task enqueued.")

    @celery.task(name=EVENT_LOG_EVENT)
    def process_log_event(
        event_type: str,
        message: str,
        timestamp: str,
        user: str | None = None,
        context: dict | None = None,
    ):
        db_client.insert_one(
            {
                "event_type": event_type,
                "message": message,
                "timestamp": timestamp,
                "user": user,
                "context": context,
            }
        )

else:
    print("FEATURE_ASYNC_LOGGING flag is OFF, no async task enqueued.")
