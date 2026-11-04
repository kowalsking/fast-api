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
    path: TaskPath = Depends(),
):
    return TaskGetResponse(id=path.task_id)