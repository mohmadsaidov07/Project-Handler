import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import APIRouter, HTTPException
from typing import List

from schemas import (
    EmployeeSchema,
    UpdateEmployeeSchema,
    EmployeeRelSchema,
    EmployeeBase,
)

from routers.db_conn.queries_package.employee_queries import (
    get_employees,
    get_employee,
    create_employee,
    delete_employee,
    update_employee,
)

router = APIRouter(prefix="/employees", tags=["employees"])


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


@router.post("/", response_model=EmployeeSchema)
async def create_employee_handle(data: EmployeeBase) -> EmployeeSchema:
    employee = await create_employee(data)
    return employee


@router.delete("/", response_model=EmployeeSchema)
async def delete_employee_handle(employee_id: int) -> EmployeeSchema:
    return await delete_employee(employee_id=employee_id)


@router.put("/{employee_id}", response_model=EmployeeSchema)
async def replace_employee_handle(
    employee_id: int, update_data: UpdateEmployeeSchema
) -> EmployeeSchema:
    return await update_employee(employee_id, update_data)


@router.patch("/{employee_id}", response_model=EmployeeSchema)
async def update_employee_handle(
    employee_id: int, update_data: UpdateEmployeeSchema
) -> EmployeeSchema:
    return await update_employee(employee_id, update_data, True)
