from typing import List, Optional
from enum import IntEnum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class TaskBase(BaseModel):
    task: str = Field(..., min_length=3, description="Task to complete")
    task_description: str = Field(..., description="Information about task")
    notes: List[str] = Field(..., description="Notes about task")
    priority: Priority = Field(default=Priority.LOW, description="Task priority")


class Task(TaskBase):
    task_id: int = Field(..., description="Task unique identifier")


class CreateTask(TaskBase):
    pass


class UpdateTask(BaseModel):
    task: Optional[str] = None
    task_description: Optional[str] = None
    notes: Optional[List[str]] = []
    priority: Optional[Priority] = None


all_tasks = [
    Task(
        task_id=1,
        task="Cleaning",
        task_description="Do the dishes",
        notes=["Just do the dishes before 3pm", "All you need gonna be in garage"],
        priority=Priority.MEDIUM,
    ),
    Task(
        task_id=2,
        task="Work",
        task_description="Make new features for website",
        notes=["Add a button", "Make a theme feature"],
        priority=Priority.HIGH,
    ),
    Task(
        task_id=3,
        task="Study",
        task_description="Read the book",
        notes=["Prepare for exams", "Read chapter #12"],
        priority=Priority.LOW,
    ),
]


@app.get("/")
def hello_world():
    return {"message": "Hello world"}


@app.get("/tasks", response_model=List[Task])
def ShowTasks():
    return all_tasks


@app.get("/tasks/{task_id}", response_model=Task)
def ShowTask(task_id: int):
    for task_obj in all_tasks:
        if task_obj.task_id == task_id:
            return task_obj
    raise HTTPException(
        status_code=404, detail=f"There is no task with task_id:{task_id}"
    )


@app.post("/tasks", response_model=Task)
def createTask(task: CreateTask):
    new_task_id = max([task.task_id for task in all_tasks]) + 1

    new_task = Task(
        task_id=new_task_id,
        task=task.task,
        task_description=task.task_description,
        notes=task.notes,
        priority=task.priority,
    )

    all_tasks.append(new_task)
    return new_task


@app.put("/tasks", response_model=UpdateTask)
def updateTask(updating_task_id: int, changed_task: UpdateTask):
    for task_obj in all_tasks:
        if task_obj.task_id == updating_task_id:
            if changed_task.task != task_obj.task and changed_task.task != None:
                task_obj.task = changed_task.task
            if (
                changed_task.task_description != task_obj.task_description
                and changed_task.task_description != None
            ):
                task_obj.task_description = changed_task.task_description
            if changed_task.notes != task_obj.notes and changed_task.notes != None:
                task_obj.notes = changed_task.notes
            if (
                changed_task.priority != task_obj.priority
                and changed_task.priority != None
            ):
                task_obj.priority = changed_task.priority
            return task_obj
    raise HTTPException(
        status_code=404, detail=f"There is no task with task_id:{task_id}"
    )


@app.delete("/tasks/{task_id}")
def deleteTask(task_id: int):
    for index, task_obj in enumerate(all_tasks):
        if task_obj.task_id == task_id:
            return all_tasks.pop(index)
    raise HTTPException(
        status_code=404, detail=f"There is no task with task_id:{task_id}"
    )
