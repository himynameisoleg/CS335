""" Forchetta: the Eliza-like Chatbot - have a chat over coffee or gossip about friends. """
__author__="Oleg Perchyk"

# https://github.com/himynameisoleg/CS335/tree/main/HW2/src

import random
import re

class User:
  name = ""
  age = 0
  likes_waffles = False

class Bot:

    def __init__(self, name):
        self.name = name

    def respond(self, msg):
      print(msg)

    def respond_with_context(self, context):

        name = context.user.name

        if context.question["is_question"]:
            if context.question["is_directed_at_bot"]:
                self.respond(
                    random.choice([
                        f"Me? Lets talk about you, {name}.",
                        f"{name}, lets not talk about me so much. Tell me something about, how about someone you know?",
                        f"Lets get back to you, {name}. What did you do yesterday?",
                        f"Was that supposed to be a question for me?",
                        f"You insist on asking questions about me, what about you {name}?"
                    ])
                )
            else:
                self.respond(
                    random.choice([
                        "Hmm good question.",
                        f"That's a great question, {name}.",
                        f"Idk, how would you answer that {name}?"
                    ])
                )

        elif context.response["is_response"]:
            self.respond(context.response["response"])

        elif context.tense["is_past_tense"]:
            word = context.tense["word"]
            
            if word == "go":
                self.respond(
                    random.choice([
                        "Do you like to go there often?",
                        "Why did you go there"
                    ])
                )
            elif word == "do":
                self.respond(
                    random.choice([
                        "You did?",
                        "Tell me more about how you did that."
                    ])
                )
            else:   
                self.respond(
                    random.choice([
                    f"And do you like to {word}?",
                    f"Tell me more about how you {word}?",
                    f"Wait, you {word}ed? What do you mean?"
                    ])
                )

        elif context.relationship["is_relationship"]:
            person = context.relationship['name']
            self.respond(
                random.choice([
                    f"Tell me more about your {person}.",
                    f"Nice. By the way, how is your {person} doing?",
                    f"Your {person} sounds like an interesting character for sure.",
                    f"Wait random question, does your {person} like to eat waffles?",
                    f"Have I met your {person}?"
                ])
            )

        elif context.feeling:
            feeling = context.feeling
            if feeling == "positive":
                self.respond(
                    random.choice([
                        f"Wonderful, love the positivity {name}!",
                        f"Thats great!",
                        f"Thats so super!"
                    ])
                )
            elif feeling == "negative":
                self.respond(
                    random.choice([
                        f"Well that not good at all.",
                        f"{name}, that sounded very negative.",
                        f"I am sensing some negativity."
                    ])
                )
            elif feeling == "neutral":
               self.respond(
                    random.choice([
                        f"Nothing wrong with having a neutral feeling, am I right?",
                        f"You're sounding like Switzerland over here."
                    ])
                )

            if (random.choice([1, 0]) == 1):
                self.generic_response(context)

        else:
            self.generic_response(context)
           


    def generic_response(self, context):
        self.respond(
                random.choice([
                    "Hmm ok, so what then?",
                    "OK so, tell me more.",
                    "Mhmm... (awkward silence)",
                    "Ok. Let's change the topic, im getting bored.",
                    "Cool, so wanna gossip about someone? Who should we talk about?",
                    "Anyways, why dont you tell me about someone in your life.",
                    "Anyways, done anything fun recently?",
                    "Btw, do you have any family here?",
                    "Oh almost forgot to ask, what did you do last night?",
                    "What else?",
                    "Okay. Do anything fun last weekend?"
                ])
            )
  
class Context:
    user = None
    msg = ""
    feeling = ""
    relationship = {
        "is_relationship": False,
        "name": ""
    }
    question = {
        "is_question": False,
        "is_directed_at_bot": False
    }
    response = {
        "is_response": False,
        "response": ""
    }
    tense = {
        "is_past_tense": False,
        "word": ""
    }

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
        reg = re.findall(rf'you|your|yours', msg, re.IGNORECASE)
        return True if reg else False

    def get_past_tense_regex(msg):
        reg = re.findall(rf'(\w+)ed\b', msg, re.IGNORECASE)
        if reg:
            return reg[0]
        elif re.findall(rf'\bwent', msg, re.IGNORECASE):
            return "go"
        elif re.findall(rf'\bdid', msg, re.IGNORECASE):
            return "do"

class Farewells:

  FAREWELLS = [
    "Goodbye",
    "See you later",
    "Talk to you soon",
    "Later",
    "Ciao",
    "Adios",
    "Godspeed",
    "Peace-out",
    "Good luck"
  ]

  @staticmethod
  def get_msg(name):
        return f"{random.choice(Farewells.FAREWELLS)}, {name}.\n"

class Feelings:
    POSITIVE = ["good", "well", "great", "amazing", "happy", "joyful", "wonderful", "excit", "glad", "sweet", "fantastic","smart", "beautiful","positive","optimistic"]
    NEGATIVE = ["bad", "dissapoint", "not so good", "upset", "not good", "angry", "annoy", "sad", "mean", "weird", "smelly", "rude", "stupid", "depressed","upset", "worthless", "negative"]
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
    
class Greetings:

    GREETINGS = [
        "Nice to meet you",
        "Thats a nice name",
        "Happy to make your aquaintence"
    ]

    LEAD_INS = [
        "How is your day going today?",
        "How are you?",
        "How's it goin?",
        "Whats up?"
    ]

    @staticmethod
    def get_welcome_msg(username, botname):
        welcome = (f"{random.choice(Greetings.GREETINGS)}, {username}.\n"
            f"My name is {botname}.\n"
            f"{random.choice(Greetings.LEAD_INS)}\n"
        )
        
        return welcome
       
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
        "boyfriend",
        "girlfriend",
        "partner",
        "child",
        "children",
        "son", 
        "daughter",
        "neice",
        "nephew",
        "friend",
    ]

    @staticmethod
    def get_relationship(msg):
        for name in Relationships.RELATIONSHIPS:
            reg = re.findall(rf'{name}*\S', msg)
            if reg:
                return reg[0]

class Responses:
    YES = ["yes", "yea", "ya"]
    NO = ["no", "nope", "nah"]
    MAYBE = ["maybe" "sure", "perhaps"]

    @staticmethod
    def get_response(msg):
        for word in Responses.YES:
            if re.match(rf"\b{word}\b", msg, re.IGNORECASE):
                return random.choice(["Yes? Why is that?", "Oh yea?", "No way! Really?"])

        for word in Responses.NO:
            if re.match(rf"\b{word}\b", msg, re.IGNORECASE):
                return random.choice(["Oh, why not?", "No? How come?", "Why do you say No?"])

        for word in Responses.MAYBE:
            if re.match(rf"\b{word}\b", msg, re.IGNORECASE):
                return random.choice(["Maybe so...", "Maybe lets circle back?", "Yea, maybe..."])

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
    

bot = Bot("Forchetta")
user = User()
context = Context();

def begin_dialog():
    # bot initiates convo + asks for name
    context.msg = input("Hi, what's your name? \n")
    user.name = Helpers.get_name(Helpers, context.msg)
    context.msg = input(Greetings.get_welcome_msg(user.name, bot.name))
    context.user = user
     
    #dialog begins
    goodbye = False
    while (not goodbye):
        if context.msg == "bye":
            goodbye = True
            bot.respond(Farewells.get_msg(user.name))
        elif not context.msg:
            bot.respond(f"Try asking me something, {user.name}")
            context.msg = input()
        else:
            
            context.feeling = Sentiment.get_feeling_sentiment(context.msg)
            context.question = Sentiment.get_question_sentiment(context.msg)
            context.relationship = Sentiment.get_relationship_sentiment(context.msg)
            context.response = Sentiment.get_response_sentiment(context.msg)
            context.tense = Sentiment.get_past_tense_sentiment(context.msg)

            bot.respond_with_context(context)

            context.msg = input()
            

begin_dialog()