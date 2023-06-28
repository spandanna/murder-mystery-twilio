from twilio.rest import Client
import random
import os
from dotenv import load_dotenv

load_dotenv()

class Guest:
    def __init__(
        self,
        real_name: str,
        phone_number: str,
        alias: str,
        description: str,
    ):
        self.is_murderer = False
        self.real_name = real_name
        self.phone_number = phone_number
        self.alias = alias
        self.description = description
        self.cahoots = []

    @classmethod
    def from_dict(cls, dict: dict):
        return cls(
            real_name=dict["real_name"],
            phone_number=dict["phone_number"],
            alias=dict["alias"],
            description=dict["description"],
        )

    def commit_a_murder(self):
        self.is_murderer = True

    def assign_cahoots(self, dict: dict):
        self.cahoots += [dict]


class MurderMysteryParty:
    def __init__(self):
        # Twilio stuff
        self.account_sid = os.environ.get("ACCOUNT_SID")
        self.auth_token = os.environ.get("AUTH_TOKEN")
        self.messaging_service_sid = os.environ.get("MESSAGING_SERVICE_SID")
        self.from_number = os.environ.get("FROM_NUMBER")

        # party stuff
        self.guests = []
        self.guest_count = 0
        self.murderer = None
        self.chosen_one = None
    
    def update_guest_count(func):
        def _method(self, *args):
            func(self, *args)
            self.guest_count = len(self.guests)
        return _method

    @update_guest_count
    def add_guest(self, guest: Guest):
        self.guests += [guest]

    @update_guest_count
    def add_phonebook(self, phonebook: dict):
        for guest in phonebook:
            guest = Guest.from_dict(guest)
            self.add_guest(guest)

    def murder(self):
        if not self.murderer:
            murderer_index = random.randint(0, self.guest_count - 1)
            self.murderer = self.guests[murderer_index]
            self.murderer.commit_a_murder()
            return "A murder has been committed."
        else:
            return "The murderer is already at large."

    def get_random_guest(self):
        index = random.randint(0, self.guest_count - 1)
        chosen_one = self.guests[index]
        return chosen_one

    def send_text(self, phone_number: str, message: str):
        client = Client(username=self.account_sid, password=self.auth_token)
        message = client.messages.create(
            to=phone_number, from_=self.from_number, body=message
        )

    def send_to_all(self, message: str):
        for person in self.guests:
            self.send_text(phone_number=person.phone_number, message=message)

    def send_to_all_except(
        self, normal_message: str, except_message: str, except_guest: Guest
    ):
        for person in self.guests:
            if not person == except_guest:
                self.send_text(
                    phone_number=person.phone_number, message=normal_message
                )
            elif person == except_guest:
                self.send_text(phone_number=person.phone_number, message=except_message)

    def send_innocents_message(self, message: str):
        for person in self.guests:
            if not self.is_murderer:
                self.send_text(phone_number=person.phone_number, message=message)

    def send_murderer_message(self, message: str):
        self.murderer.send_text(phone_number=self.murderer.phone_number, message=message)
    

    def create_cahoots(self, cahoots_dict: dict):
        if not self.chosen_one:
            chosen_one = self.get_random_guest()
            chosen_one.assign_cahoots(cahoots_dict)
            starting_messages = cahoots_dict["starting_messages"]
            self.send_to_all_except(
                starting_messages["everyone_else"], starting_messages["chosen_one"], chosen_one
            )
            self.chosen_one = chosen_one
            return "The chosen one has been chosen."
        elif self.chosen_one:
            return "The chosen one has already been chosen. Finish the current quest before beginning a new one!"

    def continue_cahoots(self, cahoots_dict: dict):
        if self.chosen_one:
            during_messages = cahoots_dict["during_messages"]
            self.send_to_all_except(
                during_messages["everyone_else"], during_messages["chosen_one"], self.chosen_one
            )            
            return "The chosen one continues to be chosen"
        elif not self.chosen_one:
            return "A chosen one must first be chosen before cahoots can continue."
    
    def end_cahoots(self, cahoots_dict: dict):
        if self.chosen_one:
            ending_messages = cahoots_dict["ending_messages"]
            self.send_to_all_except(
                ending_messages["everyone_else"], ending_messages["chosen_one"], self.chosen_one
            )
            self.chosen_one = None    
            return "An end has been put to the cahoots."
        elif not self.chosen_one:
            return "A chosen one must first be chosen before cahoots can be ended."



    