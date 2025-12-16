from app.database import SessionLocal, init_db
from app.models.test_result import TestResult
from datetime import datetime, timezone

# Initialize tabbles (safe call again)
init_db()

# Create a new session
session = SessionLocal()

# Create a sample TestResult entry
sample_result = TestResult(
    test_name="Sample Test",
    framework="pytest",
    status="pass",
    duration=1.23,
    executed_at=datetime.timezone.utc(),
)

# Add and commit
session.add(sample_result)
session.commit()

# Query back the inserted row
results = session.query(TestResult).all()
for r in results:
    print(r)

# Close the session
session.close()
