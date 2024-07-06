from schemas import ProjectID, ProjectSchema
from adapter import project_adapter


def get_projects():
    return project_adapter.get_projects()


def get_project(project_id: ProjectID):
    return project_adapter.get_project(project_id=project_id)


def create_project(project_data: ProjectSchema):
    return project_adapter.create_project(project_data=project_data)


def patch_project(project_data: ProjectSchema):
    return project_adapter.patch_project(project_data=project_data)
