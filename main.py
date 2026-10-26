
from fastapi import FastAPI
from database import engine, Base
from routers import tasks
import models

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()

# Connect task routes
app.include_router(tasks.router)


@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI project!"}


@app.get("/health")
def health():
    return {"status": "healthy"}
