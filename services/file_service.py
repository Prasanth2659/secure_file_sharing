from fastapi import HTTPException, UploadFile

ALLOWED_FILE_TYPES = {"application/vnd.openxmlformats-officedocument.presentationml.presentation",
                      "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"}

def validate_file(file: UploadFile):
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type")
