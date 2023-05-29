# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

account_database = [
    {"name": "John Doe", "balance": 1000, "account_number": "1234", "history": "Your account has been debited Rs.200"},
    {"name": "Jane Smith", "balance": 500,  "account_number": "5678", "history": "Your account has been debited Rs.70"},
    {"name": "Pranjal Khadka", "balance": 2500,  "account_number": "8904", "history": "Your account has been credited Rs.600"},
    {"name": "Bibek Shrestha", "balance": 700,  "account_number": "1278", "history": "Your account has been debited Rs.150"},
    {"name": "Anish Kc", "balance": 900,  "account_number": "6723", "history": "Your account has been credited Rs.500"},
    {"name": "Hari Prasad", "balance": 2000,  "account_number": "6667", "history": "Your account has been credited Rs.1000"}
]

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        account_number = tracker.get_slot("account_number")
        acc_found = False

        for each_data in account_database:
            if(account_number == each_data['account_number']):
                acc_found = True
                name = each_data["name"]
                balance = each_data["balance"]
                dispatcher.utter_message(f"Dear {name}, your account {account_number} has a balance of Rs. {balance}.")
                break

        if not acc_found:
            dispatcher.utter_message("Sorry, the account number is invalid.")

        return []


class ActionCheckTranscationHistory(Action):
    def name(self) -> Text:
        return "action_check_transcation_history"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        name_found = False

        for each_data in account_database:
            if (name == each_data['name']):
                name_found = True
                account_number = each_data["account_number"]
                history = each_data["history"]
                dispatcher.utter_message(f"The recent transaction for account {account_number} is {history}.")
                break

        if not name_found:
            dispatcher.utter_message("Sorry, the name is invalid.")

        return []
