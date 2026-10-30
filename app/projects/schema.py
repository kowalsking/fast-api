
from fastapi import HTTPException
from pydantic import BaseModel, field_validator, Field

class ProjectPath(BaseModel):
    project_id: int = Field(ge=0)

class ProjectCreateRequest(BaseModel):
    key: str
    name: str
    description: str | None = None
    
    model_config = {
        "extra": "forbid"
    }
    
    @field_validator("key")
    @classmethod
    def key_note_empty(cls, value):
        if not value.strip():
            raise HTTPException(400, "key must be valid string")
        return value
    
class ProjectCreateResponse(BaseModel):
    id: int
    name: str