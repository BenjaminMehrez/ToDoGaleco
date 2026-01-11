from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.core.database import get_db
from .service import TaskService
from typing import List,Any
from .schemas import TaskResponse,TaskBase
from app.core.config import get_settings
from uuid import UUID


settings = get_settings()
router = APIRouter(prefix = "/api/task",tags = ["tasks"])

@router.get("/", response_model = List[TaskResponse])
def get_tasks(db:Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.get_all_task()


@router.get("/id", response_model = List[TaskResponse])
def get_tasks_by_id(id:UUID,db:Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.get_by_id(id)

@router.post("/", response_model = TaskResponse)
def create_task(task:TaskBase, db:Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.create(task)

@router.put("/update", response_model = List[TaskResponse])
def update_task(id: UUID,clave:str, valor:Any, db:Session = Depends(get_db)):
    task_service = TaskService(db)
    if valor == "True":
        valor = True
    elif valor == "False":
        valor = False
    task_service.update(id,clave,valor)
    return task_service.get_by_id(id)
    
@router.delete("/delete")
def delete_task(id: UUID,db:Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.delete(id)
    
    
@router.get("/completed", response_model = List[TaskResponse])
def get_completed(db:Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.get_true()

@router.get("/uncompleted", response_model = List[TaskResponse])
def get_uncompleted(db:Session = Depends(get_db)):
    task_service = TaskService(db)
    return task_service.get_false()


