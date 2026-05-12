from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.database.models import Conversation

def save_conversation(
    session_id: str,
    user_message: str,
    ai_response: str
):

    db: Session = SessionLocal()

    conversation = Conversation(
        session_id=session_id,
        user_message=user_message,
        ai_response=ai_response
    )

    db.add(conversation)

    db.commit()

    db.close()
def get_conversation_history(
    session_id: str
):

    db: Session = SessionLocal()

    conversations = db.query(Conversation).filter(
        Conversation.session_id == session_id
    ).all()

    db.close()

    history = ""

    for convo in conversations:

        history += f"""
User: {convo.user_message}

Assistant: {convo.ai_response}
"""

    return history