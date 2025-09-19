from sqlalchemy import select, func, Integer
from sqlalchemy.orm import selectinload, joinedload, aliased
from sqlalchemy.ext.asyncio import AsyncSession
from ..db_models import Task, Note, Employee, Project, TaskEmployees
from pydantic_schemas import (
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
    TaskEmployeeSchema,
)
from ..db_setup import async_session_factory, async_engine, Base
from typing import List, Any, Dict, Annotated
from fastapi import HTTPException, Depends, Request, UploadFile
import asyncio
from pydantic import Field, BaseModel


async def get_session():
    async with async_session_factory() as session:
        yield session


class PaginationParamsGetMany(BaseModel):
    skip: int = Field(default=0, ge=0, description="Amount of rows you wanna skip")
    limit: int = Field(
        default=3, ge=0, le=100, description="Amount of rows you wanna get"
    )


PaginationDep_get = Annotated[PaginationParamsGetMany, Depends()]

__all__ = [
    # pydantic_schemas
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
    "AsyncSession",
    # Models
    "Task",
    "Note",
    "Employee",
    "Project",
    "TaskEmployees",
    "TaskEmployeeSchema",
    # Database
    "async_session_factory",
    "async_engine",
    "Base",
    # Typing & built-ins
    "List",
    "Any",
    "Dict",
    "HTTPException",
    "UploadFile",
    "Request",
    "Depends",
    "asyncio",
    "Annotated",
    # My func's
    "get_session",
    "PaginationDep_get",
]
