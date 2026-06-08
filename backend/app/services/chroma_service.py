import chromadb

from app.services.embedding_service import (
    get_embedding
)

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="medical_documents"
)


def add_document(
    document_id: str,
    text: str,
    metadata: dict
):

    embedding = get_embedding(text)

    collection.add(
        ids=[document_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata]
    )


def search_documents(
    query: str,
    filename=None,
    top_k: int = 10
):

    query_embedding = get_embedding(
        query
    )

    if filename:

        results = collection.query(
            query_embeddings=[
                query_embedding
            ],
            n_results=top_k,
            where={
                "filename": filename
            }
        )

    else:

        results = collection.query(
            query_embeddings=[
                query_embedding
            ],
            n_results=top_k
        )

    return results