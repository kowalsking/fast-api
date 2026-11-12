from pydantic import BaseModel, Field


class UserLoginRequest(BaseModel):
    email: str
    password: str

    model_config = {"extra": "forbid"}

class JWTResponse(BaseModel):
    token: str

class UserRegisterRequest(BaseModel):
    email: str
    password: str

    model_config = {"extra": "forbid"}
