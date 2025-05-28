from fastapi.testclient import TestClient
from serving.main import app

client = TestClient(app)

def test_status():
    res = client.get("/status")
    assert res.status_code == 200
