from app.services.llm_service import generate_response


def recommendation_agent(state):

    analysis = state["analysis"]

    query = state["query"]

    prompt = f"""
You are a healthcare recommendation agent.

User Question:
{query}

Medical Analysis:
{analysis}

Instructions:

- If user asks report-specific question,
  answer directly.

- If diagnosis exists,
  provide useful lifestyle guidance.

- If no recommendation needed,
  simply return the answer.

Answer:
"""

    recommendations = generate_response(prompt)

    state["recommendations"] = recommendations

    return state