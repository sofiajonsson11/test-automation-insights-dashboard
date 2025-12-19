from fastapi import FastAPI
from app.database import init_db
from app.routers import ingest

# Initialize DB tables
init_db()

app = FastAPI(title="Test Automation Insights", version="1.0.0")

# Include ingestion router
app.include_router(ingest.router, prefix="", tags=["Ingestion"])
