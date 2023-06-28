# murder-mystery-twilio

A simple project I created to assist in assigning the murderer for a murder mystery party. Unfortunately the code was written very quickly whilst having a drink before the party and someone forgot to run the line that assigned the murderer...

## About the code
Use the `MurderMysteryParty` class to create an instance for your party. `Guests` are made up of a real name, phone number, alias name, and a character description. You must register guests to the party, then you can use the party class to randomly set the murdered and send out messages. Messages can be sent out by the person running the code without finding out who the murderer is.

You can also use `cahoots` to create tasks throughout the party. A cahoot allows you to randomly choose someone to carry out a secret mission. You can orchestrate the secret mission through texts.


## Setting up and running

Set up a twilio account to get access to the messaging API. Put the env variables in an env file. Install requirements and use `party_time` to orchestrate the party.
