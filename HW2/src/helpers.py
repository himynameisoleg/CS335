import re

class Helpers:
    def get_name(self, msg):
        if msg and len(msg.split(" ")) == 1:
            return msg
    
        elif len(self.get_name_regex(msg)) > 0:
            return self.get_name_regex(msg)[0]

        # elif len(re.findall('(?<=is\s)\w+', input)) > 0:
        #     return re.findall('(?<=is\s)\w+', input)[0]
        # elif len(re.findall('(?<=am\s)\w+', input)) > 0:
        #     return re.findall('(?<=am\s)\w+', input)[0]
        # elif len(re.findall('(?<=I\'m\s)\w+', input)) > 0:
        #     return re.findall('(?<=I\'m\s)\w+', input)[0]
        else:
            return "friend"

    def get_name_regex(msg):
        return re.findall(r"(?<=\bam\s)(\w+)|(?<=\bis\s)(\w+)|(?<=\bim\s)(\w+)|(?<=\bI'm\s)(\w+)", msg)