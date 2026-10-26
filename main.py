from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from database import Base, engine
from logger import logger
from routers import tasks

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()

# Connect task routes
app.include_router(tasks.router)


@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {"message": "Welcome to my FastAPI project!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(
        f"HTTP {exc.status_code} - {request.method} "
        f"{request.url.path} - {exc.detail}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code
        },
        headers=exc.headers
    )
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.exception(
        f"Unexpected error: {request.method} {request.url.path}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "status_code": 500
        }
    )
