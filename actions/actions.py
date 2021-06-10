# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# [rasa run actions] <= on console to activate endpoint

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class BookRoomInfo(FormAction):
    def name(self) -> Text:
        return "form_book_room"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["room_type"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        # utter submit template
        dispatcher.utter_message(template="utter_room_booked",
                                 room_type=tracker.get_slot('room_type'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "room_type": self.from_entity(entity="room_type", intent="type_select_room")
        }


class GetUserName(FormAction):
    def name(self) -> Text:
        return "form_user_name"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["user_name"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        # utter submit template
        dispatcher.utter_message(template="utter_welcome_user",
                                 room_type=tracker.get_slot('user_name'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "user_name": self.from_entity(entity="user_name", intent="introduce")
        }

# class GetUserName(Action):

class ResetSlots(Action):

    def name(self):
        return "action_reset_slots"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("room_type", None)]

