from app.core.settings import SettingsDeps

from .service import TaskServiceDeps
from .schema import TaskGetResponse, TaskPath
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

router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])

@router.get(
    "/{task_id}",
    response_model=TaskGetResponse,
    summary="Get project by id",
    description="""
    Get task by id. This is description of router
            """,
)
def get_task(
    service: TaskServiceDeps,
    settings: SettingsDeps,
    path: TaskPath = Depends(),
):
    res = service.get(path.task_id)
    print(settings.db.url)
    print(settings.auth.jwt_secret)
    return TaskGetResponse(id=res)