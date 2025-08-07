from pydantic import BaseModel, Field
from enum import IntEnum
from datetime import date
from typing import List, Optional, Literal


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class TaskBase(BaseModel):
    task_id: int = Field(..., description="Task unique identifier")


class Task(TaskBase):
    task_description: str = Field(..., description="Information about task")
    start_date: date = Field(..., description="Task start date")
    end_date: date = Field(..., description="Task end date")
    priority: int = Field(default=1, description="Task priority")
    project_id: int = Field(..., description="Project id that this task belongs to")


class DeveloperBase(BaseModel):
    developer_id: int = Field(..., description="developer unique identifier")


class Developer(DeveloperBase):
    first_name: str = Field(..., description="Developer's first name")
    last_name: str = Field(..., description="Developer's last name")

    position: Literal["intern", "junior", "middle", "senior", "teamlead"] = Field(
        ..., description="Developer's position"
    )

    salary: int = Field(..., description="developer's salary")
    is_working: bool = Field(
        default=True, description="Status of developer if he's working"
    )


class ProjectBase(BaseModel):
    project_id: int = Field(..., description="Project unique identifier")


class Project(ProjectBase):
    project_name: str = Field(..., description="Name of the project")
    start_date: date = Field(..., description="date when project started")
    end_date: date = Field(..., description="date when project ended")
    is_completed: Literal[0, 1] = Field(..., description="status of completion")


class NoteBase(BaseModel):
    note_id: int = Field(..., description="Note unique identifier")


class Note(NoteBase):
    note_info: str = Field(..., description="Note text")
    developer_id: int = Field(
        ..., description="The ID of the developer who wrote this note"
    )
    task_id: int = Field(..., description="The ID of the task this note belongs to.")


# Creating classes
class CreateProject(Project):
    pass


class CreateTask(Task):
    pass


class CreateDeveloper(Developer):
    pass


class CreateNote(Note):
    pass


# Updating classes
class UpdateProject(BaseModel):
    Project: Optional[str] = None
    Project_description: Optional[str] = None
    notes: Optional[List[str]] = None
    priority: Optional[Priority] = None
    developers: Optional[List[Developer]] = None


class UpdateTask(BaseModel):
    task: Optional[str] = None
    task_description: Optional[str] = None
    notes: Optional[List[str]] = None
    priority: Optional[Priority] = None
    developers: Optional[List[Developer]] = None


class UpdateDeveloper(BaseModel):
    task: Optional[str] = None
    task_description: Optional[str] = None
    notes: Optional[List[str]] = None
    priority: Optional[Priority] = None
    developers: Optional[List[Developer]] = None


class UpdateNote(BaseModel):
    task: Optional[str] = None
    task_description: Optional[str] = None
    notes: Optional[List[str]] = None
    priority: Optional[Priority] = None
    developers: Optional[List[Developer]] = None
