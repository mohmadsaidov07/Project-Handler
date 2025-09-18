from fastapi import FastAPI, Depends
from routers import employee, notes, projects, tasks
import uvicorn
from routers.db_conn.queries_package.employee_queries import reset_data

# FIXME: if name is uvicorn or teapot error 418, check how Request works what is it
# FIXME: Add endpoint so user can upload his own data, only if it's json file, otherwise
# give him a custom router.exception_handler to let him know


app = FastAPI()

app.include_router(employee.router)
app.include_router(projects.router)
app.include_router(notes.router)
app.include_router(tasks.router)


@app.get("/", response_model=dict[str, str])
async def read_root() -> dict[str, str]:
    return {"message": "Hello world"}


@app.put("/", response_model=str)
async def reset_data_to_default(data_resetter: str = Depends(reset_data)) -> str:
    return data_resetter


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
