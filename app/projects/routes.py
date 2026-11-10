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
def get_project(
    service: ProjectServiceDeps,
    path: ProjectPath = Depends(),
):
    res = service.get(path.project_id)
    return ProjectGetResponse(id=res)


@router.patch("/{project_id}")
def update_project(
    data: ProjectUpdateRequest,
    path: ProjectPath = Depends(),
):
    # return {"id": path.project_id}
    return ProjectUpdateResponse(
        id=path.project_id, key="123", name=data.name, description=data.description
    )


@router.post("/", response_model=ProjectCreateResponse, status_code=201)
async def create_project(service: ProjectServiceDeps, data: ProjectCreateRequest):
    res = await service.create(data)
    return ProjectCreateResponse(id=res.id, name=res.name)
