from fastapi import APIRouter, HTTPException
from typing import List, Dict
from classes import Developer, CreateDeveloper, UpdateDeveloper
from db_connect import get_data, connect_sql
from psycopg2.extras import NamedTupleCursor

router = APIRouter(prefix="/developers", tags=["developers"])
all_developers: List[Developer] = get_data("SELECT * FROM developers;")


def new_id(objects_list: List[object], id_columnName: str) -> int:
    return max(getattr(obj, id_columnName) for obj in objects_list)


@router.get("/", response_model=List[Developer])
def get_developers() -> List[Developer]:
    return all_developers


@router.get("/{developer_id}", response_model=Developer)
def get_developer(developer_id: int) -> Developer:
    for developer in all_developers:
        if developer.developer_id == developer_id:
            return developer
    raise HTTPException(
        status_code=404, detail=f"There is no developer with id:{developer_id}"
    )


@router.get("/notes/", response_model=List[Dict])
def developerNotes() -> List[Dict]:
    conn = connect_sql()
    cursor = conn.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(
        "SELECT DISTINCT d.developer_id, first_name, last_name, position FROM developers d\
         JOIN notes n ON n.developer_id = d.developer_id ORDER BY d.developer_id;"
    )
    rows = cursor.fetchall()
    return [dict(**row._asdict()) for row in rows]


@router.post("/", response_model=CreateDeveloper)
def create_developer(
    developer: CreateDeveloper, project_id: int, developer_id: int = None
) -> CreateDeveloper:
    conn = connect_sql()
    cursor = conn.cursor()
    cursor.execute(
        f"""
        INSERT INTO developers({"developer_id, " if developer_id != None else ""}first_name, last_name, position, salary, is_working) 
            VALUES({f"{developer_id}, " if developer_id != None else ""}, {", ".join(repr(getattr(developer, attr)) for attr in developer.__dict__.keys())});
        
        INSERT INTO project_developers(project_id, developer_id) 
            VALUES({project_id}, {new_id(all_developers, "developer_id") if developer_id == None else developer_id});"""
    )
    cursor.execute(
        "SELECT setval('developers_developer_id_seq', (SELECT MAX(developer_id) FROM developers))"
    )
    conn.commit()
    cursor.close()
    conn.close()
    return developer


@router.delete("/", response_model=Developer)
def delete_developer(developer_id: int) -> Developer:
    for developer_obj in all_developers:
        if developer_obj.developer_id == developer_id:
            conn = connect_sql()
            cursor = conn.cursor()
            cursor.execute(
                f"DELETE FROM developers WHERE developer_id = {developer_id}"
            )
            cursor.execute(
                f"DELETE FROM project_developers WHERE developer_id = {developer_id}"
            )
            conn.commit()
            cursor.close()
            conn.close()
            return developer_obj
    raise HTTPException(
        status_code=404,
        detail=f"There is no developer with developer_id:{developer_id}",
    )


def apply_developer_update(developer_id: int, update_data: dict) -> Developer:
    for developer in all_developers:
        conn = connect_sql()
        cursor = conn.cursor()
        if developer.developer_id == developer_id:
            for key, value in update_data.items():
                if getattr(developer, key) != value:
                    cursor.execute(
                        f"UPDATE developers SET {key} = {repr(value)} WHERE developer_id = {developer_id}"
                    )

                    conn.commit()
            cursor.close()
            conn.close()
            return developer
    raise HTTPException(
        status_code=404, detail=f"developer id {developer_id} not found"
    )


@router.put("/{developer_id}", response_model=Developer)
def replace_developer(
    developer_id: int, updated_developer: CreateDeveloper
) -> Developer:
    update_data = updated_developer.model_dump()
    return apply_developer_update(developer_id, update_data)


@router.patch("/{developer_id}", response_model=Developer)
def update_developer_partial(
    developer_id: int, partial_developer: UpdateDeveloper
) -> Developer:
    update_data = partial_developer.model_dump(exclude_unset=True)
    return apply_developer_update(developer_id, update_data)
