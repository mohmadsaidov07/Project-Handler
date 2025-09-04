from sqlalchemy import select, func, Integer
from sqlalchemy.orm import selectinload, joinedload, aliased
from ..db_models import Task, Note, Employee, Project
from schemas import (
    TaskBase,
    TaskSchema,
    EmployeeBase,
    EmployeeSchema,
    ProjectBase,
    ProjectSchema,
    NoteBase,
    NoteSchema,
    TaskRelSchema,
    ProjectRelSchema,
    EmployeeRelSchema,
    NoteRelSchema,
    UpdateProjectSchema,
    UpdateTaskSchema,
    UpdateEmployeeSchema,
    UpdateNoteSchema,
)
from ..db_setup import async_session_factory, async_engine, Base
from ..test_data import projects, tasks, employees, notes, tasks_employees
from typing import List, Any, Dict
from fastapi import HTTPException
import asyncio


async def create_tables() -> None:
    async_engine.echo = False
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async_engine.echo = True


async def insert_data() -> None:
    async_engine.echo = False
    async with async_session_factory() as session:
        session.add_all([*projects, *tasks, *employees])
        await session.flush()
        session.add_all([*notes, *tasks_employees])
        await session.commit()
    async_engine.echo = True


__all__ = [
    # schemas
    "TaskBase",
    "TaskSchema",
    "EmployeeBase",
    "EmployeeSchema",
    "ProjectBase",
    "ProjectSchema",
    "NoteBase",
    "NoteSchema",
    "TaskRelSchema",
    "ProjectRelSchema",
    "EmployeeRelSchema",
    "NoteRelSchema",
    "UpdateProjectSchema",
    "UpdateTaskSchema",
    "UpdateEmployeeSchema",
    "UpdateNoteSchema",
    # SQLAlchemy
    "select",
    "func",
    "Integer",
    "selectinload",
    "joinedload",
    "aliased",
    # Models
    "Task",
    "Note",
    "Employee",
    "Project",
    # Database
    "async_session_factory",
    "async_engine",
    "Base",
    # Test data
    "projects",
    "tasks",
    "employees",
    "notes",
    "tasks_employees",
    # Typing & built-ins
    "List",
    "Any",
    "Dict",
    "HTTPException",
    "asyncio",
    # My func's
    "create_tables",
    "insert_data",
]
