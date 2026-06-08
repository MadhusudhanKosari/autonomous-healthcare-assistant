from fastapi import APIRouter

from app.api.routes.upload import router as upload_router

from app.api.routes.stream_chat import router as stream_chat_router


api_router = APIRouter()

api_router.include_router(

    upload_router,

    prefix="/upload",

    tags=["Upload"]
)

api_router.include_router(

    stream_chat_router,

    prefix="/stream-chat",

    tags=["Chat"]
)
from app.api.routes.session import (
    router as session_router
)
api_router.include_router(

    session_router,

    prefix="/session",

    tags=["Session"]
)