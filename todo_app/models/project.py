from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from typing import Optional

class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    description: Optional[str] = None
    owner_id: UUID

    class Config:
        from_attributes = True
        json_encoders = {UUID: lambda v: str(v)}
