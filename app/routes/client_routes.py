from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

@router.get("/client/download/{file_id}")
async def get_download_link(file_id: int, user: dict = Depends(get_current_client_user)):
    file = get_file(file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    
    encrypted_url = cipher.encrypt(f"/files/{file.path}".encode())
    return {"download-link": encrypted_url.decode(), "message": "success"}
