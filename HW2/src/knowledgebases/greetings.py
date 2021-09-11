import random

class Greetings:

    GREETINGS = [
        "Nice to meet you",
        "Thats a nice name",
        "Happy to make your aquaintence"
    ]

    @staticmethod
    def get_msg(name):
        return f"{random.choice(Greetings.GREETINGS)}, {name}.\nHow can I help you?\n"
       