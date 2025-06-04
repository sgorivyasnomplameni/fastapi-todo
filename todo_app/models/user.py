from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    username: str
    email: str
    hashed_password: str
    is_active: bool = True

    class Config:
        from_attributes = True
        json_encoders = {UUID: lambda v: str(v)}
