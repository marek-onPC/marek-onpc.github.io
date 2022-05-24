import os
from typing import Dict
from dotenv import load_dotenv
from fastapi import Depends, APIRouter
from auth.authentication import Authentication
from auth.schemas import AuthDetails
from db.db_client import DatabaseClient

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_client = DatabaseClient(db_uri, db_name)

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.get("/authpath")
def authpath(username = Depends(authentication.auth_wrapper)):
    return { "name" : username }