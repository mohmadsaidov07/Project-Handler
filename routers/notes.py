import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import APIRouter, HTTPException
from typing import List

from schemas import (
    NoteBase,
    NoteSchema,
    UpdateNoteSchema,
    NoteRelSchema,
)

from routers.db_conn.queries_package.note_queries import (
    get_notes,
    get_note,
    create_note,
    delete_note,
    update_note,
)

router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/", response_model=List[NoteSchema])
async def get_notes_handle(skip: int = 0, limit: int = 5) -> List[NoteSchema]:
    return await get_notes(skip, limit)


@router.get("/{note_id}", response_model=NoteRelSchema)
async def get_note_handle(note_id: int) -> NoteRelSchema:
    res = await get_note(note_id)
    if res is not None:
        return res
    else:
        raise HTTPException(
            status_code=404, detail=f"There's no note with id:{note_id}"
        )


@router.post("/", response_model=NoteSchema)
async def create_note_handle(new_note_data: NoteBase) -> NoteSchema:
    note = await create_note(new_note_data)
    return note


@router.delete("/", response_model=NoteSchema)
async def delete_note_handle(note_id: int) -> NoteSchema:
    return await delete_note(note_id=note_id)


@router.put("/{note_id}", response_model=NoteSchema)
async def replace_note_handle(
    note_id: int, update_data: UpdateNoteSchema
) -> NoteSchema:
    return await update_note(note_id, update_data)


@router.patch("/{note_id}", response_model=NoteSchema)
async def update_note_handle(note_id: int, update_data: UpdateNoteSchema) -> NoteSchema:
    return await update_note(note_id, update_data, True)
