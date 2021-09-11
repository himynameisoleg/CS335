import re
from knowledgebases.feelings import Feelings
from knowledgebases.relationships import Relationships

class Sentiment:
    def get_question_sentiment(msg):
        return { "is_question": False, "topic": "" }

    def get_relationship_sentiment(msg):
        relationship = { 
            "is_relationship": True if Relationships.get_relationship(msg) else False, 
            "name": Relationships.get_relationship(msg) 
        }

        return relationship
    
    def get_feeling_sentiment(msg):
        return Feelings.get_feeling(Feelings, msg)
    

        