import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import APIRouter, HTTPException
from typing import List

from schemas import (
    NoteSchema,
    UpdateNoteSchema,
    NoteRelSchema,
)

from routers.db_conn.employee_queries import (
    get_employees,
    get_employee,
    create_employee,
    delete_employee,
    update_employee,
)

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/", response_model=List[NoteSchema])
async def get_employees_handle(skip: int = 0, limit: int = 5) -> List[NoteSchema]:
    return await get_employees(skip, limit)


@router.get("/{employee_id}", response_model=NoteRelSchema)
async def get_employee_handle(employee_id: int) -> NoteRelSchema:
    res = await get_employee(employee_id)
    if res is not None:
        return res
    else:
        raise HTTPException(
            status_code=404, detail=f"There's no employee with id:{employee_id}"
        )


@router.post("/", response_model=NoteSchema)
async def create_employee_handle(
    first_name: str | None = None,
    last_name: str | None = None,
    salary: int = 0,
    is_working: bool = True,
) -> NoteSchema:
    employee = await create_employee(
        first_name=first_name, last_name=last_name, salary=salary, is_working=is_working
    )
    return employee


@router.delete("/", response_model=NoteSchema)
async def delete_employee_handle(employee_id: int) -> NoteSchema:
    return await delete_employee(employee_id=employee_id)


@router.put("/{employee_id}", response_model=NoteSchema)
async def replace_employee_handler(
    employee_id: int, update_data: UpdateNoteSchema
) -> NoteSchema:
    return await update_employee(employee_id, update_data)


@router.patch("/{employee_id}", response_model=NoteSchema)
async def update_employee_handler(
    employee_id: int, update_data: UpdateNoteSchema
) -> NoteSchema:
    return await update_employee(employee_id, update_data, True)


# router = APIRouter(prefix="/notes", tags=["notes"])
# all_notes: List[Note] = get_data("SELECT * FROM notes;")


# @router.get("/", response_model=List[Note])
# def get_notes() -> List[Note]:
#     return all_notes


# @router.get("/{note_id}", response_model=Note)
# def get_note(note_id: int) -> Note:
#     for note in all_notes:
#         if note.note_id == note_id:
#             return note
#     raise HTTPException(status_code=404, detail=f"There is no note with id:{note_id}")


# @router.post("/", response_model=CreateNote)
# def create_note(note: CreateNote, note_id=None) -> CreateNote:
#     conn = connect_sql()
#     cursor = conn.cursor()
#     cursor.execute(
#         f"""INSERT INTO notes({"note_id, " if note_id is not None else ""}note_info, developer_id, task_id)
#                     VALUES({f"{note_id}, " if note_id is not None else ""},{", ".join(repr(getattr(note, attr)) for attr in note.__dict__.keys())});"""
#     )
#     cursor.execute(
#         "SELECT setval('notes_note_id_seq', (SELECT MAX(note_id) FROM notes))"
#     )
#     conn.commit()
#     cursor.close()
#     conn.close()
#     return note


# @router.delete("/", response_model=Note)
# def delete_developer(note_id: int) -> Note:
#     for note_obj in all_notes:
#         if note_obj.note_id == note_id:
#             conn = connect_sql()
#             cursor = conn.cursor()
#             cursor.execute(f"DELETE FROM notes WHERE note_id = {note_id}")

#             conn.commit()
#             cursor.close()
#             conn.close()
#             return note_obj
#     raise HTTPException(
#         status_code=404,
#         detail=f"There is no note with note_id:{note_id}",
#     )


# def apply_note_update(note_id: int, update_data: dict) -> Note:
#     for note in all_notes:
#         conn = connect_sql()
#         cursor = conn.cursor()
#         if note.note_id == note_id:
#             for key, value in update_data.items():
#                 if getattr(note, key) != value:
#                     cursor.execute(
#                         f"UPDATE notes SET {key} = {repr(value)} WHERE note_id = {note_id}"
#                     )

#                     conn.commit()
#             cursor.close()
#             conn.close()
#             return note
#     raise HTTPException(status_code=404, detail=f"note id {note_id} not found")


# @router.put("/{note_id}", response_model=Note)
# def replace_note(note_id: int, updated_note: CreateNote) -> Note:
#     update_data = updated_note.model_dump()
#     return apply_note_update(note_id, update_data)


# @router.patch("/{note_id}", response_model=Note)
# def update_note_partial(note_id: int, partial_note: UpdateNote) -> Note:
#     update_data = partial_note.model_dump(exclude_unset=True)
#     return apply_note_update(note_id, update_data)
