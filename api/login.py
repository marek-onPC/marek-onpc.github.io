import os
from typing import Dict
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from auth.authentication import Authentication
from auth.schemas import AuthDetails
from db.db_client import DatabaseClient

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_client = DatabaseClient(db_uri, db_name)

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.post("/login")
def login(auth_details: AuthDetails) -> Dict:
    collection_name = "users"
    collection = db_client.db_connection(collection_name)

    user = collection.find_one({
        "user": auth_details.username
    })

    if user is None:
        raise HTTPException(status_code=401, detail="Wrong user")

    if not authentication.verify_password(auth_details.password, user["password"]):
        raise HTTPException(status_code=401, detail="Wrong password")
    
    token = authentication.encode_jwt(user["user"])

    return { "token" : token }
