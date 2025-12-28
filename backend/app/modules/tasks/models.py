from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime, timezone
from app.core.database import Base


class Task(Base):
  __tablename__ = "tasks"

  title = Column(String, nullable=False)
  description = Column(String, nullable=True)
  completed = Column(Boolean, default=False)
  created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


  def __repr__(self):
    return f"<Task(title='{self.title}', description='{self.description}', completed='{self.completed}', created_at='{self.created_at}')>"