from sqlalchemy.orm import Session
from typing import List
from .models import Task

class TaskRepository():
    def __init__(self,db:Session):
        self.db = db
        
    def get_all(self) -> List[Task]:
        return self.db.query(Task).all()
    
    def get_true(self) -> List[Task]:
        return self.db.query(Task).filter(Task.completed == True)
    
    def get_false(self) -> List[Task]:
        return self.db.query(Task).filter(Task.completed == False)
    
    def get_by_id(self,id) -> List[Task]:
        return self.db.query(Task).filter(Task.id == id)
    
    def update_task(self,id,clave,valor) -> List[Task]:
        clave = clave
        self.db.query(Task).filter(Task.id == id).update({clave:valor})
        self.db.commit()
        return self.db.query(Task).filter(Task.id == id)
        
    def delete_task(self,id):
        self.db.query(Task).filter(Task.id == id).delete()
        self.db.commit()
        return {"message":"task deleted succesfully"}
        
    
    def create(self,task:Task) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task