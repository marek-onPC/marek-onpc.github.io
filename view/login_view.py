from typing import Dict, Optional
from fastapi import APIRouter
from auth.authentication import Authentication
from domain import login_domain
from schemas.schemas import AuthDetails
from fastapi import UploadFile, File, Form

router = APIRouter(prefix="/api")
authentication = Authentication()


@router.post("/login")
def login(username: str = Form(...), password: str = Form(...), photo: Optional[UploadFile] = File(None)) -> Dict:
    auth_details = AuthDetails(username=username, password=password)
    return login_domain.login(auth_details=auth_details, photo=photo)
