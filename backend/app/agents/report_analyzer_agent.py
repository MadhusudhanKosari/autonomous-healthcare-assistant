from app.services.llm_service import generate_response

def report_analyzer_agent(state):

    context = state["context"]

    query = state["query"]

    prompt = f"""
You are a medical report analysis assistant.

Analyze the medical context carefully.

Medical Context:
{context}

User Question:
{query}

Provide:
- important findings
- simplified explanation
- possible concerns

Answer:
"""

    analysis = generate_response(prompt)

    state["analysis"] = analysis

    return state