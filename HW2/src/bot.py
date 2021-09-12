import random

class Bot:

    def __init__(self, name):
        self.name = name

    def respond(self, msg):
      print(msg)

    def respond_with_context(self, context):
        if context.question["is_question"]:
            self.respond(
                random.choice([
                    "Hmm good question.",
                    f"That's a great question, {context.user.name}",
                    "Excellent question."
                ])
            )

        if context.response["is_response"]:
            self.respond(context.response["response"])

        elif context.relationship["is_relationship"]:
            self.respond(f"Tell me more about your {context.relationship['name']}.")

        elif context.feeling:
            self.respond(f"Sounds like you are feeling {context.feeling}.")
        
        else:
            self.respond(
                random.choice([
                    "Hmm ok, so what then?",
                    "Interesting. Tell me more.",
                    "Mhmm... anyways",
                    "Let's change the topic, im getting bored.",
                    "Wanna gossip about someone?",
                    "Anyways, why dont you tell me about someone in your life."
                    "What else?",
                    "Uhuh uhuh..."
                    ])
            )