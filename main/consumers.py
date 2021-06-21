import json
from random import randint as rand
from time import sleep
from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    def connect(self):
        pass

