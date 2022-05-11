# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # buttons = []
        # buttons.append({"title": "Sure", "payload": "affirm"})
        # buttons.append({"title": "Not Now!", "payload": "Bye"})
        # customername=tracker.get_slot("customername")
        # agencyname=tracker.get_slot("agencyname")
        customername = 'Zahor'
        agencyname = 'XXX'
        dispatcher.utter_message(text ="Hi {}, This is us from the agency {}. In a short process, we can arrange all insurance and pension payments for you and check whether there is double insurance, unnecessary coverage and the possibility of reducing management fees. It's free and only takes a few minutes.".format(customername, agencyname))
        return []


class ActionGreetFollowUp(Action):

    def name(self) -> Text:
        return "action_greet_followup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # buttons = []
        # buttons.append({"title": "Edit Email", "payload": "Edit Email"})
        # buttons.append({"title": "Edit Issue Date", "payload": "Edit Issue Date"})
        # buttons.append({"title": "Edit ID", "payload": "Edit ID"})
        # buttons.append({"title": "Confirm Details", "payload": "yes"})
        # customername=tracker.get_slot("customername")
        # agencyname=tracker.get_slot("agencyname")
        customername = 'Zahor'
        agencyname = 'XXX'
        id = '123456789'
        issue_date = '01/01/2020'
        email = 'example@example.com'
        # Getting the value of the slot id.
        # id = tracker.get_slot("id")
        # issuedate = tracker.get_slot("issuedate")
        # email = tracker.get_slot("email")
        dispatcher.utter_message(text ="Hi {},Glad you chose to move forward. In order for us to start sorting out your insurance and pension savings, it is important that we understand what products you already have in the various insurance companies.".format(customername))
        dispatcher.utter_message(text ="To do this we will need to confirm the existing details about you:")
        dispatcher.utter_message(text ="id no:{id},".format(id))
        dispatcher.utter_message(text ="issue date:{},".format(issuedate))
        dispatcher.utter_message(text ="email address:{}".format(email)) 
        dispatcher.utter_message(text ="Do You need to edit any of the above data? If yes, please let us know your option (Edit Email, Edit Id, Edit Issue Date).")
        return []


class ActionUpdateEmail(Action):

    def name(self) -> Text:
        return "action_update_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # buttons = []
        # buttons.append({"title": "Edit Email", "payload": "Edit Email"})
        # buttons.append({"title": "Edit Issue Date", "payload": "Edit Issue Date"})
        # buttons.append({"title": "Edit ID", "payload": "Edit ID"})
        # buttons.append({"title": "Confirm Details", "payload": "yes"})
        # customername=tracker.get_slot("customername")
        # agencyname=tracker.get_slot("agencyname")
        customername = 'Zahor'
        agencyname = 'XXX'
        id = '123456789'
        issue_date = '01/01/2020'
        email = 'example@example.com'
        new_email = tracker.get_slot("email")
        # issuedate = tracker.get_slot("issuedate")
        # email = tracker.get_slot("email")
        dispatcher.utter_message(text ="We will now need your digital signature so we can request the data on your behalf from the insurance company, insurance companies and the pension clearing house. A copy of the signed forms will be sent to you at the email address.")
        dispatcher.utter_message(text ="To do Please visit the following [Link](https://prescient-automation.com). Remember after you have signed. Please come back to chat and say *Signed*.")
        # dispatcher.utter_message(text ="id no:{id},".format(id))
        # dispatcher.utter_message(text ="issue date:{},".format(issuedate))
        # dispatcher.utter_message(text ="email address:{}".format(email)) 
        # dispatcher.utter_message(text ="Do You need to edit any of the above data? If yes, please let us know your option (Edit Email, Edit Id, Edit Issue Date).")
        return []



class ActionUpdateIssueDate(Action):

    def name(self) -> Text:
        return "action_update_issue_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # buttons = []
        # buttons.append({"title": "Edit Email", "payload": "Edit Email"})
        # buttons.append({"title": "Edit Issue Date", "payload": "Edit Issue Date"})
        # buttons.append({"title": "Edit ID", "payload": "Edit ID"})
        # buttons.append({"title": "Confirm Details", "payload": "yes"})
        # customername=tracker.get_slot("customername")
        # agencyname=tracker.get_slot("agencyname")
        customername = 'Zahor'
        agencyname = 'XXX'
        id = '123456789'
        issue_date = '01/01/2020'
        email = 'example@example.com'
        new_issue_date = tracker.get_slot("issue_date")
        # issuedate = tracker.get_slot("issuedate")
        # email = tracker.get_slot("email")
        dispatcher.utter_message(text ="We will now need your digital signature so we can request the data on your behalf from the insurance company, insurance companies and the pension clearing house. A copy of the signed forms will be sent to you at the email address.")
        dispatcher.utter_message(text ="To do Please visit the following [Link](https://prescient-automation.com). Remember after you have signed. Please come back to chat and say *Signed*.")
        # dispatcher.utter_message(text ="id no:{id},".format(id))
        # dispatcher.utter_message(text ="issue date:{},".format(issuedate))
        # dispatcher.utter_message(text ="email address:{}".format(email)) 
        # dispatcher.utter_message(text ="Do You need to edit any of the above data? If yes, please let us know your option (Edit Email, Edit Id, Edit Issue Date).")
        return []


class ActionUpdateId(Action):

    def name(self) -> Text:
        return "action_update_ID"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # buttons = []
        # buttons.append({"title": "Edit Email", "payload": "Edit Email"})
        # buttons.append({"title": "Edit Issue Date", "payload": "Edit Issue Date"})
        # buttons.append({"title": "Edit ID", "payload": "Edit ID"})
        # buttons.append({"title": "Confirm Details", "payload": "yes"})
        # customername=tracker.get_slot("customername")
        # agencyname=tracker.get_slot("agencyname")
        customername = 'Zahor'
        agencyname = 'XXX'
        id = '123456789'
        issue_date = '01/01/2020'
        email = 'example@example.com'
        new_ID = tracker.get_slot("ID")
        # issuedate = tracker.get_slot("issuedate")
        # email = tracker.get_slot("email")
        dispatcher.utter_message(text ="We will now need your digital signature so we can request the data on your behalf from the insurance company, insurance companies and the pension clearing house. A copy of the signed forms will be sent to you at the email address.")
        dispatcher.utter_message(text ="To do Please visit the following [Link](https://prescient-automation.com). Remember after you have signed. Please come back to chat and say *Signed*.")
        # dispatcher.utter_message(text ="id no:{id},".format(id))
        # dispatcher.utter_message(text ="issue date:{},".format(issuedate))
        # dispatcher.utter_message(text ="email address:{}".format(email)) 
        # dispatcher.utter_message(text ="Do You need to edit any of the above data? If yes, please let us know your option (Edit Email, Edit Id, Edit Issue Date).")
        return []

class ActionVerifySigned(Action):

    def name(self) -> Text:
        return "action_verify_signed"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # buttons = []
        # buttons.append({"title": "Edit Email", "payload": "Edit Email"})
        # buttons.append({"title": "Edit Issue Date", "payload": "Edit Issue Date"})
        # buttons.append({"title": "Edit ID", "payload": "Edit ID"})
        # buttons.append({"title": "Confirm Details", "payload": "yes"})
        # customername=tracker.get_slot("customername")
        # agencyname=tracker.get_slot("agencyname")
        customername = 'Zahor'
        agencyname = 'XXX'
        id = '123456789'
        issue_date = '01/01/2020'
        email = 'example@example.com'
        new_ID = tracker.get_slot("ID")
        # issuedate = tracker.get_slot("issuedate")
        # email = tracker.get_slot("email")
        dispatcher.utter_message(text ="Excellent we get out to collect data for you. Agent from us will contact you to help you with exist situation")
        # dispatcher.utter_message(text ="To do Please visit the following [Link](https://prescient-automation.com). Remember after you have signed. Please come back to chat and say *Signed*.")
        # dispatcher.utter_message(text ="id no:{id},".format(id))
        # dispatcher.utter_message(text ="issue date:{},".format(issuedate))
        # dispatcher.utter_message(text ="email address:{}".format(email)) 
        # dispatcher.utter_message(text ="Do You need to edit any of the above data? If yes, please let us know your option (Edit Email, Edit Id, Edit Issue Date).")
        return []

