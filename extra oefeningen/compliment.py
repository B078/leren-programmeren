import random

def get_random_compliment(naam: str) -> str:
    COMPLIMENTEN = ("Je bent geweldig", "Er is geen betere", "Je bent de beste")
    random_compliment = random.choice(COMPLIMENTEN)
    return f"{random_compliment}, {naam}!"

print(get_random_compliment("Bjorn"))
