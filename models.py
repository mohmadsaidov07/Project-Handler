from pydantic import BaseModel, Field, validator
import datetime
from typing import Optional, Literal

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
    project_id: int = Field(
        ..., gt=0, description="Reference to a project that this task belogns to"
    )

    @validator("project_id")
    def validate_project_(cls, v):
        if v <= 0:
            raise ValueError("Project id must be greater than 0")
        return v

    class Config:
        from_attributes = True


class TaskDTO(TaskBase):
    id: int = Field(..., description="Task unique identifier")


class TaskDTORel(TaskDTO):
    # task_employees: List["Employee"] = []

    # task_project: "Project"] = relationship(back_populates="project_tasks")

    # task_notes: List["Note"] = []
    pass


class EmployeeBase(BaseModel):
    first_name: str = Field(..., description="Employee's first name")
    last_name: str = Field(..., description="Employee's last name")

    salary: int = Field(..., ge=0, description="Employee's salary")
    is_working: bool = Field(
        default=True, description="Status of Employee if he's working"
    )

    class Config:
        from_attributes = True


class EmployeeDTO(EmployeeBase):
    id: int = Field(..., description="Employee unique identifier")


class ProjectBase(BaseModel):
    project_name: str = Field(..., description="Name of the project")
    start_date: datetime.datetime = Field(..., description="date when project started")
    end_date: datetime.datetime = Field(..., description="date when project ended")
    is_completed: bool = Field(default=False, description="status of completion")

    class Config:
        from_attributes = True


class ProjectDTO(ProjectBase):
    project_id: int = Field(..., description="Project unique identifier")


class NoteBase(BaseModel):
    note_info: str = Field(..., description="Note text")
    employee_id: int = Field(
        ..., gt=0, description="The ID of the employee who wrote this note"
    )
    task_id: int = Field(
        ..., gt=0, description="The ID of the task this note belongs to."
    )

    class Config:
        from_attributes = True


class NoteDTO(NoteBase):
    note_id: int = Field(..., description="Note unique identifier")


# Creating classes
class CreateProjectDTO(ProjectBase):
    pass


class CreateTaskDTO(TaskBase):
    pass


class CreateEmployeeDTO(EmployeeBase):
    pass


class CreateNoteDTO(NoteBase):
    pass


# Updating classes
# FIXME: change attributes so they'll match their class
class UpdateProjectDTO(BaseModel):
    project_name: Optional[str] = None
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    is_completed: Optional[bool] = None


class UpdateTaskDTO(BaseModel):
    task_description: Optional[str] = None
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    priority: Optional[int] = None
    project_id: Optional[int] = None


class UpdateEmployeeDTO(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    salary: Optional[int] = None
    is_working: Optional[bool] = None


class UpdateNoteDTO(BaseModel):
    note_info: Optional[str] = None
    employee_id: Optional[int] = None
    task_id: Optional[int] = None
