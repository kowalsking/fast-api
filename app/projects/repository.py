from typing import Annotated
from .db import DbSessionDeps
from fastapi import Depends

def get_project_repository(db: DbSessionDeps):
    print('get_project_repository')
    return ProjectRepository()


class ProjectRepository():
    def get_by_id(self, project_id: int):
        return project_id


ProjectRepositoryDeps = Annotated[
    ProjectRepository,
    Depends(get_project_repository,)
]