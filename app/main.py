from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def root(response: Response):
    response.status_code = 204
    # return {"Score": 102}
    # return Response(status_code=201)
    return 1
