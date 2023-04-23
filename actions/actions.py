from typing import Any, Text, Dict, List
from enum import Enum
from random import choice as random_choice

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class Choice(Enum):
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"


def get_computer_choice() -> Choice:
    return random_choice(list(Choice))


class ActionPlayRPS(Action):

    def name(self) -> Text:
        return "action_play_rps"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(tracker.get_slot("choice").upper())
        try:
            user_choice = Choice[tracker.get_slot("choice").upper()]
        except KeyError:
            dispatcher.utter_message(text=f"Incorrect value. Please try again")
            return []

        comp_choice = get_computer_choice()

        dispatcher.utter_message(text=f"You chose {user_choice.value.lower()}")
        dispatcher.utter_message(text=f"The computer chose {comp_choice.value.lower()}")

        if user_choice == comp_choice:
            dispatcher.utter_message(text="It was a tie!")
        elif (user_choice == Choice.ROCK and comp_choice == Choice.SCISSORS) or \
                (user_choice == Choice.PAPER and comp_choice == Choice.ROCK) or \
                (user_choice == Choice.SCISSORS and comp_choice == Choice.PAPER):
            dispatcher.utter_message(text="Congrats, you won!")
        else:
            dispatcher.utter_message(text="The computer won this round.")

        return []
