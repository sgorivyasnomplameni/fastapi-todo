from pydantic import BaseModel

class ProjectCreate(BaseModel):
    title: str
    description: str = None

class ProjectOut(BaseModel):
    id: str
    title: str
    description: str = None
    owner_id: str

    class Config:
        orm_mode = True