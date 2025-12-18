from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.database import SessionLocal, init_db
from app.models.test_result import TestResult
from datetime import datetime, timezone


def main():
    print("🌟 Initializing DB (creates tables if needed)...")
    init_db()

    db = SessionLocal()
    try:
        print("🔗 Testing DB connection...")
        result = db.execute(text("SELECT 1"))
        print("DB connection test result:", result.fetchone())

        print("📝 Inserting a sample test result...")
        sample = TestResult(
            test_name="Check DB Test",
            framework="pytest",
            status="pass",
            duration=0.01,
            executed_at=datetime.now(timezone.utc),
        )
        db.add(sample)
        db.commit()

        print("📦 Querying test_results table...")
        rows = db.query(TestResult).all()
        for r in rows:
            print(r)

        print("✅ DB verification complete!")

    except SQLAlchemyError as e:
        print("❌ DB verification failed:", e)
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()
