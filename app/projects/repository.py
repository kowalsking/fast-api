import logging
from typing import Annotated
from fastapi import Depends

from app.core.db import DBSessionDeps
from app.projects.model import Project

logger = logging.getLogger(__name__)

class ProjectRepository():
    def __init__(self, session: DBSessionDeps):
        self.session = session
        
    def get_by_id(self, project_id: int):
        return project_id
    
    async def create(self):
        project = Project(
            key="wz",
            name="Wazar",
            description="Ecommerce OS"
        )
        self.session.add(project)
        await self.session.commit()
        await self.session.refresh(project)
        logger.info(project)


def get_project_repository(session: DBSessionDeps):
    return ProjectRepository(session)


ProjectRepositoryDeps = Annotated[
    ProjectRepository,
    Depends(get_project_repository,)
]