from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Literal

# from enum import IntEnum


# class Priority(IntEnum):
#     LOW = 1
#     MEDIUM = 2
#     HIGH = 3


class TaskBase(BaseModel):
    task_description: str = Field(..., description="Information about task")
    start_date: date = Field(..., description="Task start date")
    end_date: date = Field(..., description="Task end date")
    priority: int = Field(default=1, description="Task priority")
    project_id: int = Field(..., description="Project id that this task belongs to")


class Task(TaskBase):
    task_id: int = Field(..., description="Task unique identifier")


class DeveloperBase(BaseModel):
    first_name: str = Field(..., description="Developer's first name")
    last_name: str = Field(..., description="Developer's last name")

    position: Literal["intern", "junior", "middle", "senior", "teamlead"] = Field(
        ..., description="Developer's position"
    )
    salary: int = Field(..., description="developer's salary")
    is_working: Literal[0, 1] = Field(
        default=1, description="Status of developer if he's working"
    )


class Developer(DeveloperBase):
    developer_id: int = Field(..., description="developer unique identifier")


class ProjectBase(BaseModel):
    project_name: str = Field(..., description="Name of the project")
    start_date: date = Field(..., description="date when project started")
    end_date: date = Field(..., description="date when project ended")
    is_completed: Literal[0, 1] = Field(..., description="status of completion")


class Project(ProjectBase):
    project_id: int = Field(..., description="Project unique identifier")


class NoteBase(BaseModel):
    note_info: str = Field(..., description="Note text")
    developer_id: int = Field(
        ..., description="The ID of the developer who wrote this note"
    )
    task_id: int = Field(..., description="The ID of the task this note belongs to.")


class Note(NoteBase):
    note_id: int = Field(..., description="Note unique identifier")


# Creating classes
class CreateProject(ProjectBase):
    pass


class CreateTask(TaskBase):
    pass


class CreateDeveloper(DeveloperBase):
    pass


class CreateNote(NoteBase):
    pass


# Updating classes
# FIXME: change attributes so they'll match their class
class UpdateProject(BaseModel):
    project_name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    is_completed: Optional[Literal[0, 1]] = None


class UpdateTask(BaseModel):
    task_description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    priority: Optional[int] = None
    project_id: Optional[int] = None


class UpdateDeveloper(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    position: Optional[Literal["intern", "junior", "middle", "senior", "teamlead"]] = (
        None
    )
    salary: Optional[int] = None
    is_working: Optional[Literal[0, 1]] = None


class UpdateNote(BaseModel):
    note_info: Optional[str] = None
    developer_id: Optional[int] = None
    task_id: Optional[int] = None
