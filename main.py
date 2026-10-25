

from schemas import TaskCreate, TaskResponse


from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal



from database import engine, Base
import models
Base.metadata.create_all(bind=engine)

from tasks import Task
from fastapi import HTTPException

from fastapi import FastAPI

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI project!"}

@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):

    existing_task = db.query(models.Task).filter(
        models.Task.id == task.id
    ).first()

    if existing_task:
        raise HTTPException(
            status_code=409,
            detail="Task ID already exists"
        )

    new_task = models.Task(
        id=task.id,
        title=task.title,
        description=task.description,
        completed=task.completed
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task



@app.get("/tasks", response_model=list[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks



@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task




@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskCreate, db: Session = Depends(get_db)):

    existing_task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if updated_task.id != task_id:
        raise HTTPException(
            status_code=400,
            detail="Task ID in body must match URL"
        )

    existing_task.title = updated_task.title
    existing_task.description = updated_task.description
    existing_task.completed = updated_task.completed

    db.commit()
    db.refresh(existing_task)

    return existing_task




@app.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id: int, db: Session = Depends(get_db)):

    existing_task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(existing_task)
    db.commit()

    return {"message": "Task deleted successfully"}
