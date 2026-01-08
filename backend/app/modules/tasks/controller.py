from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.core.database import get_db
from .service import TaskService
from typing import List
from .schemas import TaskResponse,TaskBase
from app.core.config import get_settings

settings = get_settings()
router = APIRouter(prefix = "/api/task",tags = ["tasks"])


    


























































@router.get("/", response_model = List[TaskResponse])
def get_tasks(db:Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.get_all_task()


@router.get("/id", response_model = List[TaskResponse])
def get_tasks_by_id(id,db:Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.get_by_id(id)

@router.post("/", response_model = TaskResponse)
def create_task(task:TaskBase, db:Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.create(task)

