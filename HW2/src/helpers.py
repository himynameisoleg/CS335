import re

class Helpers:
    def get_name(self, msg):
        if msg and len(msg.split(" ")) == 1:
            return msg
    
        elif len(self.get_name_regex(msg)) > 0:
            return self.get_name_regex(msg)[0]
        else:
            return "friend"

    def get_name_regex(msg):
        return re.findall(r"(?<=\bam\s)\w+|(?<=\bis\s)\w+|(?<=\bim\s)\w+|(?<=\bi'm\s)\w+", msg, re.IGNORECASE)

    def get_question_regex(msg):
        reg = re.findall(rf'\?', msg)
        return True if reg else False
    
    def get_directed_question_regex(msg):
        reg = re.findall(rf'you', msg, re.IGNORECASE)
        return True if reg else False

    def get_past_tense_regex(msg):
        reg = re.findall(rf'(\w+)ed\b', msg, re.IGNORECASE)
        if reg:
            return reg[0]