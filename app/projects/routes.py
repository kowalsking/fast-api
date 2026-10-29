from fastapi import FastAPI, Path, HTTPException, Query, Body, Request, APIRouter, Depends
import random
from .schema import ProjectCreateRequest

router = APIRouter(
    prefix="/projects"
)

@router.post("/")
async def create_project(data: ProjectCreateRequest):
    return data