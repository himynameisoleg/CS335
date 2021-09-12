import random

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
                        f"{name}, lets not talk about me so much.",
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

        if context.response["is_response"]:
            self.respond(context.response["response"])

        if context.tense["is_past_tense"]:
            word = context.tense["word"]

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
                        f"{name}, that sounded very negative."
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
                    "Let's change the topic, im getting bored.",
                    "Cool, so wanna gossip about someone? Who should we talk about?",
                    "Anyways, why dont you tell me about someone in your life.",
                    "Anyways, done anything fun recently?",
                    "Btw, do you have any family here?",
                    "Oh almost forgot to ask, what did you do last night?",
                    "What else?",
                    "Okay.\n Do anything fun last weekend?"
                ])
            )