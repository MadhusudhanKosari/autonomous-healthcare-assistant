from fastapi import APIRouter

from app.services.chat_memory import (
    clear_memory
)

router = APIRouter()


@router.post("/new-chat")
async def new_chat():

    clear_memory()

    return {
        "message": "new chat started"
    }