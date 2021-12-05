class WordProbabilitiesModel:
    word = ""
    positive = 0
    negative = 0
    total = 0

    def __init__(self, word):
        self.word = word