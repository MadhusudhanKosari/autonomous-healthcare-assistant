conversation_memory = {
    "messages": [],
    "user_name": None,
    "last_medical_topic": None
}


def save_message(role, content):

    conversation_memory["messages"].append(
        {
            "role": role,
            "content": content
        }
    )


def get_recent_context(limit=6):

    recent = conversation_memory["messages"][-limit:]

    history = ""

    for msg in recent:

        history += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    return history


def set_user_name(name):

    conversation_memory["user_name"] = name


def get_user_name():

    return conversation_memory["user_name"]


def set_last_topic(topic):

    conversation_memory["last_medical_topic"] = topic


def get_last_topic():

    return conversation_memory["last_medical_topic"]


def clear_memory():

    conversation_memory["messages"] = []

    conversation_memory["user_name"] = None

    conversation_memory["last_medical_topic"] = None