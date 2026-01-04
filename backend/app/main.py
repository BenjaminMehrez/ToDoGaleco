from fastapi import FastAPI
from app.modules.tasks.controller import router as task_router


app = FastAPI()
app.include_router(task_router)



@app.get("/")
async def root():
  return {"message": "Hello World"}