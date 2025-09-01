# from fastapi import APIRouter, HTTPException
# from typing import List, Dict
# from models import Employee, CreateEmployee, UpdateEmployee
# from db_connect import get_data, connect_sql
# from psycopg2.extras import NamedTupleCursor

# router = APIRouter(prefix="/employees", tags=["employees"])
# all_employees: List[Employee] = get_data("SELECT * FROM employees;")


# def new_id(objects_list: List[object], id_columnName: str) -> int:
#     return max(getattr(obj, id_columnName) for obj in objects_list)


# @router.get("/", response_model=List[Employee])
# def get_employees() -> List[Employee]:
#     return all_employees


# @router.get("/{employee_id}", response_model=Employee)
# def get_employee(employee_id: int) -> Employee:
#     for employee in all_employees:
#         if Employee.id == employee_id:
#             return employee
#     raise HTTPException(
#         status_code=404, detail=f"There is no employee with id:{employee_id}"
#     )


# @router.get("/notes/", response_model=List[Dict])
# def employeeNotes() -> List[Dict]:
#     conn = connect_sql()
#     cursor = conn.cursor(cursor_factory=NamedTupleCursor)
#     cursor.execute(
#         "SELECT DISTINCT d.employee_id, first_name, last_name, position FROM employees d\
#          JOIN notes n ON n.employee_id = d.employee_id ORDER BY d.employee_id;"
#     )
#     rows = cursor.fetchall()
#     return [dict(**row._asdict()) for row in rows]


# @router.post("/", response_model=CreateEmployee)
# def create_employee(
#     employee: CreateEmployee, project_id: int, employee_id=None
# ) -> CreateEmployee:
#     conn = connect_sql()
#     cursor = conn.cursor()
#     cursor.execute(
#         f"""
#         INSERT INTO employees({"employee_id, " if employee_id is not None else ""}first_name, last_name, position, salary, is_working)
#             VALUES({f"{employee_id}, " if employee_id is not None else ""}, {", ".join(repr(getattr(employee, attr)) for attr in employee.__dict__.keys())});

#         INSERT INTO project_employees(project_id, employee_id)
#             VALUES({project_id}, {new_id(employees, "employee_id") if employee_id is None else employee_id});"""
#     )
#     cursor.execute(
#         "SELECT setval('employees_employee_id_seq', (SELECT MAX(employee_id) FROM employees))"
#     )
#     conn.commit()
#     cursor.close()
#     conn.close()
#     return employee


# @router.delete("/", response_model=Employee)
# def delete_employee(employee_id: int) -> Employee:
#     for employee_obj in all_employees:
#         if employee_obj.employee_id == employee_id:
#             conn = connect_sql()
#             cursor = conn.cursor()
#             cursor.execute(f"DELETE FROM employees WHERE employee_id = {employee_id}")
#             cursor.execute(
#                 f"DELETE FROM project_employees WHERE employee_id = {employee_id}"
#             )
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return employee_obj
#     raise HTTPException(
#         status_code=404,
#         detail=f"There is no employee with employee_id:{employee_id}",
#     )


# def apply_employee_update(employee_id: int, update_data: dict) -> employee:
#     for employee in all_employees:
#         conn = connect_sql()
#         cursor = conn.cursor()
#         if employee.employee_id == employee_id:
#             for key, value in update_data.items():
#                 if getattr(employee, key) != value:
#                     cursor.execute(
#                         f"UPDATE employees SET {key} = {repr(value)} WHERE employee_id = {employee_id}"
#                     )

#                     conn.commit()
#             cursor.close()
#             conn.close()
#             return employee
#     raise HTTPException(status_code=404, detail=f"employee id {employee_id} not found")


# @router.put("/{employee_id}", response_model=employee)
# def replace_employee(employee_id: int, updated_employee: Createemployee) -> employee:
#     update_data = updated_employee.model_dump()
#     return apply_employee_update(employee_id, update_data)


# @router.patch("/{employee_id}", response_model=employee)
# def update_employee_partial(
#     employee_id: int, partial_employee: Updateemployee
# ) -> employee:
#     update_data = partial_employee.model_dump(exclude_unset=True)
#     return apply_employee_update(employee_id, update_data)


"""

Wayyy before

Before

"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import APIRouter, HTTPException
from typing import List, Dict

from models import (
    EmployeeSchema,
    UpdateEmployeeSchema,
    NoteSchema,
    EmployeeRelSchema,
    EmployeeBase,
)

# from db_connect import get_data, connect_sql
# from psycopg2.extras import NamedTupleCursor
from db_conn.async_queries import get_employees, get_employee, create_employee

router = APIRouter(prefix="/employees", tags=["employees"])
# all_employees: List[Employee] = get_data("SELECT * FROM employees;")


# def new_id(objects_list: List[object], id_columnName: str) -> int:
#     return max(getattr(obj, id_columnName) for obj in objects_list)


@router.get("/", response_model=List[EmployeeSchema])
async def get_employees_handle(skip: int = 0, limit: int = 5) -> List[EmployeeSchema]:
    return await get_employees(skip, limit)


@router.get("/{employee_id}", response_model=EmployeeRelSchema)
async def get_employee_handle(employee_id: int) -> EmployeeRelSchema:
    res = await get_employee(employee_id)
    if res is not None:
        return res
    else:
        raise HTTPException(
            status_code=404, detail=f"There's no employee with id:{employee_id}"
        )


@router.post("/", response_model=EmployeeBase)
async def create_employee_handle(
    first_name: str | None = None,
    last_name: str | None = None,
    salary: int = 0,
    is_working: bool = True,
) -> EmployeeBase:
    employee = await create_employee(
        first_name=first_name, last_name=last_name, salary=salary, is_working=is_working
    )
    print(employee)
    return employee


# @router.delete("/", response_model=Employee)
# def delete_employee(employee_id: int) -> Employee:
#     for employee_obj in all_employees:
#         if employee_obj.employee_id == employee_id:
#             conn = connect_sql()
#             cursor = conn.cursor()
#             cursor.execute(f"DELETE FROM employees WHERE employee_id = {employee_id}")
#             cursor.execute(
#                 f"DELETE FROM project_employees WHERE employee_id = {employee_id}"
#             )
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return employee_obj
#     raise HTTPException(
#         status_code=404,
#         detail=f"There is no employee with employee_id:{employee_id}",
#     )


# def apply_employee_update(employee_id: int, update_data: dict) -> employee:
#     for employee in all_employees:
#         conn = connect_sql()
#         cursor = conn.cursor()
#         if employee.employee_id == employee_id:
#             for key, value in update_data.items():
#                 if getattr(employee, key) != value:
#                     cursor.execute(
#                         f"UPDATE employees SET {key} = {repr(value)} WHERE employee_id = {employee_id}"
#                     )

#                     conn.commit()
#             cursor.close()
#             conn.close()
#             return employee
#     raise HTTPException(status_code=404, detail=f"employee id {employee_id} not found")


# @router.put("/{employee_id}", response_model=employee)
# def replace_employee(employee_id: int, updated_employee: Createemployee) -> employee:
#     update_data = updated_employee.model_dump()
#     return apply_employee_update(employee_id, update_data)


# @router.patch("/{employee_id}", response_model=employee)
# def update_employee_partial(
#     employee_id: int, partial_employee: Updateemployee
# ) -> employee:
#     update_data = partial_employee.model_dump(exclude_unset=True)
#     return apply_employee_update(employee_id, update_data)
