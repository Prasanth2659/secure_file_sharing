import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_ops_login():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/ops/login", json={"email": "ops@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_file_upload():
    async with AsyncClient(app=app, base_url="http://test") as client:
        token = "Bearer <Your-Valid-Token>"  # Replace with valid token
        files = {"file": ("test.docx", b"fake-content", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")}
        response = await client.post("/ops/upload", files=files, headers={"Authorization": token})
    assert response.status_code == 200
    assert response.json()["message"] == "File uploaded successfully"
