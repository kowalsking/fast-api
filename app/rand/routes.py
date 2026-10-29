from fastapi import FastAPI, Path, HTTPException, Query, Body, Request, APIRouter
import random

router = APIRouter(
    prefix="/random"
)

@router.get("/")
def get_posts(
    rnd_from: int = 0,
    rnd_to: int = 100
):
    if rnd_from > rnd_to:
        raise HTTPException(400, "rnd_from should be < rnd_to")
    return {
        "value": random.randint(rnd_from, rnd_to)
    }