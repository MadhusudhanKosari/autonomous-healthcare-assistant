from app.services.chroma_service import (
    add_document,
    search_documents
)

add_document(
    "doc1",
    "Patient has diabetes and high blood pressure"
)

add_document(
    "doc2",
    "Fever and viral infection detected"
)

results = search_documents(
    "Symptoms of fever"
)

print(results)