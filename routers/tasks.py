import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import APIRouter, HTTPException
from typing import List

from schemas import (
    TaskBase,
    TaskSchema,
    UpdateTaskSchema,
    TaskRelSchema,
)

from routers.db_conn.queries_package.task_queries import (
    get_tasks,
    get_task,
    create_task,
    delete_task,
    update_task,
)

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=List[TaskSchema])
async def get_tasks_handle(skip: int = 0, limit: int = 5) -> List[TaskSchema]:
    return await get_tasks(skip, limit)


@router.get("/{task_id}", response_model=TaskRelSchema)
async def get_task_handle(task_id: int) -> TaskRelSchema:
    res = await get_task(task_id)
    if res is not None:
        return res
    else:
        raise HTTPException(
            status_code=404, detail=f"There's no task with id:{task_id}"
        )


@router.post("/", response_model=TaskSchema)
async def create_task_handle(new_task_data: TaskBase) -> TaskSchema:
    task = await create_task(new_task_data)
    return task


@router.delete("/", response_model=TaskSchema)
async def delete_task_handle(task_id: int) -> TaskSchema:
    return await delete_task(task_id=task_id)


@router.put("/{task_id}", response_model=TaskSchema)
async def replace_task_handle(
    task_id: int, update_data: UpdateTaskSchema
) -> TaskSchema:
    return await update_task(task_id, update_data)


@router.patch("/{task_id}", response_model=TaskSchema)
async def update_task_handle(task_id: int, update_data: UpdateTaskSchema) -> TaskSchema:
    return await update_task(task_id, update_data, True)
