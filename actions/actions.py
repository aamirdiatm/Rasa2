# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from typing import Dict, Text, Any, List, Union, Optional
from rasa.core.trackers import DialogueStateTracker
from rasa.core.domain import Domain
from rasa.core.events import (
    SlotSet,
    AllSlotsReset,
    ConversationPaused,
    ConversationResumed,
)
import time
import random
import datetime
import os
import pymongo
import threading 
from multiprocessing.connection import Client
import logging
import requests
import json
from rasa_sdk import Action
### custom actions
#from rasa_core.actions import Action
from rasa.core.events import SlotSet
import requests
#from rasa_sdk.forms import FormAction
import logging
#from datetime import datetime
from typing import Text, Dict, Any, List
import json
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
import requests 
import numpy as np
#import matplotlib.pyplot as plt
#import plotly.express as px
import boto3
import mysql.connector
import traceback
from rasa_sdk.events import UserUtteranceReverted, ConversationPaused

#from rasa_core.trackers import DialogueStateTracker

from rasa.core.domain import Domain
from rasa_sdk.forms import FormAction
#from rasa_core.actions.action import Action
from rasa_sdk.events import (
    SlotSet,
    AllSlotsReset,
    ConversationPaused,
    ConversationResumed,
)

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
