import random
import re
from app.chatbot.chatbot_flight import flight
from app.chatbot.chatbot_config import respond, usr
from app.preprocessing.preprocessing import cool_preproc


# Here, you indicate regex or keywords that trigger the corresponding topic (function).
def matches(usr_txt):

    # Goodbye when exiting chat.
    if re.match(r'exit|bye|stop|stahp', usr_txt.lower()):
        return "Thanks for talking to me."

    else:
        # Default answer when no matches found.
        return "Human, please employ logic. I don't understand."


def hello():
    greetings = ["How can I help you?", "What can I do for you?"]
    return random.choice(greetings)


def run_bot():
    respond("Hello, human.")
    usr_txt = ''
    while not re.match(r'exit|bye|stop|stahp', usr_txt.lower()):
        usr_txt = input(usr)
        if not usr_txt:
            usr_txt = input(usr)
        else:
            respond(matches(usr_txt))
