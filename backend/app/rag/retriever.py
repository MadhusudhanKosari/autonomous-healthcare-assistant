from app.services.chroma_service import (
    search_documents
)

from app.services.session_service import (
    get_current_report
)
from app.services.report_memory import (
    get_active_report
)

# COMMON WORDS TO IGNORE
STOPWORDS = {

    "what",
    "is",
    "the",
    "does",
    "tell",
    "about",
    "my",
    "me",
    "a",
    "an",
    "of",
    "in",
    "on",
    "for",
    "to",
    "and",
    "or"
}


def clean_words(text: str):

    words = text.lower().split()

    filtered = [

        word.strip(".,?!")

        for word in words

        if word.lower() not in STOPWORDS
    ]

    return set(filtered)


def retrieve_context(query: str):

    active_report = get_current_report()

    active_report = get_active_report()

    results = search_documents(
        query=query,
        filename=active_report,
        top_k=10
    )
    print(
    "\nACTIVE REPORT:",
    active_report
)

    documents = results["documents"][0]
    print("\n===== RETRIEVED CHUNKS =====")

    for i, doc in enumerate(documents):
        print(f"\nCHUNK {i}\n")
        print(doc[:500])

    print("\n============================")

    metadatas = results["metadatas"][0]

    distances = results["distances"][0]

    combined_context = ""

    sources = []

    for doc, meta in zip(
        documents,
        metadatas
    ):

        combined_context += doc + "\n\n"

        if meta:

            sources.append({

                "filename": meta.get(
                    "filename",
                    "Unknown"
                )
            })

    average_distance = (

        sum(distances)
        / len(distances)

        if distances else 999
    )

    query_words = clean_words(query)

    context_words = clean_words(
        combined_context
    )

    keyword_overlap = (

        query_words.intersection(
            context_words
        )
    )

    keyword_match_score = len(
        keyword_overlap
    )

    print("\n===== RETRIEVAL DEBUG =====")

    print(
        "ACTIVE REPORT:",
        active_report
    )

    print(
        "KEYWORD MATCH SCORE:",
        keyword_match_score
    )

    print(
        "DISTANCE:",
        average_distance
    )

    print("===========================\n")

    return {

        "context": combined_context,

        "sources": sources,

        "relevance_score":
        average_distance,

        "keyword_match_score":
        keyword_match_score
    }
    