from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from typing import List
from todo_app.models.user import User
from todo_app.schemas.user_schema import UserCreate, UserOut
from todo_app.repositories.user_repo import UserRepository
from todo_app.utils.validators import validate_username, validate_uuid

router = APIRouter(prefix="/users", tags=["users"])
repo = UserRepository()

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    validate_username(user.username)
    if repo.get_by_username(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    if repo.get_by_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    # В реальном приложении нужно хешировать пароль!
    db_user = User(username=user.username, email=user.email, hashed_password=user.password)
    return repo.create(db_user)

@router.get("/", response_model=List[UserOut])
async def get_users():
    return repo.get_all()

@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: str):
    uuid = validate_uuid(user_id)
    user = repo.get_by_id(uuid)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user