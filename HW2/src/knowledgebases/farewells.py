import random

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
