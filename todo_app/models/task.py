from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo
    project_id: UUID

    class Config:
        from_attributes = True
        json_encoders = {UUID: lambda v: str(v)}
