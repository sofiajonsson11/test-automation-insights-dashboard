# simple DB wait script that tries to connect with psycopg2 via sqlalchemy engine
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    print("DATABASE_URL not set in environment")
    raise SystemExit(1)

print("Waiting for database to be ready...")
engine = create_engine(DATABASE_URL)
max_tries = 30
for i in range(max_tries):
    try:
        conn = engine.connect()
        conn.close()
        print("Database is ready!")
        break
    except OperationalError:
        print(f"Database not ready yet (try {i+1}/{max_tries}) — sleeping 2s...")
        time.sleep(2)
else:
    print("Database did not become available in time.")
    raise SystemExit(1)
