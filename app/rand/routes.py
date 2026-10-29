from fastapi import FastAPI, Path, HTTPException, Query, Body, Request, APIRouter, Depends
import random
from .schema import RandQuery

router = APIRouter(
    prefix="/random"
)

@router.get("/")
def get_posts(query: RandQuery = Depends()):
    if query.rnd_from > query.rnd_to:
        raise HTTPException(400, "rnd_from should be < rnd_to")
    return {
        "value": random.randint(query.rnd_from, query.rnd_to)
    }