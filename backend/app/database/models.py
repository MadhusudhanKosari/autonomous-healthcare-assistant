from sqlalchemy import Column, Integer, String, Text

from app.database.db import Base

class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(String, index=True)

    user_message = Column(Text)

    ai_response = Column(Text)