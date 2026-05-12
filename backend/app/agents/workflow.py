from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.agents.retrieval_agent import retrieval_agent
from app.agents.report_analyzer_agent import report_analyzer_agent
from app.agents.recommendation_agent import recommendation_agent
from app.agents.safety_agent import safety_agent


class AgentState(TypedDict):

    query: str

    context: str

    analysis: str

    recommendations: str

    final_response: str

    symptom_analysis: str

    risk_assessment: str

workflow = StateGraph(AgentState)

workflow.add_node(
    "retrieval",
    retrieval_agent
)

workflow.add_node(
    "analysis",
    report_analyzer_agent
)

workflow.add_node(
    "recommendation",
    recommendation_agent
)

workflow.add_node(
    "safety",
    safety_agent
)

workflow.set_entry_point("retrieval")

workflow.add_edge(
    "retrieval",
    "analysis"
)

workflow.add_edge(
    "analysis",
    "recommendation"
)

workflow.add_edge(
    "recommendation",
    "safety"
)

workflow.add_edge(
    "safety",
    END
)



app_workflow = workflow.compile()