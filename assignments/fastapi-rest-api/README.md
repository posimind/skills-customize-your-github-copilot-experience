# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that manages tasks in memory. Practice defining HTTP endpoints, validating request data with Pydantic, and returning appropriate status codes and error responses.

## 📝 Tasks

### 🛠️ Create the API and List Tasks

#### Description
Use the provided starter code to create a FastAPI application for a simple task list. Install the dependencies with `python -m pip install fastapi uvicorn`, then start the server and implement endpoints that let a client check the API and retrieve all tasks.

#### Requirements
Completed program should:

- Create a FastAPI application in `starter-code.py`
- Return a short message from `GET /`
- Return all tasks as JSON from `GET /tasks` (an empty list is fine at first)
- Run locally with `uvicorn starter-code:app --reload` and open the interactive API docs at `/docs`


### 🛠️ Create and Retrieve Tasks

#### Description
Add endpoints to create a task and retrieve one task by its ID. Use the provided Pydantic model to validate incoming task data.

#### Requirements
Completed program should:

- Accept `POST /tasks` with a task title and optional `completed` value, defaulting to `false`
- Validate that the title is not empty
- Assign each new task a unique integer ID and return the created task as JSON
- Return a task from `GET /tasks/{task_id}`, or respond with HTTP 404 when the ID does not exist

Example request:

```json
{
  "title": "Read about HTTP methods",
  "completed": false
}
```


### 🛠️ Update and Delete Tasks

#### Description
Complete the task API by allowing clients to update a task's title or completion status, and delete tasks they no longer need.

#### Requirements
Completed program should:

- Accept `PUT /tasks/{task_id}` with a title and completion status, then return the updated task
- Accept `DELETE /tasks/{task_id}` and return a success response
- Return HTTP 404 when attempting to update or delete a task that does not exist
- Keep the API data in memory while the server is running; restarting the server may clear it
