import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

from schemas import (
    ProjectBase,
    ProjectSchema,
    UpdateProjectSchema,
    ProjectRelSchema,
)

from routers.db_conn.queries_package.project_queries import (
    get_projects,
    get_project,
    create_project,
    delete_project,
    update_project,
    project_avg_salary,
)

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_model=List[ProjectSchema])
async def get_projects_handle(skip: int = 0, limit: int = 5) -> List[ProjectSchema]:
    return await get_projects(skip, limit)


@router.get("/avg_salary", response_model=List[Dict[str, Any]])
async def get_projects_avg_salary() -> List[Dict[str, Any]]:
    return await project_avg_salary()


@router.get("/{project_id}", response_model=ProjectRelSchema)
async def get_project_handle(project_id: int) -> ProjectRelSchema:
    res = await get_project(project_id)
    if res is not None:
        return res
    else:
        raise HTTPException(
            status_code=404, detail=f"There's no project with id:{project_id}"
        )


@router.post("/", response_model=ProjectSchema)
async def create_project_handle(new_project_data: ProjectBase) -> ProjectSchema:
    project = await create_project(new_project_data)
    return project


@router.delete("/", response_model=ProjectSchema)
async def delete_project_handle(project_id: int) -> ProjectSchema:
    return await delete_project(project_id=project_id)


@router.put("/{project_id}", response_model=ProjectSchema)
async def replace_project_handle(
    project_id: int, update_data: UpdateProjectSchema
) -> ProjectSchema:
    return await update_project(project_id, update_data)


@router.patch("/{project_id}", response_model=ProjectSchema)
async def update_project_handle(
    project_id: int, update_data: UpdateProjectSchema
) -> ProjectSchema:
    return await update_project(project_id, update_data, True)
