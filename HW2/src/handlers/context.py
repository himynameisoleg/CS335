import re

class Context:
    msg = ""
    sentiment= ""

    def get_name(input):
        if len(input.split(" ")) == 1:
            return input
        elif len(re.findall('(?<=is\s)\w+', input)) > 0:
            return re.findall('(?<=is\s)\w+', input)[0]
        elif len(re.findall('(?<=am\s)\w+', input)) > 0:
            return re.findall('(?<=am\s)\w+', input)[0]
        elif len(re.findall('(?<=I\'m\s)\w+', input)) > 0:
            return re.findall('(?<=I\'m\s)\w+', input)[0]
        else:
            return "friend"