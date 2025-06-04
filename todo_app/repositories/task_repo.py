from uuid import UUID
from typing import List
from todo_app.models.task import Task
from .base import BaseRepository

class TaskRepository(BaseRepository[Task]):
    def get_by_project(self, project_id: UUID) -> List[Task]:
        return [task for task in self.items.values() if task.project_id == project_id]

    def get_by_status(self, status: str) -> List[Task]:
        return [task for task in self.items.values() if task.status == status]