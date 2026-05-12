from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router

from app.core.config import settings

from app.database.db import engine
from app.database.models import Base


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(

    title=settings.APP_NAME,

    version="1.0.0"
)


# CORS Middleware
app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# Include API routes
app.include_router(api_router)


@app.get("/")
async def root():

    return {

        "message": settings.APP_NAME
    }