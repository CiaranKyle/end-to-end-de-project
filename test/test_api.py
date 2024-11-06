from fastapi.testclient import TestClient
from api.api import app
import pytest

class TestAPIHealthcheck:
    def test_handle_healthcheck(self):
        client = TestClient(app)
        response = client.get("/healthcheck")
        assert response.status_code == 200
        body = response.json()
        assert body == {"message": "server is running!"}