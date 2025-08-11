from fastapi import APIRouter, HTTPException
from typing import List
from classes import Task, CreateTask, UpdateTask
from db_connect import get_data, connect_sql


router = APIRouter(prefix="/tasks", tags=["tasks"])

all_tasks: List[Task] = get_data("SELECT * FROM tasks;")


@router.get("/", response_model=List[Task])
def get_tasks() -> List[Task]:
    return all_tasks


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    for task in all_tasks:
        if task.task_id == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"There is no task with id:{task_id}")


@router.post("/", response_model=CreateTask)
def create_task(task: CreateTask, task_id: int = None) -> CreateTask:
    conn = connect_sql()
    cursor = conn.cursor()
    cursor.execute(
        f"""INSERT INTO tasks({"task_id, " if task_id != None else ""}task_description, start_date, end_date, priority, project_id)
                    VALUES({f"{task_id}, " if task_id != None else ""}
                        {", ".join(
                            repr(getattr(task, attr)) 
                        if attr not in ["start_date", "end_date"] 
                        else 
                            repr((getattr(task, attr)).strftime('%Y-%m-%d')) 
                    for attr in task.__dict__.keys()
                                    )
                    });"""
    )
    cursor.execute(
        "SELECT setval('tasks_task_id_seq', (SELECT MAX(task_id) FROM tasks))"
    )
    conn.commit()
    cursor.close()
    conn.close()
    return task


@router.delete("/", response_model=Task)
def delete_developer(task_id: int) -> Task:
    for task_obj in all_tasks:
        if task_obj.task_id == task_id:
            conn = connect_sql()
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM tasks WHERE task_id = {task_id}")

            conn.commit()
            cursor.close()
            conn.close()
            return task_obj
    raise HTTPException(
        status_code=404,
        detail=f"There is no task with task_id:{task_id}",
    )


def apply_task_update(task_id: int, update_data: dict) -> Task:
    for task in all_tasks:
        if task.task_id == task_id:
            conn = connect_sql()
            cursor = conn.cursor()
            for key, value in update_data.items():
                if getattr(task, key) != value:
                    if key not in ["start_date", "end_date"]:
                        cursor.execute(
                            f"UPDATE tasks SET {key} = {repr(value)} WHERE task_id = {task_id}"
                        )
                    else:
                        cursor.execute(
                            f"UPDATE tasks SET {key} = {repr((value.strftime('%Y-%m-%d')))} WHERE task_id = {task_id}"
                        )

                    conn.commit()
            cursor.close()
            conn.close()
            return task
    raise HTTPException(status_code=404, detail=f"task id {task_id} not found")


@router.put("/{task_id}", response_model=Task)
def replace_task(task_id: int, updated_task: CreateTask) -> Task:
    update_data = updated_task.model_dump()
    return apply_task_update(task_id, update_data)


@router.patch("/{task_id}", response_model=Task)
def update_task_partial(task_id: int, partial_task: UpdateTask) -> Task:
    update_data = partial_task.model_dump(exclude_unset=True)
    return apply_task_update(task_id, update_data)
