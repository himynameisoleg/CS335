import re

class Feelings:
    POSITIVE = ["well", "good", "great", "amazing", "happy", "joyful", "wonderful", "excit", "glad"]
    NEGATIVE = ["dissapoint", "upset", "bad", "not good", "angry", "annoy"]
    NEUTRAL = ["fine", "normal"]
    
    def has_regex_match(word, msg):
        return re.match(f'{word}\w+|\b{word}\b', msg.lower())

    @staticmethod
    def get_feeling(self, msg):
        for word in Feelings.NEGATIVE:
            if self.has_regex_match(word, msg):
                return "negative"

        for word in Feelings.POSITIVE:
            if self.has_regex_match(word, msg):
                return "positive"

        for word in Feelings.NEUTRAL:
            if self.has_regex_match(word, msg):
                return "neutral"
    
    

