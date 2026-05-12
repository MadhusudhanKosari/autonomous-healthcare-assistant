from app.services.llm_service import generate_response

def risk_assessment_agent(state):

    print("\n[Risk Assessment Agent Running]\n")

    analysis = state.get("analysis", "")

    symptom_analysis = state.get("symptom_analysis", "")

    prompt = f"""
You are a healthcare risk assessment assistant.

Medical Analysis:
{analysis}

Symptom Analysis:
{symptom_analysis}

Assess:
- low risk
- moderate risk
- high risk

Explain briefly and safely.

Do NOT provide medical diagnosis.
"""

    risk_assessment = generate_response(prompt)

    state["risk_assessment"] = risk_assessment

    return state