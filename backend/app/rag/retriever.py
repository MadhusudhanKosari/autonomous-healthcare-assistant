from app.services.chroma_service import (

    search_documents
)


def retrieve_context(

    query: str
):

    results = search_documents(

        query
    )

    documents = results["documents"][0]

    metadatas = results["metadatas"][0]

    combined_context = ""

    sources = []

    for doc, meta in zip(

        documents,

        metadatas
    ):

        combined_context += doc + "\n\n"

        sources.append({

            "filename": meta["filename"],

            "chunk_index": meta["chunk_index"]
        })

    return {

        "context": combined_context,

        "sources": sources
    }