#!/bin/sh
set -e

echo "Starting with APP_TYPE=$APP_TYPE"

if [ "$APP_TYPE" = "fastapi" ]; then
    echo "Starting FastAPI server..."
    exec gunicorn -k uvicorn.workers.UvicornWorker main:app
elif [ "$APP_TYPE" = "celery" ]; then
    echo "Starting Celery worker..."
    exec poetry run celery -A main worker --loglevel=info
else
    echo "Unknown APP_TYPE=$APP_TYPE"
    exit 1
fi
