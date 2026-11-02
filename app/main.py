from fastapi import FastAPI
from projects.routes import router as project_router

app = FastAPI(
    title="KanbanBoard API",
    description='Some smart description',
    version="0.0.1",
    openapi_tags=[
        {
            "name": "Projects",
            "description": "Project management"
        }
    ]
)

app.include_router(project_router)