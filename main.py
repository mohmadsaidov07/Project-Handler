from typing import List, Optional, Dict, Literal, Tuple
from fastapi import FastAPI, HTTPException
from classes import *
from db_connect import get_data


app = FastAPI()


all_tasks: List[Task] = get_data("SELECT * FROM tasks;")
all_projects: List[Project] = get_data("SELECT * FROM projects;")
all_developers: List[Developer] = get_data("SELECT * FROM developers;")
all_notes: List[Note] = get_data("SELECT * FROM notes;")


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
    return all_developers


@app.get("/tasks/{task_id}/developers", response_model=List[Developer])
def get_developers_for_task(task_id: int) -> List[Developer]:
    for task_obj in all_tasks:
        if task_obj.task_id == task_id:
            return task_obj.developers
    raise HTTPException(
        status_code=404, detail=f"There is no task with task_id:{task_id}"
    )


# @app.post("/tasks", response_model=Task)
# def create_task(task: CreateTask) -> Task:
#     new_task_id = max([task.task_id for task in all_tasks]) + 1

#     new_task = Task(task_id=new_task_id, **task)

#     all_tasks.append(new_task)
#     return new_task


# def apply_task_update(task_id: int, update_data: dict) -> Task:
#     for task in all_tasks:
#         if task.task_id == task_id:
#             for key, value in update_data.items():
#                 if getattr(task, key) != value:
#                     setattr(task, key, value)
#             return task
#     raise HTTPException(status_code=404, detail=f"Task id {task_id} not found")


# @app.put("/tasks/{task_id}", response_model=Task)
# def replace_task(task_id: int, updated_task: CreateTask) -> Task:
#     update_data = updated_task.model_dump()
#     return apply_task_update(task_id, update_data)


# @app.patch("/tasks/{task_id}", response_model=Task)
# def update_task_partial(task_id: int, partial_task: UpdateTask) -> Task:
#     update_data = partial_task.model_dump(exclude_unset=True)
#     return apply_task_update(task_id, update_data)


# @app.delete("/tasks/{task_id}", response_model=Task)
# def delete_task(task_id: int) -> Task:
#     for index, task_obj in enumerate(all_tasks):
#         if task_obj.task_id == task_id:
#             return all_tasks.pop(index)
#     raise HTTPException(
#         status_code=404, detail=f"There is no task with task_id:{task_id}"
#     )


# TODO:, Implement db with Orm such as sqlAlchemy,find a way to use websockets, and make a minimal frontend, then connect em together
# TODO: add project, which will have tasks as a daughter element
