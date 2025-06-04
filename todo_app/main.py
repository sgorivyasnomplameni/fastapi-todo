from fastapi import FastAPI
from todo_app.routers import user_router, project_router, task_router
from pydantic import BaseModel, Field

app = FastAPI(
    title="TODO App",
    description="Simple TODO application with FastAPI",
    version="0.1.0",
)

app.include_router(user_router.router)
app.include_router(project_router.router)
app.include_router(task_router.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to TODO App"}