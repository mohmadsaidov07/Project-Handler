from fastapi import APIRouter, HTTPException
from typing import List
from classes import Project, CreateProject, UpdateProject
from db_connect import get_data, connect_sql


router = APIRouter(prefix="/projects", tags=["projects"])

all_projects: List[Project] = get_data("SELECT * FROM projects;")


@router.get("/", response_model=List[Project])
def get_projects() -> List[Project]:
    return all_projects


@router.get("/{id}", response_model=Project)
def get_project(project_id: int) -> Project:
    for project in all_projects:
        if project.project_id == project_id:
            return project
    raise HTTPException(
        status_code=404, detail=f"There is no project with id:{project_id}"
    )


@router.post("/", response_model=CreateProject)
def create_project(project: CreateProject, project_id: int = None) -> CreateProject:
    conn = connect_sql()
    cursor = conn.cursor()

    cursor.execute(
        f"""INSERT INTO projects({"project_id, " if project_id != None else ""}project_name,start_date, end_date,is_completed)
                    VALUES({"project_id, " if project_id != None else ""}
                    {
                    ", ".join(
                                repr(getattr(project, key)) #IF TRUE
                            if key not in ["start_date", "end_date"] 
                            else 
                                repr((getattr(project, key)).strftime('%Y-%m-%d'))#ELSE 
                        for key in project.__dict__.keys()#For loop
                            ) 
                        });"""
    )
    cursor.execute(
        "SELECT setval('projects_project_id_seq', (SELECT MAX(project_id) FROM projects))"
    )
    conn.commit()
    cursor.close()
    conn.close()
    return project


@router.delete("/", response_model=Project)
def delete_developer(project_id: int) -> Project:
    for project_obj in all_projects:
        if project_obj.project_id == project_id:
            conn = connect_sql()
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM projects WHERE project_id = {project_id}")

            conn.commit()
            cursor.close()
            conn.close()
            return project_obj
    raise HTTPException(
        status_code=404,
        detail=f"There is no project with project_id:{project_id}",
    )


def apply_project_update(project_id: int, update_data: dict) -> Project:
    for project in all_projects:
        if project.project_id == project_id:
            conn = connect_sql()
            cursor = conn.cursor()
            for key, value in update_data.items():
                if getattr(project, key) != value:
                    if key not in ["start_date", "end_date"]:
                        cursor.execute(
                            f"UPDATE projects SET {key} = {repr(value)} WHERE project_id = {project_id}"
                        )
                    else:
                        cursor.execute(
                            f"UPDATE projects SET {key} = {repr((value.strftime('%Y-%m-%d')))} WHERE project_id = {project_id}"
                        )

                    conn.commit()
            cursor.close()
            conn.close()
            return project
    raise HTTPException(status_code=404, detail=f"project id {project_id} not found")


@router.put("/{project_id}", response_model=Project)
def replace_project(project_id: int, updated_project: CreateProject) -> Project:
    update_data = updated_project.model_dump()
    return apply_project_update(project_id, update_data)


@router.patch("/{project_id}", response_model=Project)
def update_project_partial(project_id: int, partial_project: UpdateProject) -> Project:
    update_data = partial_project.model_dump(exclude_unset=True)
    return apply_project_update(project_id, update_data)
