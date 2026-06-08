from fastapi import APIRouter
from pydantic import BaseModel
import re

from app.agents.workflow import app_workflow

from app.rag.retriever import retrieve_context
from app.rag.prompt_builder import build_medical_prompt

from app.services.llm_service import generate_response

from app.services.chat_memory import (
    save_message,
    get_recent_context,
    set_user_name,
    get_user_name,
    set_last_topic,
    get_last_topic
)

router = APIRouter()


class StreamChatRequest(BaseModel):
    query: str


HEALTHCARE_KEYWORDS = {

    "health",
    "medical",
    "doctor",
    "disease",
    "symptom",
    "symptoms",
    "medicine",
    "treatment",
    "blood",
    "pressure",
    "diabetes",
    "heart",
    "kidney",
    "hiv",
    "aids",
    "copd",
    "cancer",
    "fever",
    "pain",
    "infection",
    "nutrition",
    "exercise",
    "hospital",
    "patient",
    "report",
    "glucose",
    "cholesterol",
    "mental",
    "anxiety",
    "depression",
    "headache",
    "headaches",
    "migraine",
    "vomiting",
    "nausea",
    "fatigue",
    "weakness",
    "virus",
    "viral",
    "bacteria",
    "bacterial",
    "lung",
    "liver",
    "brain",
    "stomach",
    "covid",
    "asthma",
    "allergy",
    "rash",
    "cough",
    "cold",
    "flu",
    "breathing",
    "oxygen",
    "dizziness",
    "injury",
    "fracture",
    "arthritis",

    "tired",
    "ill",
    "sick",
    "sleep",
    "insomnia",
    "drowsy",
    "weak",
    "dizzy",
    "body",
    "ache",
    "aches",
    "weight",
    "loss",
    "gain",
    "appetite",
    "thirst",
    "urination"
}


REPORT_KEYWORDS = {

    "report",
    "summary",
    "summarize",
    "patient",
    "diagnosis",
    "diagnoses",
    "medication",
    "medicine",
    "prescription",
    "lab",
    "test",
    "result",
    "results",
    "blood",
    "scan",
    "mri",
    "ct",
    "xray",
    "x-ray",
    "name",
    "age",
    "gender"
}


FOLLOW_UP_WORDS = {

    "it",
    "this",
    "that",
    "these",
    "those",
    "its",
    "they",
    "them",
    "cause",
    "causes",
    "effect",
    "effects",
    "side",
    "sideeffect",
    "sideeffects",
    "symptom",
    "symptoms"
}


def clean_query_words(text: str):

    words = re.findall(
        r"\b\w+\b",
        text.lower()
    )

    return set(words)


def is_healthcare_query(query: str):

    query_lower = query.lower()

    report_phrases = [

        "pdf",
        "report",
        "medical report",
        "uploaded file",
        "uploaded pdf",
        "document",
        "lab report",
        "test result",
        "medical document"
    ]

    if any(
        phrase in query_lower
        for phrase in report_phrases
    ):
        return True

    query_words = clean_query_words(query)

    overlap = query_words.intersection(
        HEALTHCARE_KEYWORDS
    )

    return len(overlap) > 0


@router.post("/")
async def stream_chat(request: StreamChatRequest):

    query_lower = request.query.lower()

    # ==================================
    # NAME MEMORY
    # ==================================

    name_match = re.search(
        r"my name is (\w+)",
        query_lower
    )

    if name_match:

        user_name = name_match.group(1)

        set_user_name(user_name)

        return (
            f"Nice to meet you "
            f"{user_name.title()}. "
            f"How can I help with your healthcare concerns today?"
        )

    if "what is my name" in query_lower:

        saved_name = get_user_name()

        if saved_name:

            return (
                f"Your name is "
                f"{saved_name.title()}."
            )

        return (
            "I do not know your name yet. "
            "Please tell me your name."
        )

    # ==================================
    # DOMAIN VALIDATION
    # ==================================

    query_words = clean_query_words(
        request.query
    )

    previous_topic = get_last_topic()

    contains_follow_up = len(
        query_words.intersection(
            FOLLOW_UP_WORDS
        )
    ) > 0

    if not is_healthcare_query(
        request.query
    ):

        if not (
            previous_topic
            and
            contains_follow_up
        ):

            return """
I am a healthcare-focused AI assistant.

Please ask healthcare, medical, wellness, or medical-report-related questions only.
"""

    # ==================================
    # RETRIEVAL
    # ==================================
    report_question = len(
        query_words.intersection(
            REPORT_KEYWORDS
        )
    ) > 0
    if report_question:

        retrieval_result = retrieve_context(
            request.query
        )

    else:

        retrieval_result = {
            "context": "",
            "sources": [],
            "relevance_score": 999,
            "keyword_match_score": 0
        }
    retrieval_result = retrieve_context(
        request.query
    )

    context = retrieval_result["context"]

    sources = retrieval_result["sources"]

    relevance_score = retrieval_result[
        "relevance_score"
    ]

    keyword_match_score = retrieval_result[
        "keyword_match_score"
    ]

    print("\n========== CONTEXT DEBUG ==========\n")
    print(context[:3000])
    print("\n===================================\n")

    report_question = len(
        query_words.intersection(
            REPORT_KEYWORDS
        )
    ) > 0

    USE_RAG = (
        report_question
        or
        keyword_match_score >= 1
    )

    print("\n========== ROUTING DEBUG ==========")

    print("QUERY:", request.query)
    print("RELEVANCE SCORE:", relevance_score)
    print("KEYWORD SCORE:", keyword_match_score)
    print("USE_RAG:", USE_RAG)

    print("===================================\n")

    # ==================================
    # MULTI AGENT WORKFLOW
    # ==================================

    if USE_RAG:

        workflow_result = app_workflow.invoke(
            {
                "query": request.query,
                "context": context,
                "analysis": "",
                "recommendations": "",
                "final_response": "",
                "symptom_analysis": "",
                "risk_assessment": ""
            }
        )

        response = workflow_result[
            "final_response"
        ]

    else:

        history = get_recent_context()

        prompt = f"""
You are a professional healthcare AI assistant.

Conversation History:
{history}

Current Question:
{request.query}

Instructions:
- Stay in healthcare domain
- Answer clearly
- Use previous context
- Be medically safe
"""

        response = generate_response(
            prompt
        )

    # ==================================
    # MEMORY SAVE
    # ==================================

    save_message(
        "user",
        request.query
    )

    save_message(
        "assistant",
        response
    )

    healthcare_terms = query_words.intersection(
        HEALTHCARE_KEYWORDS
    )

    if healthcare_terms:

        set_last_topic(
            " ".join(
                healthcare_terms
            )
        )

    # ==================================
    # SOURCES
    # ==================================

    if USE_RAG and sources:

        unique_files = set()

        response += "\n\n📄 Referenced Medical Reports:\n"

        for source in sources:

            filename = source["filename"]

            if filename not in unique_files:

                unique_files.add(filename)

                response += f"\n- {filename}"

    return response