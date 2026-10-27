from random import random

from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse

app = FastAPI()

class UnauthHTTPException(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, "Not authoraised")

@app.get("/") # response_class=HTMLResponse | PlainTextResponse | JSONResponse
def root(response: Response):
    num = random()
    response.status_code = 201
    return HTMLResponse(status_code=200, content="<h1>Hola!</h1>")

