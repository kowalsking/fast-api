from fastapi import FastAPI
from app.projects.routes import router as project_router
from app.tasks.routes import router as task_router

app = FastAPI(
    title="KanbanBoard API",
    description="Some smart description",
    version="0.0.1",
    openapi_tags=[
        {"name": "Projects", "description": "Project management"},
        {"name": "Tasks", "description": "Tasks handler"}
    ],
)

app.include_router(project_router)
app.include_router(task_router)
