from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from app.database import Base


class TestResult(Base):
    __tablename__ = "test_results"

    id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String, index=True)
    status = Column(String, index=True)  # pass/fail/skip
    duration = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    source = Column(String)  # pytest/cypress/postman
    is_flaky = Column(Boolean, default=False)
