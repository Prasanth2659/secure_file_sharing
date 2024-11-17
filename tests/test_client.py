import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_client_signup():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/client/signup", json={"email": "client@example.com", "password": "password"})
    assert response.status_code == 201
    assert "encrypted_link" in response.json()

@pytest.mark.asyncio
async def test_email_verification():
    encrypted_email = "<Your-Encrypted-Email>"  # Replace with encrypted email token
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get(f"/client/verify-email/{encrypted_email}")
    assert response.status_code == 200
    assert response.json()["message"] == "Email verified successfully"

@pytest.mark.asyncio
async def test_client_login():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/client/login", json={"email": "client@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_download_file():
    async with AsyncClient(app=app, base_url="http://test") as client:
        token = "Bearer <Your-Valid-Token>"  # Replace with valid token
        response = await client.get("/client/download/1", headers={"Authorization": token})
    assert response.status_code == 200
    assert "download-link" in response.json()
