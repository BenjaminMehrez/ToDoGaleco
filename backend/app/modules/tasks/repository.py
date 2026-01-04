from sqlalchemy.orm import Session
from typing import List
from .models import Task

class TaskRepository():
    def __init__(self,db:Session):
        self.db = db
        
    def get_all(self) -> List[Task]:
        return self.db.query(Task).all()
    
    def create(self,task:Task) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task