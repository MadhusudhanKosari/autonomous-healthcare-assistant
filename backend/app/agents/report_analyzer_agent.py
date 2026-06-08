from app.services.llm_service import generate_response


def report_analyzer_agent(state):

    context = state["context"]

    query = state["query"]

    prompt = f"""
You are an expert medical report analysis agent.

REPORT CONTENT:
{context}

USER QUESTION:
{query}

Your task:

1. Extract patient information if available
2. Extract diagnoses
3. Extract symptoms
4. Extract medications
5. Extract lab results
6. Extract doctor recommendations
7. Answer the user's question directly

Rules:
- Use only report information
- Do not invent data
- If information is absent say:
  "Not found in report"

Answer:
"""

    analysis = generate_response(prompt)

    state["analysis"] = analysis

    return state