from fastapi import APIRouter
from app.core.logger import logger

router = APIRouter()

@router.get("/")
async def health_check():

    logger.info("Health check endpoint called")

    return {
        "status": "healthy"
    }