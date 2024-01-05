import logging
from typing import Any, Dict, List, Text

from rasa_sdk import Action

logger = logging.getLogger(__name__)

class ActionShowSlots(Action):
    def name(self):
        logger.info("ActionVersion self called")
        # define the name of the action which can then be included in training stories
        return "action_show_slots"

    def run(self, dispatcher, tracker, domain):
        # msg = "Slots:\n"
        msg = "| slot | value |\n|---|---|\n"
        for k, v in tracker.slots.items():
            msg += f"| {k} | {v} |\n"
        dispatcher.utter_message(msg)
        return []
