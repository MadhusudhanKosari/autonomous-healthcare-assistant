from fastapi import APIRouter

from fastapi.responses import StreamingResponse

from pydantic import BaseModel

from app.rag.retriever import (

    retrieve_context
)

from app.rag.prompt_builder import (

    build_medical_prompt
)

from app.services.llm_service import (

    stream_response
)

router = APIRouter()


class StreamChatRequest(

    BaseModel
):

    query: str


@router.post("/")
async def stream_chat(

    request: StreamChatRequest
):

    retrieval_result = retrieve_context(

        request.query
    )

    context = retrieval_result["context"]

    sources = retrieval_result["sources"]

    prompt = build_medical_prompt(

        context=context,

        history="",

        query=request.query
    )

    def response_generator():

        full_response = ""

        for chunk in stream_response(

            prompt
        ):

            full_response += chunk

            yield chunk

        source_text = "\n\nSources:\n"

        for source in sources:

            source_text += (

                f"- {source['filename']} "
                f"(chunk {source['chunk_index']})\n"
            )

        yield source_text

    return StreamingResponse(

        response_generator(),

        media_type="text/plain"
    )