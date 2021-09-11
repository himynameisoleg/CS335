import re

class Sentiment:
    def get_sentiment(msg):
        if len(msg) == 0:
            return "Try asking me something..."
        else:
            return recognize_sentiment(msg)

    def recognize_sentiment(msg):
        