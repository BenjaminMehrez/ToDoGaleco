from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID




class TaskBase(BaseModel):
  title: str = Field(..., max_length=30)
  description: str = Field(..., min_length=5, max_length=50)
  

class TaskResponse(TaskBase):
  id: UUID
  completed: bool


