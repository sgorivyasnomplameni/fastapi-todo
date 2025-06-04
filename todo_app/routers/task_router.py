from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from typing import List
from todo_app.models.task import Task, TaskStatus
from todo_app.schemas.task_schema import TaskCreate, TaskUpdate, TaskOut
from todo_app.repositories.task_repo import TaskRepository
from todo_app.repositories.project_repo import ProjectRepository
from todo_app.utils.validators import validate_uuid

router = APIRouter(prefix="/tasks", tags=["tasks"])
repo = TaskRepository()
project_repo = ProjectRepository()

@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    project_uuid = validate_uuid(task.project_id)
    if not project_repo.get_by_id(project_uuid):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    db_task = Task(title=task.title, description=task.description, project_id=project_uuid)
    return repo.create(db_task)

@router.get("/", response_model=List[TaskOut])
async def get_tasks():
    return repo.get_all()

@router.get("/{task_id}", response_model=TaskOut)
async def get_task(task_id: str):
    uuid = validate_uuid(task_id)
    task = repo.get_by_id(uuid)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task

@router.get("/project/{project_id}", response_model=List[TaskOut])
async def get_project_tasks(project_id: str):
    return repo.get_by_project(validate_uuid(project_id))

@router.get("/status/{status}", response_model=List[TaskOut])
async def get_tasks_by_status(status: str):
    if status not in [s.value for s in TaskStatus]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid status"
        )
    return repo.get_by_status(status)

@router.patch("/{task_id}", response_model=TaskOut)
async def update_task(task_id: str, task_update: TaskUpdate):
    uuid = validate_uuid(task_id)
    task = repo.get_by_id(uuid)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    update_data = task_update.dict(exclude_unset=True)
    # Обновляем только переданные поля
    for field, value in update_data.items():
        setattr(task, field, value)
    return repo.update(uuid, task)