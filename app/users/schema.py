from pydantic import BaseModel, Field


class UserRegisterRequest(BaseModel):
    email: str
    password: str

    model_config = {"extra": "forbid"}


class UserRegisterResponse(BaseModel):
    id: int
    email: str

