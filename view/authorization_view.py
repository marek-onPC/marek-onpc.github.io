from fastapi import Depends, APIRouter, HTTPException, UploadFile, File
from auth.authentication import Authentication
from domain import authorization_domain


router = APIRouter(prefix="/api")
authentication = Authentication()


@router.post("/authorization/configure")
def configure(photo: UploadFile = File(...), username = Depends(authentication.auth_wrapper)):
    if username:
        authorization_domain.add_photo(username, photo)
    else:
        raise HTTPException(status_code=401, detail="Non authenticated")
