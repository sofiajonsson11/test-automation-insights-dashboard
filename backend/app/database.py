# backend/app/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/test_insights"
)
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def init_db():
    # Import models **inside** the function to avoid circular imports
    from app.models.test_result import TestResult

    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")
