class Context:
    user = None
    msg = ""
    feeling = ""
    relationship = {
        "is_relationship": False,
        "name": ""
    }
    question = {
        "is_question": False,
        "is_directed_at_bot": False
    }
    response = {
        "is_response": False,
        "response": ""
    }
    tense = {
        "is_past_tense": False,
        "word": ""
    }