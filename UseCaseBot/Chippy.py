from webex_bot.models.command import Command
from webex_bot.models.response import Response
import requests

class chippy(Command):
    
    def __init__(self):
        super().__init__(command_keyword="ping", help_message="Ping devices from Webex Chat", card=None)

    def execute(self, message, attachment_actions, activity):
        response = requests.get("http://127.0.0.1:8000/ping")

            # Check the request was successful
        if response.status_code == 200:
                # Extract the JSON data from the response
            data = response.json()

                # Convert the JSON data into a string to send back to the user
            message = "\n".join(f"{key}: {value}" for key, value in data.items())

                # Create and return a new message with the text
            return message

class HelpCommand(Command):
    
    def __init__(self):
        super().__init__()

    def execute(self, message, attachment_actions, activity):
        response = requests.get("http://127.0.0.1:8000/ping")

            # Check the request was successful
        if response.status_code == 200:
                # Extract the JSON data from the response
            data = response.json()

                # Convert the JSON data into a string to send back to the user
            message = "\n".join(f"{key}: {value}" for key, value in data.items())

                # Create and return a new message with the text
            return message