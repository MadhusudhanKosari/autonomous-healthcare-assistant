from app.rag.retriever import retrieve_context

query = "blood pressure"

context = retrieve_context(query)

print(context)