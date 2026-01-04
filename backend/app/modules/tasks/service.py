from sqlalchemy.orm import Session
from .repository import TaskRepository
from typing import List
from .models import Task
from .schemas import TaskBase

class TaskService:
    def __init__(self,db:Session):
        self.db = db
        self.repository = TaskRepository(db)
        
    def get_all_task(self) -> List[Task]:
        return self.repository.get_all()
    
    def create(self,task_data:TaskBase) -> Task:
        db_task = Task(
            title = task_data.title,
            description = task_data.description
        )
        return self.repository.create(db_task)
    

    
        