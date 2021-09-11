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
        "friend"
    ]

    @staticmethod
    def get_relationship(msg):
        for name in Relationships.RELATIONSHIPS:
            if re.match(f'{name}\w', msg):
                return name 