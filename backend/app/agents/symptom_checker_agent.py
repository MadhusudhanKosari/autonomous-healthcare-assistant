from app.services.llm_service import generate_response

def symptom_checker_agent(state):

    print("\n[Symptom Checker Agent Running]\n")

    query = state["query"]

    prompt = f"""
You are a healthcare symptom checker assistant.

Analyze these symptoms carefully:

{query}

Provide:
- possible general causes
- common related conditions
- when to seek medical attention

DO NOT diagnose diseases.
DO NOT prescribe medicines.

Answer safely.
"""

    symptom_analysis = generate_response(prompt)

    state["symptom_analysis"] = symptom_analysis

    return state