import re

class Relationships:

    RELATIONSHIPS = [
        "mom",
        "mother",
        "dad",
        "father",
        "sister",
        "brother",
        "wife",
        "husband",
        "friend",
        "boyfriend",
        "girlfriend",
        "partner"
    ]

    @staticmethod
    def get_relationship(msg):
        for name in Relationships.RELATIONSHIPS:
            reg = re.findall(rf'{name}*\S', msg)
            if reg:
                return reg[0]