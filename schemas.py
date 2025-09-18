from pydantic import BaseModel, Field, BeforeValidator
from datetime import datetime
from typing import Optional, List, Annotated
import enum

import re

DateString = Annotated[str, BeforeValidator(lambda x: validate_date_format(x))]


def validate_date_format(date_str: str) -> str:
    if not isinstance(date_str, str):
        raise ValueError("Date must be string")
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern=pattern, string=date_str):
        raise ValueError("String must be formatted like YYYY-MM-DD")

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date")

    return date_str


class Priority(enum.IntEnum):
    high_priority = 3
    mid_priority = 2
    low_priority = 1


class TaskBase(BaseModel):
    task_description: str = Field(..., description="Information about task")
    start_date: DateString = Field(
        default="2000-01-01", description="Date when task started"
    )
    end_date: DateString = Field(
        default="2000-01-01", description="Date when task ended or will end"
    )
    priority: Priority = Field(
        default=Priority.low_priority, description="Task priority"
    )
    project_id: int = Field(..., description="Project id that this task belongs to")

    class Config:
        from_attributes = True


class TaskSchema(TaskBase):
    id: int = Field(..., description="Task unique identifier")


class EmployeeBase(BaseModel):
    first_name: str = Field(..., description="Employee's first name")
    last_name: str = Field(..., description="Employee's last name")

    salary: int = Field(..., description="Employee's salary")
    is_working: bool = Field(
        default=True, description="Status of Employee if he's working"
    )

    class Config:
        from_attributes = True


class EmployeeSchema(EmployeeBase):
    id: int = Field(..., description="Employee unique identifier")


class ProjectBase(BaseModel):
    project_name: str = Field(..., description="Name of the project")
    start_date: DateString = Field(
        default="2000-01-01", description="date when project started"
    )
    end_date: DateString = Field(
        default="2000-01-01", description="date when project ended"
    )
    is_completed: bool = Field(default=False, description="status of completion")

    class Config:
        from_attributes = True


class ProjectSchema(ProjectBase):
    id: int = Field(..., description="Project unique identifier")


class NoteBase(BaseModel):
    note_info: str = Field(..., description="Note text")
    employee_id: int = Field(
        ..., description="The ID of the employee who wrote this note"
    )
    task_id: int = Field(..., description="The ID of the task this note belongs to.")

    class Config:
        from_attributes = True


class NoteSchema(NoteBase):
    id: int = Field(..., description="Note unique identifier")


class TaskEmployeeSchema(BaseModel):
    task_id: int = Field(..., gt=0, description="ID of the task that employee works on")
    employee_id: int = Field(
        ..., gt=0, description="ID of the employee that works on the task"
    )


# Relations


class ProjectRelSchema(ProjectSchema):
    project_tasks: List["TaskSchema"] = []


class TaskRelSchema(TaskSchema):
    task_employees: List["EmployeeSchema"] = []
    task_project: "ProjectSchema"
    task_notes: List["NoteSchema"] = []


class EmployeeRelSchema(EmployeeSchema):
    employee_tasks: List["TaskSchema"] = []
    employee_notes: List["NoteSchema"] = []


class NoteRelSchema(NoteSchema):
    note_task: "TaskSchema"
    written_by: "EmployeeSchema"


# Updating classes
# FIXME: change attributes so they'll match their class
class UpdateProjectSchema(BaseModel):
    project_name: Optional[str] = None
    start_date: Optional[DateString] = None
    end_date: Optional[DateString] = None
    is_completed: Optional[bool] = None


class UpdateTaskSchema(BaseModel):
    task_description: Optional[str] = None
    start_date: Optional[DateString] = None
    end_date: Optional[DateString] = None
    priority: Optional[Priority] = None
    project_id: Optional[int] = None


class UpdateEmployeeSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    salary: Optional[int] = None
    is_working: Optional[bool] = None


class UpdateNoteSchema(BaseModel):
    note_info: Optional[str] = None
    employee_id: Optional[int] = None
    task_id: Optional[int] = None
