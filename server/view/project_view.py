from fastapi import Depends, APIRouter, HTTPException
from helpers.authentication import Authentication
from domain import project_domain
from schemas import ProjectID, ProjectSchema, Username


router = APIRouter(prefix="/api")
authentication = Authentication()


@router.get("/projects")
def projects():
    return project_domain.get_projects()


@router.get("/projects/{project_id}")
def get_project_by_id(project_id: ProjectID):
    return project_domain.get_project(project_id=project_id)


@router.post("/projects")
def post_project(project_data: ProjectSchema, username: Username = Depends(authentication.auth_wrapper)):
    if username:
        if project_data.id == "":
            return project_domain.create_project(project_data=project_data)
        else:
            return project_domain.patch_project(project_data=project_data)
    else:
        raise HTTPException(status_code=401, detail="Non authenticated")
