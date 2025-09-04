from . import *


async def get_projects(skip: int = 0, limit: int = 5) -> List[ProjectSchema]:
    async with async_session_factory() as session:
        e = aliased(Project)
        res = await session.scalars(
            select(e).where(e.id >= skip).limit(limit).order_by(e.id)
        )
        projects = res.all()
        projects_json = [ProjectSchema.model_validate(project) for project in projects]
        for project_json in projects_json:
            print(project_json)
        return projects_json


async def get_project(project_id: int) -> ProjectRelSchema:
    async with async_session_factory() as session:
        project = await session.get(
            Project, project_id, options=[selectinload(Project.project_tasks)]
        )
        if project is None:
            raise HTTPException(
                status_code=418,
                detail=f"Sry you're a teapot, there's no user with id {project_id}",
            )
        res = ProjectRelSchema.model_validate(project)
        print(res)
        return res


async def delete_project(project_id: int) -> ProjectSchema:
    async with async_session_factory() as session:
        project = await session.get(Project, project_id)
        if project is not None:
            deleted_project = ProjectSchema.model_validate(project)
            await session.delete(project)
            await session.commit()
            return deleted_project
        else:
            raise HTTPException(
                status_code=404, detail=f"Project with id:{project_id} not found!"
            )


async def create_project(new_data: ProjectBase) -> ProjectSchema:
    async with async_session_factory() as session:
        mapped_data = Project(
            project_name=new_data.project_name.strip(),
            start_date=new_data.start_date,
            end_date=new_data.end_date,
            is_completed=new_data.is_completed,
        )
        session.add(mapped_data)
        await session.flush()
        await session.refresh(mapped_data)
        print(f"Added Project: {mapped_data}")

        project_json = ProjectSchema.model_validate(mapped_data)

        await session.commit()

        return project_json


async def update_project(
    update_id: int, update_data: UpdateProjectSchema, partial: bool = False
) -> ProjectSchema:
    async with async_session_factory() as session:
        prev_project = await session.get(Project, update_id)
        if prev_project is None:
            raise HTTPException(
                status_code=404, detail=f"Project with id:{update_id} not found"
            )
        if partial:
            update_dict = update_data.model_dump(exclude_unset=True)
        else:
            update_dict = update_data.model_dump()

        for key, val in update_dict.items():
            setattr(prev_project, key, val)

        await session.commit()
        await session.refresh(prev_project)

        project_json = ProjectSchema.model_validate(prev_project)
        print(project_json)
        return project_json


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
#     await get_projects(8)
#     # await update_project(9, UpdateProjectSchema(is_completed=True), partial=True)


# asyncio.run(main())
