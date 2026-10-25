# My FastAPI Project

A Python REST API learning project built using FastAPI.

## Features

- REST API development using Python and FastAPI
- Home endpoint to return a welcome message
- Health check endpoint to monitor application status
- Interactive API documentation using Swagger UI
- Automatic request and response handling

## Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- REST APIs
- Swagger UI
- Git and GitHub

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns a welcome message |
| GET | `/health` | Returns application health status |
| GET | `/docs` | Interactive API documentation |

## Installation

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

Start the application:

```bash
py -m uvicorn main:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

## Project Status

Initial FastAPI application completed. Additional backend features and tests are planned.

## Learning Reference

This is an independently created learning application. Corey Schafer's FastAPI course is used as a learning reference.

Original course: https://github.com/CoreyMSchafer/FastAPI-Full-Course
