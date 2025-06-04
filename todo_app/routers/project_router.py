from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from typing import List
from todo_app.models.project import Project
from todo_app.schemas.project_schema import ProjectCreate, ProjectOut
from todo_app.repositories.project_repo import ProjectRepository
from todo_app.repositories.user_repo import UserRepository
from todo_app.utils.validators import validate_uuid

router = APIRouter(prefix="/projects", tags=["projects"])
repo = ProjectRepository()
user_repo = UserRepository()

@router.post("/", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate, owner_id: str):
    owner_uuid = validate_uuid(owner_id)
    if not user_repo.get_by_id(owner_uuid):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    db_project = Project(title=project.title, description=project.description, owner_id=owner_uuid)
    return repo.create(db_project)

@router.get("/", response_model=List[ProjectOut])
async def get_projects():
    return repo.get_all()

@router.get("/{project_id}", response_model=ProjectOut)
async def get_project(project_id: str):
    uuid = validate_uuid(project_id)
    project = repo.get_by_id(uuid)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return project

@router.get("/user/{user_id}", response_model=List[ProjectOut])
async def get_user_projects(user_id: str):
    return repo.get_by_owner(validate_uuid(user_id))