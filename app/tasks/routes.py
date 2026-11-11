import logging
from app.core.settings import SettingsDeps

from .service import TaskServiceDeps
from .schema import TaskCreateRequest, TaskCreateResponse, TaskGetResponse, TaskPath, TaskSearchParams, TaskSearchResponse
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)


@router.get(
    "/{task_id}",
    response_model=TaskGetResponse,
    summary="Get project by id",
    description="""
    Get task by id. This is description of router
            """,
)
async def get_task(
    service: TaskServiceDeps,
    path: TaskPath = Depends(),
):
    res = await service.get(path.task_id)
    return TaskGetResponse(
        id=res.id,
        title=res.title,
        description=res.description,
        is_completed=res.is_completed,
        project_id=res.project_id,
    )
    
@router.get(
    "/",
    response_model=TaskSearchResponse,
    description="""
    Task Search
            """,
)
async def search_task(
    service: TaskServiceDeps,
    params: TaskSearchParams = Depends(),
):
    tasks, total = await service.search(params)

    return TaskSearchResponse(
        items=[
            TaskGetResponse(
                id=t.id,
                title=t.title,
                description=t.description,
                is_completed=t.is_completed,
                project_id=t.project_id
            )
            for t in tasks
        ],
        total=total,
        limit=params.limit,
        offset=params.offset
    )


@router.post("/", response_model=TaskCreateResponse, status_code=201)
async def create_tasks(service: TaskServiceDeps, data: TaskCreateRequest):
    res = await service.create(data)
    return TaskCreateResponse(
        id=res.id,
        title=res.title,
        description=res.description,
        is_completed=res.is_completed,
        project_id=res.project_id,
    )
