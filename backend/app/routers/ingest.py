from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.test_result import TestResult
from datetime import datetime, timezone

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/ingest/pytest")
def ingest_pytest(json_report: dict, db: Session = Depends(get_db)):
    """
    Ingests a pytest JSON report into the database.
    """
    try:
        tests = json_report.get("tests", [])
        for t in tests:
            test_result = TestResult(
                test_name=t.get("nodeid"),
                framework="pytest",
                status=t.get("outcome"),
                duration=t.get("duration", 0.0),
                executed_at=datetime.now(timezone.utc),
            )
            db.add(test_result)
        db.commit()
        return {"message": f"Inserted {len(tests)} test results successfully!"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
