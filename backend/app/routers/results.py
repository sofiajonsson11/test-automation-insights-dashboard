from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.test_result import TestResult
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/results", tags=["results"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ResultCreate(BaseModel):
    test_name: str
    status: str
    duration: int = 0
    source: str = "pytest"


@router.post("/", status_code=201)
def create_result(payload: ResultCreate, db: Session = Depends(get_db)):
    item = TestResult(
        test_name=payload.test_name,
        status=payload.status,
        duration=payload.duration,
        source=payload.source,
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/", response_model=List[dict])
def list_results(db: Session = Depends(get_db)):
    rows = db.query(TestResult).order_by(TestResult.timestamp.desc()).all()
    # convert SQLAlchemy objects to dicts for simple JSON serialization
    return [
        {
            "id": r.id,
            "test_name": r.test_name,
            "status": r.status,
            "duration": r.duration,
            "timestamp": r.timestamp.isoformat(),
            "source": r.source,
            "is_flaky": r.is_flaky,
        }
        for r in rows
    ]
