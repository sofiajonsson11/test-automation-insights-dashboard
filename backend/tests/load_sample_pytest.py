import json
from fastapi.testclient import TestClient
from app.main import app  # import your FastAPI app

client = TestClient(app)

# Load the sample pytest JSON
with open("app/ingestion_samples/sample_pytest.json") as f:
    pytest_data = json.load(f)

# POST to your ingestion endpoint
response = client.post("/ingest/pytest", json=pytest_data)

print("Status code:", response.status_code)
print("Response:", response.json())
