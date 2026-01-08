from fastapi import FastAPI
from app.modules.tasks.controller import router as task_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import create_tables
from app.core.config import get_settings
from app.core.database import engine, Base
from app.modules.tasks import models 

settings = get_settings()

# Create the database tables
create_tables()


app = FastAPI(
    swagger_ui_parameters={
        "theme": "dark"
    }
)

app.include_router(task_router)

@app.get("/")
async def root():
  return {"message": "Hello World"}