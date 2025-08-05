from typing import List, Optional, Dict, Literal
from enum import IntEnum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Developer(BaseModel):
    name: str = Field(..., min_length=1, description="Developer's name", max_length=20)
    age: int = Field(..., ge=0, le=130, description="Developer's age")
    sex: Literal["male", "female"] = Field(..., description="Developer's sex")
    position: Literal["intern", "junior", "middle", "senior", "teamlead"] = Field(
        ..., description="Developer's position"
    )


class TaskBase(BaseModel):
    task: str = Field(..., min_length=3, description="Task to complete")
    task_description: str = Field(..., description="Information about task")
    notes: List[str] = Field(..., description="Notes about task")
    priority: Priority = Field(default=Priority.LOW, description="Task priority")
    developers: List[Developer] = Field(
        ..., description="Developer(s) working on this task", min_length=1
    )


class Task(TaskBase):
    task_id: int = Field(..., description="Task unique identifier")


class CreateTask(TaskBase):
    pass


class UpdateTask(BaseModel):
    task: Optional[str] = None
    task_description: Optional[str] = None
    notes: Optional[List[str]] = None
    priority: Optional[Priority] = None
    developers: Optional[List[Developer]] = None


developers: List[Developer] = [
    Developer(name="John", age=25, sex="male", position="middle"),
    Developer(name="Max", age=22, sex="female", position="junior"),
    Developer(name="Joe", age=45, sex="male", position="senior"),
]

all_tasks: List[Task] = [
    Task(
        task_id=1,
        task="Cleaning",
        task_description="Do the dishes",
        notes=["Just do the dishes before 3pm", "All you need gonna be in garage"],
        priority=Priority.MEDIUM,
        developers=[developers[1], developers[0]],
    ),
    Task(
        task_id=2,
        task="Work",
        task_description="Make new features for website",
        notes=["Add a button", "Make a theme feature"],
        priority=Priority.HIGH,
        developers=[developers[2], developers[0]],
    ),
    Task(
        task_id=3,
        task="Study",
        task_description="Read the book",
        notes=["Prepare for exams", "Read chapter #12"],
        priority=Priority.LOW,
        developers=[developers[1], developers[2]],
    ),
]


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Hello world"}


@app.get("/tasks", response_model=List[Task])
def get_tasks() -> List[Task]:
    return all_tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    for task_obj in all_tasks:
        if task_obj.task_id == task_id:
            return task_obj
    raise HTTPException(
        status_code=404, detail=f"There is no task with task_id:{task_id}"
    )


@app.get("/developers", response_model=List[Developer])
def get_developers() -> List[Developer]:
    return developers


@app.get("/tasks/{task_id}/developers", response_model=List[Developer])
def get_developers_for_task(task_id: int) -> List[Developer]:
    for task_obj in all_tasks:
        if task_obj.task_id == task_id:
            return task_obj.developers
    raise HTTPException(
        status_code=404, detail=f"There is no task with task_id:{task_id}"
    )


@app.post("/tasks", response_model=Task)
def create_task(task: CreateTask) -> Task:
    new_task_id = max([task.task_id for task in all_tasks]) + 1

    new_task = Task(task_id=new_task_id, **task)

    all_tasks.append(new_task)
    return new_task


def apply_task_update(task_id: int, update_data: dict) -> Task:
    for task in all_tasks:
        if task.task_id == task_id:
            for key, value in update_data.items():
                if getattr(task, key) != value:
                    setattr(task, key, value)
            return task
    raise HTTPException(status_code=404, detail=f"Task id {task_id} not found")


@app.put("/tasks/{task_id}", response_model=Task)
def replace_task(task_id: int, updated_task: CreateTask) -> Task:
    update_data = updated_task.model_dump()
    return apply_task_update(task_id, update_data)


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task_partial(task_id: int, partial_task: UpdateTask) -> Task:
    update_data = partial_task.model_dump(exclude_unset=True)
    return apply_task_update(task_id, update_data)


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int) -> Task:
    for index, task_obj in enumerate(all_tasks):
        if task_obj.task_id == task_id:
            return all_tasks.pop(index)
    raise HTTPException(
        status_code=404, detail=f"There is no task with task_id:{task_id}"
    )


# TODO:, Implement db with Orm such as sqlAlchemy,find a way to use websockets, and make a minimal frontend, then connect em together
