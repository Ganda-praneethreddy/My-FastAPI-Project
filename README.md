
# FastAPI Task Management REST API

A Python REST API built using FastAPI, SQLite, SQLAlchemy, and Pydantic to manage tasks with complete CRUD operations.

## Features

- Create new tasks
- Retrieve all tasks
- Retrieve a task by ID
- Update existing tasks
- Delete tasks
- Persistent SQLite database storage
- SQLAlchemy ORM integration
- Pydantic request and response validation
- Automatic Swagger UI documentation
- HTTP error handling (404, 409)

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn
- Swagger UI
- Git and GitHub

## Project Structure

```text
My-FastAPI-Project/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── tasks.py
├── requirements.txt
├── README.md
└── .gitignore
```

The SQLite database file (`tasks.db`) is created locally and excluded from Git.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /health | Application health check |
| POST | /tasks | Create a task |
| GET | /tasks | Retrieve all tasks |
| GET | /tasks/{task_id} | Retrieve a specific task |
| PUT | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

## Installation

Clone the repository:

```bash
git clone https://github.com/Ganda-praneethreddy/My-FastAPI-Project.git
cd My-FastAPI-Project
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn main:app --reload
```

## API Documentation

Open Swagger UI:

http://127.0.0.1:8000/docs

## Example: Create a Task

POST `/tasks`

Request body:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Build REST APIs with SQLite",
  "completed": false
}
```

Successful response: HTTP 201 Created

## Database Integration

SQLite provides persistent local storage.

SQLAlchemy ORM is used to:
- Create database tables
- Insert new records
- Retrieve stored records
- Update existing records
- Delete records

Pydantic schemas validate incoming API requests and serialize responses.

## Project Status

Implemented:
- FastAPI REST API
- CRUD operations
- SQLite database integration
- SQLAlchemy ORM
- Pydantic schemas
- Swagger UI testing
- GitHub version control

Future improvements:
- Automated API testing with pytest
- Authentication and authorization
- Docker containerization
- Cloud deployment


