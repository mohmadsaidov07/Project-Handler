from sqlalchemy import select, func, Integer, label
from sqlalchemy.orm import selectinload, joinedload, aliased
from .db_models import Task, Note, Employee, Project, TasksEmployees
from schemas import (
    EmployeeSchema,
    TaskSchema,
    NoteSchema,
    EmployeeRelSchema,
    UpdateEmployeeSchema,
)
from .db_setup import (
    async_session_factory,
    async_engine,
    sync_engine,
    sync_session_factory,
    Base,
)
import asyncio
from .test_data import projects, tasks, employees, notes, tasks_employees
from typing import List, Dict, Sequence, Tuple, no_type_check, Optional, Any
from fastapi import HTTPException


async def create_tables() -> None:
    async_engine.echo = False
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async_engine.echo = True


async def insert_data() -> None:
    async_engine.echo = False
    async with async_session_factory() as session:
        session.add_all([*projects, *tasks, *employees])
        await session.flush()
        session.add_all([*notes, *tasks_employees])
        await session.commit()
    async_engine.echo = True


"""

EMPLOYEES TABLE MANIPULATION

"""


async def get_employees(skip: int = 0, limit: int = 5) -> List[EmployeeSchema]:
    async with async_session_factory() as session:
        e = aliased(Employee)
        res = await session.scalars(
            select(e).where(e.id >= skip).limit(limit).order_by(e.id)
        )
        employees = res.all()
        employees_json = [
            EmployeeSchema.model_validate(employee) for employee in employees
        ]
        for employee_json in employees_json:
            print(employee_json)
        return employees_json


async def get_employee(employee_id: int) -> EmployeeRelSchema:
    async with async_session_factory() as session:
        employee = await session.get(
            Employee,
            employee_id,
            options=(
                selectinload(Employee.employee_tasks),
                selectinload(Employee.employee_notes),
            ),
        )
        if employee is None:
            raise HTTPException(
                status_code=418,
                detail=f"Sry you're a teapot, there's no user with id {employee_id}",
            )
        res = EmployeeRelSchema.model_validate(employee)
        print(res)
        return res


async def delete_employee(employee_id: int) -> EmployeeSchema:
    async with async_session_factory() as session:
        employee = await session.get(Employee, employee_id)
        if employee is not None:
            deleted_employee = EmployeeSchema.model_validate(employee)
            await session.delete(employee)
            await session.commit()
            return deleted_employee
        else:
            raise HTTPException(
                status_code=404, detail=f"Employee with id:{employee_id} not found!"
            )


async def create_employee(
    first_name: str, last_name: str, salary: int, is_working: bool = False
) -> EmployeeSchema:
    async with async_session_factory() as session:
        new_employee = Employee(
            first_name=first_name.title().strip(),
            last_name=last_name.title().strip(),
            salary=salary,
            is_working=is_working,
        )
        session.add(new_employee)
        await session.flush()
        await session.refresh(new_employee)
        print(f"Added employee: {new_employee}")
        employee_data = {
            "id": new_employee.id,
            "first_name": new_employee.first_name,
            "last_name": new_employee.last_name,
            "salary": new_employee.salary,
            "is_working": bool(new_employee.is_working),
        }
        employee_json = EmployeeSchema.model_validate(employee_data)

        await session.commit()

        return employee_json


async def update_employee(
    update_id: int, update_data: UpdateEmployeeSchema, partial: bool = False
) -> EmployeeSchema:
    async with async_session_factory() as session:
        prev_employee = await session.get(Employee, update_id)
        if prev_employee is None:
            raise HTTPException(
                status_code=404, detail=f"Employee with id:{update_id} not found"
            )
        if not partial:
            update_dict = update_data.model_dump()
        else:
            update_dict = update_data.model_dump(exclude_unset=True)

        for key, val in update_dict.items():
            setattr(prev_employee, key, val)

        await session.commit()
        await session.refresh(prev_employee)

        employee_json = EmployeeSchema.model_validate(prev_employee)
        print(employee_json)
        return employee_json


async def project_avg_salary() -> List[Dict[str, Any]]:
    async with async_session_factory() as session:
        t = aliased(Task)
        p = aliased(Project)
        subquery = (
            select(
                t.project_id.label("project_id"),
                func.avg(Employee.salary).cast(Integer).label("project_avg_salary"),
            )
            .join(t.task_employees)
            .group_by(t.project_id)
            .order_by(t.project_id)
            .subquery()
        )

        query = select(p.id, p.project_name, subquery.c.project_avg_salary).join(
            p, p.id == subquery.c.project_id
        )

        res = await session.execute(query)
        res_dict = []
        for row in res:
            print(row._asdict())
            res_dict.append(row._asdict())
        return res_dict


# async def main():
#     # await create_tables()
#     # await insert_data()
#     # await create_employee("Patrick", "Bateman", 1_000_000, 1)
#     # await update_employee(84, salary=999_999)
#     await project_avg_salary()


# asyncio.run(main())
