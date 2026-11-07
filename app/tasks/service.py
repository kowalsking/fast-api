import logging
from typing import Annotated
from .repository import TaskRepository, TaskRepositoryDeps
from fastapi import Depends

logger = logging.getLogger(__name__)

repo = TaskRepository()

def get_task_service(repo: TaskRepositoryDeps):
    return TaskService(repo)

class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def get(self, project_id: int):
        try:
            return self.repo.get_by_id(project_id)
        except ValueError as e:
            logger.error('Errorrror %s', e, exc_info=True)
            


TaskServiceDeps = Annotated[
    TaskService,
    Depends(get_task_service)
]