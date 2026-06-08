def safety_agent(state):

    recommendations = state["recommendations"]

    final_response = f"""
{recommendations}

---
⚠️ Medical Disclaimer

This assistant provides informational guidance only.

Consult a licensed healthcare professional for diagnosis,
treatment decisions, or emergencies.
"""

    state["final_response"] = final_response

    return state