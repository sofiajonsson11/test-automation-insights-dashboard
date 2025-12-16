# backend/app/models/test_result.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base


class TestResult(Base):
    __tablename__ = "test_results"

    id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String, nullable=False)
    framework = Column(String, nullable=False)  # e.g., pytest, cypress
    status = Column(String, nullable=False)  # pass/fail
    duration = Column(Float, nullable=False)  # in seconds
    executed_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<TestResult(id={self.id}, test_name={self.test_name}, status={self.status}, duration={self.duration}, executed_at={self.executed_at})>"
