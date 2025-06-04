from uuid import UUID
from fastapi import HTTPException, status

def validate_uuid(id: str) -> UUID:
    try:
        return UUID(id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid UUID format"
        )

def validate_username(username: str) -> str:
    if len(username) < 3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username must be at least 3 characters long"
        )
    return username