from fastapi import APIRouter, UploadFile, File
import os

from app.services.document_processor import process_document

router = APIRouter()

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":

        return {
            "error": "Only PDF files allowed"
        }

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:

        content = await file.read()

        buffer.write(content)

    total_chunks = process_document(file_path)

    return {
        "filename": file.filename,
        "chunks_stored": total_chunks,
        "message": "Document processed successfully"
    }