from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime, timezone
from app.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Task(Base):
  __tablename__ = "tasks"

  title = Column(String, nullable=False)
  description = Column(String, nullable=True)
  completed = Column(Boolean, default=False)
  created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
  id = Column(UUID(as_uuid = True), primary_key= True, default=uuid.uuid4)


  def __repr__(self):
    return f"<Task(title='{self.title}', description='{self.description}', completed='{self.completed}', created_at='{self.created_at}')>"