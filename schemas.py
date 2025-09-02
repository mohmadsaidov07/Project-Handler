from pydantic import BaseModel, Field
import datetime
from typing import Optional, List

from enum import IntEnum


class Priority(IntEnum):
    high_priority = 3
    mid_priority = 2
    low_priority = 1


class TaskBase(BaseModel):
    task_description: str = Field(..., description="Information about task")
    start_date: datetime.datetime = Field(..., description="Task start date")
    end_date: datetime.datetime = Field(..., description="Task end date")
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
    start_date: datetime.datetime = Field(..., description="date when project started")
    end_date: datetime.datetime = Field(..., description="date when project ended")
    is_completed: bool = Field(default=False, description="status of completion")

    class Config:
        from_attributes = True


class ProjectSchema(ProjectBase):
    project_id: int = Field(..., description="Project unique identifier")


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
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    is_completed: Optional[bool] = None


class UpdateTaskSchema(BaseModel):
    task_description: Optional[str] = None
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    priority: Optional[int] = None
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
