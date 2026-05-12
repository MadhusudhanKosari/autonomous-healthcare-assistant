from app.rag.retriever import retrieve_context

def retrieval_agent(state):

    query = state["query"]

    context = retrieve_context(query)

    state["context"] = context

    return state