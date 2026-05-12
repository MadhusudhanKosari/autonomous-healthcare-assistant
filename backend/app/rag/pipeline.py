from app.rag.retriever import retrieve_context
from app.rag.prompt_builder import build_medical_prompt

from app.services.llm_service import generate_response
from app.services.memory_service import (
    save_conversation,
    get_conversation_history
)

def run_rag_pipeline(
    session_id: str,
    query: str
):

    history = get_conversation_history(
        session_id
    )

    context = retrieve_context(
        query
    )

    prompt = build_medical_prompt(
        context=context,
        history=history,
        query=query
    )

    response = generate_response(
        prompt
    )

    save_conversation(
        session_id=session_id,
        user_message=query,
        ai_response=response
    )

    return response