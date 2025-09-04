from . import *


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
        res = EmployeeRelSchema.modxel_validate(employee)
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


async def create_employee(new_data: EmployeeBase) -> EmployeeSchema:
    async with async_session_factory() as session:
        mapped_data = Employee(
            first_name=new_data.first_name.title().strip(),
            last_name=new_data.last_name.title().strip(),
            salary=new_data.salary,
            is_working=new_data.is_working,
        )
        session.add(mapped_data)
        await session.flush()
        await session.refresh(mapped_data)
        print(f"Added employee: {mapped_data}")

        employee_json = EmployeeSchema.model_validate(mapped_data)

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
        if partial:
            update_dict = update_data.model_dump(exclude_unset=True)
        else:
            update_dict = update_data.model_dump()

        for key, val in update_dict.items():
            setattr(prev_employee, key, val)

        await session.commit()
        await session.refresh(prev_employee)

        employee_json = EmployeeSchema.model_validate(prev_employee)
        print(employee_json)
        return employee_json


# async def main():
#     # await create_tables()
#     # await insert_data()
#     # await create_employee("Patrick", "Bateman", 1_000_000, 1)
#     # await update_employee(84, salary=999_999)
#     await project_avg_salary()


# asyncio.run(main())
