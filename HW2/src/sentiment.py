import re
from knowledgebases.responses import Responses
from knowledgebases.feelings import Feelings
from knowledgebases.relationships import Relationships
from helpers import Helpers

class Sentiment:
    def get_question_sentiment(msg):
        question = { 
            "is_question": Helpers.get_question_regex(msg), 
            "is_directed_at_bot": Helpers.get_directed_question_regex(msg) 
        }
        return question

    def get_relationship_sentiment(msg):
        relationship = { 
            "is_relationship": True if Relationships.get_relationship(msg) else False, 
            "name": Relationships.get_relationship(msg) 
        }
        return relationship

    def get_response_sentiment(msg):
        response = {
            "is_response": True if Responses.get_response(msg) else False,
            "response": Responses.get_response(msg)
        }
        return response

    def get_past_tense_sentiment(msg):
        tense = {
            "is_past_tense": True if Helpers.get_past_tense_regex(msg) else False,
            "word": Helpers.get_past_tense_regex(msg)
        }
        return tense
    
    def get_feeling_sentiment(msg):
        return Feelings.get_feeling(msg)
    