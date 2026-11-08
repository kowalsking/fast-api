import logging
from app.core.db import check_db
from app.core.settings import SettingsDeps

from .service import TaskServiceDeps
from .schema import TaskGetResponse, TaskPath
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
    data = await check_db()
    logger.info("DB check: %s", data)
    res = service.get(path.task_id)
    if not res:
        raise HTTPException(404, "Not found")
    logger.info("ID: %s", res, extra={"user_id": 1})
    return TaskGetResponse(id=res)