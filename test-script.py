
import sys
import time
import Spanner
from Testboard import Testboard

import http.client, urllib.parse
import json

from random import randint

testboard = Testboard("Testboard1")

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

def testDeviceOnThenOff():
    turn_device_on()
    time.sleep(30)
    turn_device_off()
    assert True
