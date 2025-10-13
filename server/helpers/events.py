from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()
amqp_url = os.environ["AMQP_URL"]
celery_backend_db_url = os.environ["CELERY_BACKEND_DB_URI"]

celery = Celery(
    'logger',
    broker=amqp_url,
    backend=celery_backend_db_url
)

EVENT_LOG_EVENT = "server.tasks.log_event"


def log_event(event_type: str, description: str):
    celery.send_task(EVENT_LOG_EVENT, args=[event_type, description])


@celery.task(name=EVENT_LOG_EVENT)
def process_log_event(event_type: str, description: str):
    # TODO - implement the actual logging logic, saving logs to a database
    print(f"Event Type: {event_type}, Description: {description}")
