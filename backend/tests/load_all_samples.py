from app.database import SessionLocal
from app.models.test_result import TestResult

db = SessionLocal()
results = db.query(TestResult).all()
for r in results:
    print(r)
