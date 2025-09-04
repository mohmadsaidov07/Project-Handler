from . import *


async def get_tasks(skip: int = 0, limit: int = 5) -> List[TaskSchema]:
    async with async_session_factory() as session:
        e = aliased(Task)
        res = await session.scalars(
            select(e).where(e.id >= skip).limit(limit).order_by(e.id)
        )
        tasks = res.all()
        tasks_json = [TaskSchema.model_validate(task) for task in tasks]
        for task_json in tasks_json:
            print(task_json)
        return tasks_json


async def get_task(task_id: int) -> TaskRelSchema:
    async with async_session_factory() as session:
        task = await session.get(
            Task,
            task_id,
            options=[
                selectinload(Task.task_employees),
                selectinload(Task.task_notes),
                joinedload(Task.task_project),
            ],
        )
        if task is None:
            raise HTTPException(
                status_code=418,
                detail=f"Sry you're a teapot, there's no user with id {task_id}",
            )
        res = TaskRelSchema.model_validate(task)
        print(res)
        return res


async def delete_task(task_id: int) -> TaskSchema:
    async with async_session_factory() as session:
        task = await session.get(Task, task_id)
        if task is not None:
            deleted_task = TaskSchema.model_validate(task)
            await session.delete(task)
            await session.commit()
            return deleted_task
        else:
            raise HTTPException(
                status_code=404, detail=f"Task with id:{task_id} not found!"
            )


async def create_task(new_data: TaskBase) -> TaskSchema:
    async with async_session_factory() as session:
        mapped_data = Task(
            task_description=new_data.task_description,
            start_date=new_data.start_date,
            end_date=new_data.end_date,
            priority=new_data.priority.name,
            project_id=new_data.project_id,
        )
        session.add(mapped_data)
        await session.flush()
        await session.refresh(mapped_data)
        print(f"Added Task: {mapped_data}")

        task_json = TaskSchema.model_validate(mapped_data)

        await session.commit()

        return task_json


async def update_task(
    update_id: int, update_data: UpdateTaskSchema, partial: bool = False
) -> TaskSchema:
    async with async_session_factory() as session:
        prev_task = await session.get(Task, update_id)
        if prev_task is None:
            raise HTTPException(
                status_code=404, detail=f"Task with id:{update_id} not found"
            )

        if partial:
            update_dict = update_data.model_dump(exclude_unset=True)
        else:
            update_dict = update_data.model_dump()

        for key, val in update_dict.items():
            if key != "priority":
                setattr(prev_task, key, val)
            else:
                prev_task.priority = update_data.priority.name  # type: ignore
        await session.commit()
        await session.refresh(prev_task)

        task_json = TaskSchema.model_validate(prev_task)
        print(task_json)
        return task_json


# async def main():
#     # await create_tables()
#     # await insert_data()
#     # await create_task(
#     #     TaskBase(
#     #         task_description="do something important",
#     #         start_date="2000-01-01",
#     #         end_date="3000-01-01",
#     #         priority=Priority.high_priority,
#     #         project_id=8,
#     #     )
#     # )
#     # await get_tasks(31)
#     await update_task(31, UpdateTaskSchema(priority=3, project_id=4), partial=True)


# asyncio.run(main())
