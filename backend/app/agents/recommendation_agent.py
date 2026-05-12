from app.services.llm_service import generate_response

def recommendation_agent(state):

    analysis = state["analysis"]

    prompt = f"""
You are a healthcare recommendation assistant.

Based on this medical analysis:

{analysis}

Provide:
- healthy lifestyle recommendations
- diet suggestions
- hydration advice
- exercise suggestions

Avoid dangerous medical claims.

Answer:
"""

    recommendations = generate_response(prompt)

    state["recommendations"] = recommendations

    return state