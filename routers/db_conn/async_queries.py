from sqlalchemy import select, func, Integer, label
from sqlalchemy.orm import selectinload, joinedload, aliased
from .db_models import Task, Note, Employee, Project, TasksEmployees
from models import EmployeeSchema, TaskSchema, NoteSchema, EmployeeRelSchema
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


async def delete_employee(employee_id: int) -> bool:
    async with async_session_factory() as session:
        employee = await session.get(Employee, employee_id)

        if employee is not None:
            await session.delete(employee)
            await session.commit()
            return True
        return False


async def create_employee(
    first_name: str, last_name: str, salary: int, is_working: bool = False
) -> Employee:
    async with async_session_factory() as session:
        new_employee = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            is_working=is_working,
        )
        session.add(new_employee)
        await session.flush()
        print(f"Added employee: {new_employee}")
        await session.commit()

        return new_employee


async def update_employee(
    update_id: int,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    salary: Optional[int] = None,
    is_working: Optional[bool] = None,
) -> Employee:
    async with async_session_factory() as session:
        prev_person = await session.get(Employee, update_id)
        if prev_person is None:
            raise ValueError(f"Employee with id:{update_id} not found")

        new_person = {
            "first_name": first_name,
            "last_name": last_name,
            "salary": salary,
            "is_working": is_working,
        }

        for key, val in new_person.items():
            if val is not None and val != getattr(prev_person, key):
                setattr(prev_person, key, val)
        await session.commit()

        await session.refresh(prev_person)
        print(prev_person)
        return prev_person


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
