# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 01:02:22 2020

@author: Shubham
"""


import json
import requests
import redis
import websocket
import random,time

ws=websocket.WebSocket()

ws.connect('ws://localhost:8000/ws/polData/')
print("Connected")
lat= 19.884309
lng= 75.330572
for i in range(1000):  
    time.sleep(1)
    lat+=0.00002
    lng+=0.00002
    ws.send(json.dumps({'id':'TW-1', 'lat':lat, 'lng':lng}))