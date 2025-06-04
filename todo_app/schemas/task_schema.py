from pydantic import BaseModel
from todo_app.models.task import TaskStatus

class TaskCreate(BaseModel):
    title: str
    description: str = None
    project_id: str

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    status: TaskStatus = None

class TaskOut(BaseModel):
    id: str
    title: str
    description: str = None
    status: str
    project_id: str

    class Config:
        orm_mode = True