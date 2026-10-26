from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from schemas import TaskCreate, TaskResponse
from database import SessionLocal
from logger import logger


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    
@router.post("/", response_model=TaskResponse, status_code=201)
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

    logger.info(f"Task created successfully: ID {new_task.id}")

    return new_task


@router.get("/", response_model=list[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()

    logger.info(f"Retrieved all tasks: Count {len(tasks)}")


    return tasks


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    logger.info(f"Retrieved task: ID {task.id}")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
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

    logger.info(f"Updated task successfully: ID {existing_task.id}")
    return existing_task

@router.delete("/{task_id}", status_code=200)
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

    logger.info(f"Deleted task successfully: ID {task_id}")
    return {"message": "Task deleted successfully"}