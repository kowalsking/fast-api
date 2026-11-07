import logging
from app.core.settings import SettingsDeps

from .service import TaskServiceDeps
from .schema import TaskGetResponse, TaskPath
from fastapi import (
    APIRouter,
    Depends,
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
def get_task(
    service: TaskServiceDeps,
    path: TaskPath = Depends(),
):
    res = service.get(path.task_id)
    logger.info("ID: %s", res, extra={"user_id": 1})
    return TaskGetResponse(id=res)