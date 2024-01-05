import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)

logger = logging.getLogger(__name__)

INTENT_DESCRIPTION_MAPPING_PATH = "actions/intent_slot_mapping.csv"

class ValidateSchoolForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_school_form"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv(INTENT_DESCRIPTION_MAPPING_PATH)
        self.intent_mappings.fillna("", inplace=True)
        # self.intent_mappings.entities = self.intent_mappings.entities.map(
        #     lambda entities: {e.strip() for e in entities.split(",")}
        # )

    def intent_school_map(self, intent_name, school_name) -> bool:
        # Filter the DataFrame for rows where 'intent' matches intent_name and 'slot_name' matches school_name
        matching_rows = self.intent_mappings[(self.intent_mappings['intent'] == intent_name) & (self.intent_mappings['slot_name'] == school_name)]
        
        # Return True if there are any matching rows, False otherwise
        return not matching_rows.empty

    def validate_school_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        # Get intent that triggered the form
        trigger_intent = tracker.active_loop.get("trigger_message", {}).get("intent", {}).get("name", "")
        # Get sport school_name
        school_name = tracker.get_slot("school_name")
        logger.debug(f"Validating school_name: {school_name}, trigger_intent: {trigger_intent}")
        return {"school_name": school_name, "trigger_intent": trigger_intent}

        # if self.intent_school_map(trigger_intent, school_name):
        #     logger.debug(f"Validating school_name: {school_name}, trigger_intent: {trigger_intent}")
        #     return {"school_name": school_name, "trigger_intent": trigger_intent}
        # else:
        #     logger.debug(f"Validating school_name, setting to other, trigger_intent: {trigger_intent}")
        #     return {"school_name": "other", "trigger_intent": trigger_intent}