from fastapi import FastAPI
from routers import employee, projects, notes, tasks

app = FastAPI()

app.include_router(employee.router)
# app.include_router(projects.router)
# app.include_router(notes.router)
# app.include_router(tasks.router)


@app.get("/")
def read_root():
    return {"message": "Hello world"}


# TODO:Implement db with Orm such as sqlAlchemy,find a way to use websockets, and make a minimal frontend, then connect em together
# FIXME: don't forget to add async support for database operations in the future
