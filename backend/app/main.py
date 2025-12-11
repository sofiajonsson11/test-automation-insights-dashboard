from fastapi import FastAPI
from app.routers import results
from app.database import Base, engine
from app.models.test_result import TestResult
from app.jobs.scheduler import start_scheduler

app = FastAPI(title="Test Automation Insights Dashboard")

# include routers
app.include_router(results.router)


@app.on_event("startup")
def on_startup():
    # create tables if they don't exist (simple approach for dev)
    Base.metadata.create_all(bind=engine)
    # start background scheduler (optional)
    start_scheduler()


@app.get("/")
def root():
    return {"status": "ok"}
