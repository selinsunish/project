from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
import os
from datetime import datetime,timezone

router = APIRouter()
MAX_FILE_SIZE_MB = 5

@router.post("/upload-syllabus")
async def upload_syllabus(files: List[UploadFile] = File(...)):
    os.makedirs("uploads/syllabus", exist_ok=True)
    uploaded_files = []

    for file in files:
        # 1. Type check
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail=f"{file.filename} is not a PDF")

        # 2. Size check
        content = await file.read()
        if len(content) > MAX_FILE_SIZE_MB * 1024 * 1024:
            raise HTTPException(status_code=400, detail=f"{file.filename} exceeds 5MB size limit")

        # 3. Save file with timestamped name
        timestamp =  datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        new_filename = f"syllabus_uploaded_on_{timestamp}.pdf"
        save_path = os.path.join("uploads/syllabus", new_filename)

        with open(save_path, "wb") as f:
            f.write(content)

        uploaded_files.append(new_filename)

    return {"message": "Syllabus uploaded successfully", "files": uploaded_files}
