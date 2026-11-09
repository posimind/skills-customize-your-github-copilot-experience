from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Task List API")

tasks: dict[int, dict[str, int | str | bool]] = {}
next_task_id = 1


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool


@app.get("/")
def read_root():
    # TODO: Return a short welcome message.
    pass


@app.get("/tasks")
def read_tasks():
    # TODO: Return all tasks.
    pass


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    # TODO: Create a task with the next available ID and return it.
    pass


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    # TODO: Return the requested task or raise HTTPException with status 404.
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    # TODO: Update the task or raise HTTPException with status 404.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete the task or raise HTTPException with status 404.
    pass
