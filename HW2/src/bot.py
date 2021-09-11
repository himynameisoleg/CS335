class Bot:

    def __init__(self, name):
        self.name = name

    def respond(self, msg):
      print(msg)

    def respond_with_context(self, context):
        if context.question["is_question"]:
            self.respond("Hmm good question, IDK")

        elif context.relationship["is_relationship"]:
            self.respond(f"Tell me more about your {context.relationship['name']}.")

        elif context.feeling:
            self.respond(f"Sounds like you are feeling {context.feeling}.")
        
        else:
            self.respond(f"Hmm idk that one...")