import re
import random

class Responses:
    YES = ["yes", "yea", "ya"]
    NO = ["no", "nope", "nah"]
    MAYBE = ["maybe" "sure", "perhaps"]

    @staticmethod
    def get_response(msg):
        for word in Responses.YES:
            if re.match(rf"\b{word}\b", msg, re.IGNORECASE):
                return random.choice(["Yes? Why is that?", "Oh yea?", "No way! Really?"])

        for word in Responses.NO:
            if re.match(rf"\b{word}\b", msg, re.IGNORECASE):
                return random.choice(["Oh, why not?", "No? How come?", "Why do you say No?"])

        for word in Responses.MAYBE:
            if re.match(rf"\b{word}\b", msg, re.IGNORECASE):
                return random.choice(["Maybe so...", "Maybe lets circle back?", "Yea, maybe..."])
