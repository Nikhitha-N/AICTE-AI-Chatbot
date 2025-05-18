# This files contains your custom actions which can be used to run
# custom Python code.
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser #inbuit in python for opening the link in web browser

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            # tracker keeps the record of all the conversation i.e going on

            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Welcome, greet by saying 'Hi'")

        return []

class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "action_save_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conversation = tracker.events
        print(conversation)
        import os
        if not os.path.isfile('chats.csv'):
            with open('chats.csv', 'w') as file:
                file.write("intent,user_input,entity_name,entity_value,action,bot_reply\n")
        chat_data = ''
        for i in conversation:
            if i['event'] == 'user':
                chat_data += i['parse_data']['intent']['name']+','+i['text']+','
                print('user: {}'.format(i['text']))
                if len(i['parse_data']['entities']) > 0:
                    chat_data += i['parse_data']['entities'][0]['entity']+','+i['parse_data']['entities'][0]['value']+','
                    print('extra data:', i['parse_data']['entities'][0]['entity'], '=',
                          i['parse_data']['entities'][0]['value'])
                else:
                    chat_data += ",,"
            elif i['event'] == 'bot':
                print('Bot: {}'.format(i['text']))
                try:
                    chat_data += i['metadata']['utter_action']+','+i['text']+'\n'
                except KeyError:
                    pass
        else:
            with open('chats.csv', 'a') as file:
                file.write(chat_data)

        dispatcher.utter_message(text="Your response has been saved.")

        return []
class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        video_url="https://youtu.be/45PLold-zKQ"
        dispatcher.utter_message("Please wait... Connecting to the video")
        webbrowser.open(video_url) #opens in the new tab
        return []

# class ActionService(Action):
#
#     def name(self) -> Text:
#         return "action_service"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#
#         buttons=[
#             {"payload": '/chitchat/ask_login{content_type":"login"}',"title":"Login Issues"},
#             {"payload": '/chitchat/ask_faculty{content_type":"faculty"}', "title": "Faculty Related"},
#             {"payload": '/chitchat/ask_payment{content_type":"payment"}', "title": "Payment Issues"},
#             {"payload": '/chitchat/ask_approval_process{content_type":"approval"}', "title": "Approval Process"},
#             {"payload": '/chitchat/ask_change_details{content_type":"application"}', "title": "Application form"},
#
#             ]
#
#         dispatcher.utter_message(text="Anything I can help you from below?", buttons=buttons)
#
#         return []

#       buttons=[
#                   {
#                       "title": "great",
#                       "payload": "great"
#                   },
#                   {
#                       "title": "super sad",
#                       "payload": "super sad"
#                   }
#               ]
#
# dispatcher.utter_message(text="Hey hi, Anything I can help you from below?", buttons=button)



