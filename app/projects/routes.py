from .repository import ProjectRepositoryDeps

from .service import ProjectService, ProjectServiceDeps, get_project_service
from fastapi import (
    FastAPI,
    Path,
    HTTPException,
    Query,
    Body,
    Request,
    APIRouter,
    Depends,
)
import random
from .schema import (
    ProjectCreateRequest,
    ProjectCreateResponse,
    ProjectGetResponse,
    ProjectPath,
    ProjectUpdateRequest,
    ProjectUpdateResponse,
)

router = APIRouter(prefix="/v1/projects", tags=["Projects"])


@router.get(
    "/{project_id}",
    response_model=ProjectGetResponse,
    summary="Get project by id",
    description="""
    Get project by id. This is description of router
            """,
)
async def get_project(
    service: ProjectServiceDeps,
    path: ProjectPath = Depends(),
):
    project = await service.get(path.project_id)
    if project is None:
        raise HTTPException(404, "Project not found")
    return ProjectGetResponse(
        id=project.id,
        key=project.key,
        name=project.name,
        description=project.description,
    )


@router.delete(
    "/{project_id}",
    description="""
    Delete project by id. This is description of router
            """,
)
async def delete_project(
    service: ProjectServiceDeps,
    path: ProjectPath = Depends(),
):
    success = await service.delete(path.project_id)
    if not success:
        raise HTTPException(404, "Project not found")


@router.patch("/{project_id}")
async def update_project(
    data: ProjectUpdateRequest,
    service: ProjectServiceDeps,
    path: ProjectPath = Depends(),
):
    project = await service.update(path.project_id, data)
    if project is None:
        raise HTTPException(404, "Project not found")
    return ProjectUpdateResponse(
        id=project.id,
        key=project.key,
        name=project.name,
        description=project.description,
    )


@router.post("/", response_model=ProjectCreateResponse, status_code=201)
async def create_project(service: ProjectServiceDeps, data: ProjectCreateRequest):
    res = await service.create(data)
    return ProjectCreateResponse(id=res.id, name=res.name)
