import uuid

import os

from app.services.pdf_service import (

    extract_text_from_pdf
)

from app.services.ocr_service import (

    extract_text_with_ocr
)

from app.services.chunking_service import (

    chunk_text
)

from app.services.chroma_service import (

    add_document
)


def process_document(

    file_path: str
):

    filename = os.path.basename(

        file_path
    )

    extracted_text = extract_text_from_pdf(

        file_path
    )

    # OCR FALLBACK
    if len(extracted_text.strip()) < 100:

        print("\nUsing OCR Extraction...\n")

        extracted_text = extract_text_with_ocr(

            file_path
        )

    print("\nEXTRACTED TEXT:\n")

    print(extracted_text[:1000])

    chunks = chunk_text(

        extracted_text
    )

    print(f"\nTOTAL CHUNKS: {len(chunks)}")

    for index, chunk in enumerate(chunks):

        document_id = str(uuid.uuid4())

        metadata = {

            "filename": filename,

            "chunk_index": index
        }

        add_document(

            document_id=document_id,

            text=chunk,

            metadata=metadata
        )

    return len(chunks)