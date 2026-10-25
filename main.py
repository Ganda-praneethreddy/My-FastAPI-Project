from tasks import Task
from fastapi import HTTPException

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI project!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# Temporary in-memory storage
tasks_db = {}

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    if task.id in tasks_db:
        raise HTTPException(
            status_code=409,
            detail="Task ID already exists"
        )

    tasks_db[task.id] = task
    return task


@app.get("/tasks")
def get_all_tasks():
    return list(tasks_db.values())


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks_db[task_id]


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if updated_task.id != task_id:
        raise HTTPException(
            status_code=400,
            detail="Task ID in body must match URL"
        )

    tasks_db[task_id] = updated_task
    return updated_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    del tasks_db[task_id]

    return {"message": "Task deleted successfully"}