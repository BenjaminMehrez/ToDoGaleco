from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime




class TaskBase(BaseModel):
  title: str = Field(..., max_length=30)
  description: str = Field(..., min_length=5, max_length=50)


