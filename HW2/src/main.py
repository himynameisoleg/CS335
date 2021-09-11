from knowledgebases.farewells import Farewells
from knowledgebases.greetings import Greetings
from handlers.context import Context
from handlers.sentiment import Sentiment
from bot import Bot
from user import User

bot = Bot("Eliza")
user = User()
context = Context();

def begin_dialog():
    # bot initiates convo, asks for name
    context.msg = input("Hi, what's your name? \n")
    user.name = Context.get_name(context.msg)
    context.msg = input(Greetings.get_msg(user.name))
     
    #dialog begins
    goodbye = False
    while (not goodbye):
        if context.msg == "bye":
            goodbye = True
            bot.respond(Farewells.get_msg(user.name))
        else:
            bot.respond(Sentiment.get_sentiment(context.msg))
            context.msg = input()
            

begin_dialog()