# FastAPI TODO App

Простое in-memory TODO-приложение с REST API.

## Стек
- Python 3.11+
- FastAPI
- Pydantic
- In-memory storage (без БД)
- Repository pattern

## Функционал
- Пользователи (User)
- Проекты (Project)
- Задачи (Task)
- Валидация UUID / username / status
- CRUD через REST API

## Как запустить

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn todo_app.main:app --reload
```

Пример запроса

```bash
curl -X POST http://127.0.0.1:8000/users/  \
-H "Content-Type: application/json"  \
-d '{"username": "testuser", "email": "testuser@example.com", "password": "test123"}'
```


