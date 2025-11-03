import datetime
import os
from enum import StrEnum

from celery import Celery
from dotenv import load_dotenv

from helpers.db_client import DatabaseClient

load_dotenv()
amqp_url = os.environ["AMQP_URL"]
celery_backend_db_url = os.environ["CELERY_BACKEND_DB_URI"]
db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_LOGGING"]
db_client = DatabaseClient(db_uri, db_name).connection()[db_collection_name]

celery = Celery("logger", broker=amqp_url)

EVENT_LOG_EVENT = "server.tasks.log_event"


class EventTypes(StrEnum):
    LOGIN_ATTEMPT = "login_attempt"


# ----- LOG EVENT, asynchronous logging
def send_log_event(
    event_type: EventTypes, user: str | None, message: str, context: dict | None = None
):
    now = datetime.datetime.now(datetime.timezone.utc)
    celery.send_task(
        EVENT_LOG_EVENT, args=[event_type, message, user, now.isoformat(), context]
    )


@celery.task(name=EVENT_LOG_EVENT)
def process_log_event(
    event_type: str,
    message: str,
    user: str,
    timestamp: str,
    context: dict | None = None,
):
    db_client.insert_one(
        {
            "event_type": event_type,
            "message": message,
            "user": user,
            "timestamp": timestamp,
            "context": context,
        }
    )
