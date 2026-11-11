from typing import Annotated
from fastapi import Depends

from app.core.db import DBSessionDeps
from app.tasks.model import Task


def get_task_repository(session: DBSessionDeps):
    return TaskRepository(session)


class TaskRepository:
    def __init__(self, session: DBSessionDeps):
        self.session = session

    async def get_by_id(self, task_id: int):
        return await self.session.get(Task, task_id)

    async def save(self, task: Task):
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task


TaskRepositoryDeps = Annotated[
    TaskRepository,
    Depends(
        get_task_repository,
    ),
]
