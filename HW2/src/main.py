from knowledgebases.relationships import Relationships
from knowledgebases.farewells import Farewells
from knowledgebases.greetings import Greetings
from helpers import Helpers
from context import Context
from sentiment import Sentiment
from bot import Bot
from user import User

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