import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from app.services.report_memory import (
    set_active_report
)

from app.services.document_processor import (
    process_document
)
from app.services.document_processor import (
    process_document
)

from app.services.session_service import (
    set_current_report
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        buffer.write(
            await file.read()
        )

    process_document(
        file_path
    )

    set_active_report(
        file.filename
    )

    # IMPORTANT
    chunks_created = process_document(
        file_path
    )

    set_current_report(
        file.filename
    )

    return {
        "message":
        "PDF uploaded and indexed successfully",

        "filename":
        file.filename,

        "chunks":
        chunks_created
    }


@router.get("/files")
async def get_uploaded_files():

    files = os.listdir(
        UPLOAD_DIR
    )

    return {
        "files": files
    }