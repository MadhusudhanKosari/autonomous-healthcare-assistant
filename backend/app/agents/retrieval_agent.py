from app.rag.retriever import retrieve_context


def retrieval_agent(state):

    query = state["query"]

    retrieval_result = retrieve_context(query)

    state["context"] = retrieval_result["context"]

    state["sources"] = retrieval_result["sources"]

    state["relevance_score"] = retrieval_result["relevance_score"]

    state["keyword_match_score"] = retrieval_result["keyword_match_score"]

    return state