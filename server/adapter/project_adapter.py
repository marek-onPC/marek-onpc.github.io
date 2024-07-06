import json
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

from helpers.db_client import DatabaseClient
from schemas import ProjectSchema


load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]
db_collection_name = os.environ["DB_COLL_PROJECTS"]
db_client = DatabaseClient(db_uri, db_name)


def get_projects():
    projects = []
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_find_all(collection)

    for sample in result:
        if sample["_id"]:  
            sample["id"] = sample["_id"]
            del sample["_id"]

        projects.append(sample)
        projects.reverse()

    return json.dumps(projects, default=str)


def get_project(project_id: str):
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_find_one(collection, {
        "_id" : ObjectId(project_id)
    })

    if result["_id"]:  
        result["id"] = result["_id"]
        del result["_id"]

    return json.dumps(result, default=str)


def create_project(project_data: ProjectSchema):
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_add(collection, {
        "title": project_data.title,
        "project_type": project_data.project_type,
        "content": project_data.content
    })

    return json.dumps(result, default=str)


def patch_project(project_data: ProjectSchema):
    collection = db_client.db_connection(db_collection_name)
    result = db_client.db_update(collection, {
        "_id": project_data.id,
        "title": project_data.title,
        "project_type": project_data.project_type,
        "content": project_data.content
    })

    return json.dumps(result, default=str)
