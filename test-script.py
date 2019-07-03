
import sys
import os
import time
from SpannerTestboard import SpannerTestboard

import http.client, urllib.parse
import json

from random import randint

testboard = SpannerTestboard("Testboard1")
device_id = os.environ['device_id']
particle_token = os.environ['particle_token']

OUTPUT_PIN = "D3"

RELAY_PIN = "A5"

INPUT_PIN_RED = "A3"
INPUT_PIN_GREEN = "A2"
INPUT_PIN_BLUE = "A1"
INPUT_PIN_WHITE = "A0"

def turn_device_on():
    print ("++++ Turning Device On ++++")
    testboard.digitalWrite(RELAY_PIN, 'HIGH')
    print ("++++        Done       ++++")

def turn_device_off():
    print ("++++ Turning Device Off ++++")
    testboard.digitalWrite(RELAY_PIN, 'LOW')
    print ("++++        Done        ++++")

def testDevice():
    turn_device_on()
    time.sleep(5)
    turn_device_off()
    assert True
