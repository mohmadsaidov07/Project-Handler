from sqlalchemy import select, delete, and_, insert
from sqlalchemy.orm import selectinload, joinedload, aliased
from .db_models import Task, Note, Employee, Project, TasksEmployees
from models import EmployeeDTO
from .db_setup import (
    async_session_factory,
    async_engine,
    sync_engine,
    sync_session_factory,
    Base,
)
import asyncio
from .test_data import projects, tasks, employees, notes, tasks_employees
from typing import List, Dict, Sequence, Tuple, no_type_check, Optional


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


async def get_employees(from_id: int = 0, shown_amount: int = 5) -> List[EmployeeDTO]:
    async with async_session_factory() as session:
        res = await session.scalars(
            select(Employee)
            .where(Employee.id >= from_id)
            .limit(shown_amount)
            .order_by(Employee.id)
        )
        employees = res.all()
        employees_json = [
            EmployeeDTO.model_validate(employee) for employee in employees
        ]
        for employee_json in employees_json:
            print(employee_json)
        return employees_json


async def get_employee(employee_id: int) -> EmployeeDTO | None:
    async with async_session_factory() as session:
        result_employee = await session.get(Employee, employee_id)
        employee_json = EmployeeDTO.model_validate(result_employee)
        print(employee_json)
        return employee_json


@no_type_check
async def get_employee_notes(employee_id: int) -> Tuple[Employee, List[Note] | []]:
    async with async_session_factory() as session:
        employee = await session.get(
            Employee, employee_id, options=[selectinload(Employee.employee_notes)]
        )
        if employee is not None:
            print(f"{employee} -> {employee.employee_notes}")
            return (employee, employee.employee_notes)


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
):
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


# async def main():
#     # await create_tables()
#     # await insert_data()
#     # await create_employee("Patrick", "Bateman", 1_000_000, 1)
#     # await update_employee(84, salary=999_999)
#     await get_employees(80)


# asyncio.run(main())
