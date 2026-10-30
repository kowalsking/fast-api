from fastapi import FastAPI, Path, HTTPException, Query, Body, Request, APIRouter, Depends
import random
from .schema import ProjectCreateRequest, ProjectCreateResponse

router = APIRouter(
    prefix="/projects"
)

@router.post("/", response_model=ProjectCreateResponse)
async def create_project(data: ProjectCreateRequest):
    # return {**data.model_dump(), "id": 1}
    print(data)
    return ProjectCreateResponse(
        id=1,
        name=data.name
    )