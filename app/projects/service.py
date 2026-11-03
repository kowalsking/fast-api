from typing import Annotated
from .repository import ProjectRepository, ProjectRepositoryDeps
from fastapi import Depends

repo = ProjectRepository()

def get_project_service(repo: ProjectRepositoryDeps):
    print('get_project_service')
    return ProjectService(repo)

class ProjectService:
    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    def get_project(self, project_id: int):
        return self.repo.get_by_id(project_id)


ProjectServiceDeps = Annotated[
    ProjectService,
    Depends(get_project_service)
]