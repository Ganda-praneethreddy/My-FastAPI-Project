




def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to my FastAPI project!"
    }


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_all_tasks(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task(client):
    new_task = {
        "id": 100,
        "title": "Learn API Testing",
        "description": "Testing POST endpoint with pytest",
        "completed": False
    }

    response = client.post("/tasks", json=new_task)

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 100
    assert data["title"] == "Learn API Testing"
    assert data["description"] == "Testing POST endpoint with pytest"
    assert data["completed"] is False


def test_get_task_by_id(client):
    new_task = {
        "id": 101,
        "title": "Learn GET API Testing",
        "description": "Testing GET task by ID",
        "completed": False
    }

    create_response = client.post("/tasks", json=new_task)
    assert create_response.status_code == 201

    response = client.get("/tasks/101")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 101
    assert data["title"] == "Learn GET API Testing"
    assert data["description"] == "Testing GET task by ID"
    assert data["completed"] is False


    
def test_update_task(client):
    new_task = {
        "id": 102,
        "title": "Learn PUT Testing",
        "description": "Original task description",
        "completed": False
    }

    create_response = client.post("/tasks", json=new_task)
    assert create_response.status_code == 201

    updated_task = {
        "id": 102,
        "title": "PUT Testing Completed",
        "description": "Successfully updated task using pytest",
        "completed": True
    }

    response = client.put("/tasks/102", json=updated_task)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 102
    assert data["title"] == "PUT Testing Completed"
    assert data["description"] == "Successfully updated task using pytest"
    assert data["completed"] is True


def test_delete_task(client):
    new_task = {
        "id": 103,
        "title": "Learn DELETE Testing",
        "description": "Testing DELETE endpoint with pytest",
        "completed": False
    }

    create_response = client.post("/tasks", json=new_task)
    assert create_response.status_code == 201

    response = client.delete("/tasks/103")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Task deleted successfully"
    }

    get_response = client.get("/tasks/103")

    assert get_response.status_code == 404
    assert get_response.json() == {
        "detail": "Task not found"
    }


def test_get_nonexistent_task(client):
    response = client.get("/tasks/99999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Task not found"
    }


def test_create_duplicate_task(client):
    new_task = {
        "id": 104,
        "title": "Duplicate Task Test",
        "description": "Testing duplicate task ID",
        "completed": False
    }

    first_response = client.post("/tasks", json=new_task)
    assert first_response.status_code == 201

    second_response = client.post("/tasks", json=new_task)

    assert second_response.status_code == 409
    assert second_response.json() == {
        "detail": "Task ID already exists"
    }


def test_create_invalid_task(client):
    invalid_task = {
        "id": 105,
        "title": "Invalid Task",
        "description": "Testing invalid data",
        "completed": "not_a_boolean"
    }

    response = client.post("/tasks", json=invalid_task)

    assert response.status_code == 422
    assert "detail" in response.json()


def test_update_nonexistent_task(client):
    updated_task = {
        "id": 99999,
        "title": "Nonexistent Task",
        "description": "Testing update of missing task",
        "completed": True
    }

    response = client.put(
        "/tasks/99999",
        json=updated_task
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Task not found"
    }


def test_delete_nonexistent_task(client):
    response = client.delete("/tasks/99999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Task not found"
    }



def test_update_task_id_mismatch(client):
    new_task = {
        "id": 100,
        "title": "Existing Task",
        "description": "Testing ID mismatch",
        "completed": False
    }

    create_response = client.post("/tasks", json=new_task)
    assert create_response.status_code == 201

    updated_task = {
        "id": 999,
        "title": "Updated Task",
        "description": "Different task ID",
        "completed": True
    }

    response = client.put("/tasks/100", json=updated_task)

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Task ID in body must match URL"
    }
