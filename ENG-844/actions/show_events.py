import logging
from typing import Any, Dict, List, Text
from datetime import datetime
# from actions.api.slate import SlateAPI

from rasa_sdk import Action

logger = logging.getLogger(__name__)

def convert_date_format(date_str):
    # Parse the original date string
    date_obj = datetime.strptime(date_str, "%m/%d/%Y %I:%M %p")

    # Format the date to the new format
    new_date_str = date_obj.strftime("%a, %b %d @ %-I:%M%p")
    return new_date_str

class ActionShowEvents(Action):
    def name(self):
        return "action_show_events"

    def run(self, dispatcher, tracker, domain):
        slate_events = [{"event_name":"RNL Discovery Days","start_date":"03/02/2024 09:00 AM","end_date":"03/02/2024 01:30 PM","event_id":"32f69110-1495-42c0-8917-26048a213bb1","registration_link":"https://connect.ruffalonl.com/register/?id=32f69110-1495-42c0-8917-26048a213bb1","event_template":"Special Events","event_category":"RASA Events","event_subcategory":"RNL Discovery Days"},{"event_name":"RNL Discovery Days","start_date":"03/18/2024 09:00 AM","end_date":"03/18/2024 01:30 PM","event_id":"42f6f885-a639-474a-81ce-d0e13382f482","registration_link":"https://connect.ruffalonl.com/register/?id=42f6f885-a639-474a-81ce-d0e13382f482","event_template":"Special Events","event_category":"RASA Events","event_subcategory":"RNL Discovery Days"},{"event_name":"RNL First Look Fridays","start_date":"04/13/2024 09:00 AM","end_date":"04/13/2024 01:30 PM","event_id":"ca6873d7-f724-4ff3-82a8-10c82f9d1b24","registration_link":"https://connect.ruffalonl.com/register/?id=ca6873d7-f724-4ff3-82a8-10c82f9d1b24","event_template":"Special Events","event_category":"RASA Events","event_subcategory":"RNL First Look Fridays"},{"event_name":"RNL First Look Fridays","start_date":"05/03/2024 09:00 AM","end_date":"05/03/2024 01:30 PM","event_id":"4c42490e-e78a-429e-aa02-4ccea0e1d150","registration_link":"https://connect.ruffalonl.com/register/?id=4c42490e-e78a-429e-aa02-4ccea0e1d150","event_template":"Special Events","event_category":"RASA Events","event_subcategory":"RNL First Look Fridays"}]
        events = {event["event_name"] for event in slate_events}
        # events = [events[i]["event_name"] for i in range(len(events))]
        if len(events) == 0:
            dispatcher.utter_message(text=f"Sorry, I couldn't find events.")
        else:
            # Create message with buttons for each available date and an option to cancel
            buttons = []
            for event in events:
                buttons.append(
                    {
                        "title": event,
                        "payload": f"{event}",
                    }
                )
            buttons.append(
                {
                    "title": "Cancel",
                    "payload": "Cancel",
                }
            )
            dispatcher.utter_message(template="utter_ask_event_name_custom_action", buttons=buttons)
            # dispatcher.utter_message(text=f"Here are the available dates for {event_name}.", buttons=buttons)
        return []

class ActionAskEventName(Action):
    def name(self):
        return "action_ask_event_name"

    def run(self, dispatcher, tracker, domain):
        slate_events = [{"event_name":"RNL Discovery Days","start_date":"03/02/2024 09:00 AM","end_date":"03/02/2024 01:30 PM","event_id":"32f69110-1495-42c0-8917-26048a213bb1","registration_link":"https://connect.ruffalonl.com/register/?id=32f69110-1495-42c0-8917-26048a213bb1","event_template":"Special Events","event_category":"RASA Events","event_subcategory":"RNL Discovery Days"},{"event_name":"RNL Discovery Days","start_date":"03/18/2024 09:00 AM","end_date":"03/18/2024 01:30 PM","event_id":"42f6f885-a639-474a-81ce-d0e13382f482","registration_link":"https://connect.ruffalonl.com/register/?id=42f6f885-a639-474a-81ce-d0e13382f482","event_template":"Special Events","event_category":"RASA Events","event_subcategory":"RNL Discovery Days"},{"event_name":"RNL First Look Fridays","start_date":"04/13/2024 09:00 AM","end_date":"04/13/2024 01:30 PM","event_id":"ca6873d7-f724-4ff3-82a8-10c82f9d1b24","registration_link":"https://connect.ruffalonl.com/register/?id=ca6873d7-f724-4ff3-82a8-10c82f9d1b24","event_template":"Special Events","event_category":"RASA Events","event_subcategory":"RNL First Look Fridays"},{"event_name":"RNL First Look Fridays","start_date":"05/03/2024 09:00 AM","end_date":"05/03/2024 01:30 PM","event_id":"4c42490e-e78a-429e-aa02-4ccea0e1d150","registration_link":"https://connect.ruffalonl.com/register/?id=4c42490e-e78a-429e-aa02-4ccea0e1d150","event_template":"Special Events","event_category":"RASA Events","event_subcategory":"RNL First Look Fridays"}]
        events = {event["event_name"] for event in slate_events}
        # events = [events[i]["event_name"] for i in range(len(events))]
        if len(events) == 0:
            dispatcher.utter_message(text=f"Sorry, I couldn't find events.")
        else:
            # Create message with buttons for each available date and an option to cancel
            buttons = []
            for event in events:
                start_date_friendly = convert_date_format(event["start_date"])
                buttons.append(
                    {
                        "title": event["event_name"],
                        "payload": f"show dates for {event['event_name']}",
                    }
                )
            buttons.append(
                {
                    "title": "Cancel",
                    "payload": "greeting",
                }
            )
            dispatcher.utter_message(template="utter_ask_event_name", buttons=buttons)
            # dispatcher.utter_message(text=f"Here are the available dates for {event_name}.", buttons=buttons)
        return []
