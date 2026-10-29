from pydantic import BaseModel, Field, model_validator, HTTPException

class RandQuery(BaseModel):
    rnd_from: int = Field(0, ge=0, le=100)
    rnd_to: int = Field(100, ge=0, le=100)
    
    @model_validator(mode="after")
    def check_from_to(self):
        if self.rnd_from > self.rnd_to:
            raise HTTPException(400,'RND FROM <= RND TO')
        return self