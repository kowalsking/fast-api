from fastapi import FastAPI, Path, HTTPException, Query, Body, Request, APIRouter, Depends
import random
from .schema import ProjectCreateRequest, ProjectCreateResponse, ProjectPath, ProjectUpdateRequest, ProjectUpdateResponse

router = APIRouter(
    prefix="/projects"
)

@router.get("/{project_id}")
def get_project(
    path: ProjectPath = Depends()
):
    return {"id": path.project_id}

@router.patch("/{project_id}")
def update_project(
    data: ProjectUpdateRequest,
    path: ProjectPath = Depends(),
):
    # return {"id": path.project_id}
    return ProjectUpdateResponse(
        id=path.project_id,
        key="123",
        name=data.name,
        description=data.description
    )

@router.post("/", response_model=ProjectCreateResponse)
async def create_project(data: ProjectCreateRequest):
    # return {**data.model_dump(), "id": 1}
    print(data)
    return ProjectCreateResponse(
        id=1,
        name=data.name
    )