from uuid import UUID
from typing import List
from todo_app.models.project import Project
from .base import BaseRepository

class ProjectRepository(BaseRepository[Project]):
    def get_by_owner(self, owner_id: UUID) -> List[Project]:
        return [project for project in self.items.values() if project.owner_id == owner_id]