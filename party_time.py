from app import MurderMysteryParty
import time
import pprint

welcome_message = """
Welcome, detective extraordinaire! Prepare to unlock the secrets of our murder mystery extravaganza. But remember, if you stumble upon a lifeless body, keep the screams low-key, as we don't want the bobbies knocking on our door. Instead, put on your detective hat, channel your inner Sherlock, and get ready to crack this case like a true champ. And don't worry, our suspicious-looking butler is harmless...
"""

innocent_message = "Hello agent. You are not the murderer. Well done for upholding the law. You are a lovely person. Good job."

murder_message = "Hello agent. You have committed a murder! Naughty! Keep it hush hush ;)."

phonebook = [
    {
    "real_name": "",
    "phone_number": "",
    "alias": "",
    "description": "",
    },]

cahoots = {
    "title": "The Big Banana Cahoots",
    "description": "Find a .",
    "starting_messages": {"everyone_else": "A secret mission has begun. Someone has been chosen to complete the mission. Is it you? I don't know... is it? If it isn't keep your eyes PEELED otherwise things might go PEAR-shaped!", "chosen_one": "A secret mission has begun. Someone has been chosen to complete the mission. Is it you? YES IT IS. Quick get to a secret location so we can send you some more details."},
    "during_messages": {"everyone_else": "Nothing to see here ^-^!", "chosen_one": "You must find a piece of fruit or a vegetable and carry it around discretely or otherwise. You must then talk about the piece of fruit or vegetable to at least 5 people. To successfully complete the mission at least 5 vegetable victims (one who you bored with vegetable chat) must remember your conversation. You've got 30 mins to complete the mission. Good luck agent."},
    "ending_messages": {"everyone_else": "The secret mission has come to an end, time to guess who it was and what they were doing!", "chosen_one": "Your mission is over."},
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
