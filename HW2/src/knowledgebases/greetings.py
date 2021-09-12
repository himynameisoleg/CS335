import random

class Greetings:

    GREETINGS = [
        "Nice to meet you",
        "Thats a nice name",
        "Happy to make your aquaintence"
    ]

    LEAD_INS = [
        "How is your day going today?",
        "How are you?",
        "How's it goin?",
        "Whats up?"
    ]

    @staticmethod
    def get_welcome_msg(username, botname):
        welcome = (f"{random.choice(Greetings.GREETINGS)}, {username}.\n"
            f"My name is {botname}.\n"
            f"{random.choice(Greetings.LEAD_INS)}\n"
        )
        
        return welcome
       