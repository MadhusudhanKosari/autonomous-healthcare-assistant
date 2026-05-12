from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.workflow import app_workflow

router = APIRouter()

class ChatRequest(BaseModel):

    session_id: str

    query: str

@router.post("/")
async def chat(request: ChatRequest):

    try:

        result = app_workflow.invoke({

            "query": request.query

        })

        return {

            "session_id": request.session_id,

            "query": request.query,

            "response": result["final_response"]

        }

    except Exception as e:

        return {

            "error": str(e)

        }