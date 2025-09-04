from . import *


async def get_notes(skip: int = 0, limit: int = 5) -> List[NoteSchema]:
    async with async_session_factory() as session:
        e = aliased(Note)
        res = await session.scalars(
            select(e).where(e.id >= skip).limit(limit).order_by(e.id)
        )
        Notes = res.all()
        Notes_json = [NoteSchema.model_validate(Note) for Note in Notes]
        for Note_json in Notes_json:
            print(Note_json)
        return Notes_json


async def get_note(note_id: int) -> NoteRelSchema:
    async with async_session_factory() as session:
        note = await session.get(
            Note,
            note_id,
            options=(
                joinedload(Note.note_task),
                joinedload(Note.written_by),
            ),
        )
        if note is None:
            raise HTTPException(
                status_code=418,
                detail=f"Sry you're a teapot, there's no user with id {note_id}",
            )
        res = NoteRelSchema.model_validate(note)
        print(res)
        return res


async def delete_note(note_id: int) -> NoteSchema:
    async with async_session_factory() as session:
        note = await session.get(Note, note_id)
        if note is not None:
            deleted_note = NoteSchema.model_validate(note)
            await session.delete(note)
            await session.commit()
            return deleted_note
        else:
            raise HTTPException(
                status_code=404, detail=f"Note with id:{note_id} not found!"
            )


async def create_note(new_data: NoteBase) -> NoteSchema:
    async with async_session_factory() as session:
        mapped_data = Note(
            note_info=new_data.note_info.strip(),
            employee_id=new_data.employee_id,
            task_id=new_data.task_id,
        )
        session.add(mapped_data)
        await session.flush()
        await session.refresh(mapped_data)
        print(f"Added Note: {mapped_data}")

        note_json = NoteSchema.model_validate(mapped_data)

        await session.commit()

        return note_json


async def update_note(
    update_id: int, update_data: UpdateNoteSchema, partial: bool = False
) -> NoteSchema:
    async with async_session_factory() as session:
        prev_note = await session.get(Note, update_id)
        if prev_note is None:
            raise HTTPException(
                status_code=404, detail=f"Note with id:{update_id} not found"
            )
        if partial:
            update_dict = update_data.model_dump(exclude_unset=True)
        else:
            update_dict = update_data.model_dump()

        for key, val in update_dict.items():
            setattr(prev_note, key, val)

        await session.commit()
        await session.refresh(prev_note)

        note_json = NoteSchema.model_validate(prev_note)
        print(note_json)
        return note_json


# async def main():
#     # await create_tables()
#     # await insert_data()
#     await get_note(200)


# asyncio.run(main())
