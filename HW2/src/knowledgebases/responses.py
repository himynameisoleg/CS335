import re

class Responses:
    YES = ["yes", "yea", "ya"]
    NO = ["no", "nope"]
    MAYBE = ["maybe"]

    @staticmethod
    def get_response(msg):
        for word in Responses.YES:
            if re.match(f'\b{word}\b', msg.lower()):
                return "yes"

        for word in Responses.NO:
            if re.match(f'\b{word}\b', msg.lower()):
                return "no"

        for word in Responses.MAYBE:
            if re.match(f'\b{word}\b', msg.lower()):
                return "maybe well circle back "
