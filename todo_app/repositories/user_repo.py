from uuid import UUID
from typing import Optional
from todo_app.models.user import User
from .base import BaseRepository

class UserRepository(BaseRepository[User]):
    def get_by_username(self, username: str) -> Optional[User]:
        for user in self.items.values():
            if user.username == username:
                return user
        return None

    def get_by_email(self, email: str) -> Optional[User]:
        for user in self.items.values():
            if user.email == email:
                return user
        return None