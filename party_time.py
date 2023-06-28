import pprint
import time

from app import MurderMysteryParty

welcome_message = """
Welcome, detective extraordinaire!
Prepare to unlock the secrets of our murder mystery extravaganza.
Don't mind the butler...
"""

innocent_message = """
Hello agent. Are you the murderer? Let's find out ...
You are not! Well done for upholding the law and be careful out there.
"""

murder_message = """
    Hello agent. Are you the murderer? Let's find out ...
    You are!!!!! OMG! Everyone's looking for you so be careful and cover your tracks.
"""

phonebook = [
    {
        "real_name": "",
        "phone_number": "",
        "alias": "",
        "description": "",
    },
]

cahoots = {
    "title": "The Big Banana Cahoots",
    "description": "Find a .",
    "starting_messages": {
        "everyone_else": """A secret mission has begun.
        Someone has been chosen to complete the mission.
        Is it you? I don't know... is it?
        If it isn't keep your eyes PEELED otherwise things might go PEAR-shaped!""",
        "chosen_one": """
        A secret mission has begun.
        Someone has been chosen to complete the mission. Is it you?
        YES IT IS.
        Quick get to a secret location so we can send you some more details.""",
    },
    "during_messages": {
        "everyone_else": "Nothing to see here ^-^!",
        "chosen_one": """You must find a piece of fruit or a vegetable
        and carry it around discretely or otherwise.
        You must then talk about the piece of fruit or vegetable to at least 5 people.
        To successfully complete the mission at least 5 vegetable victims
        (ones you bored with vegetable chat) must remember your conversation.
        You've got 30 mins to complete the mission. Good luck agent.""",
    },
    "ending_messages": {
        "everyone_else": """
        The secret mission has come to an end,
        time to guess who it was and what they were doing!
        """,
        "chosen_one": "Your mission is over.",
    },
}

print("The party is starting...")

party = MurderMysteryParty()

print("Registering agents...")

party.add_phonebook(phonebook)

pprint.pprint(party.guests)
time.sleep(3)

party.send_to_all(welcome_message)

party.murder()
party.send_innocents_message(innocent_message)
party.send_murderer_message(murder_message)

party.create_cahoots(cahoots)
party.continue_cahoots(cahoots)
party.end_cahoots(cahoots)
