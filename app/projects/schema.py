
from pydantic import BaseModel, Field

class ProjectCreateRequest(BaseModel):
    key: str
    name: str
    description: str | None = None