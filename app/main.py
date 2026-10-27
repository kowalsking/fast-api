from random import random

from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

class UnauthHTTPException(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, "Not authoraised")

@app.get("/posts/{post_id}")
def get_post(post_id: int = Path(ge=5)): # uuid | int | str
    return {"id": post_id}

