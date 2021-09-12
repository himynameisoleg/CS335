import re

class Feelings:
    POSITIVE = ["good", "well", "great", "amazing", "happy", "joyful", "wonderful", "excit", "glad", "sweet", "fantastic","smart", "beautiful","positive","optimistic"]
    NEGATIVE = ["bad", "dissapoint", "upset", "not good", "angry", "annoy", "sad", "mean", "weird", "smelly", "rude", "stupid", "depressed","upset", "worthless", "negative"]
    NEUTRAL = ["fine", "normal", "not bad", "neutral", "so-so", "so so"]
    
    @staticmethod
    def has_regex_match(word, msg):
        reg = re.findall(rf'{word}*\S', msg, re.IGNORECASE)
        return True if reg else False

    @staticmethod
    def get_feeling(msg):
        for word in Feelings.NEGATIVE:
            if Feelings.has_regex_match(word, msg):
                return "negative"

        for word in Feelings.POSITIVE:
            if Feelings.has_regex_match(word, msg):
                return "positive"

        for word in Feelings.NEUTRAL:
            if Feelings.has_regex_match(word, msg):
                return "neutral"
    
    

