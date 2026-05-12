def safety_agent(state):

    recommendations = state["recommendations"]

    safety_note = """

IMPORTANT:
This AI assistant does not replace professional medical advice.
Please consult a licensed doctor for medical decisions.
"""

    final_response = f"""
{recommendations}

{safety_note}
"""

    state["final_response"] = final_response

    return state