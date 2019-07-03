
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

def send_cmd(command, value):
    BASE_URL = 'api.particle.io'
    API_PATH = '/v1/devices/'

    resource_uri = API_PATH + device_id + '/' + command

    conn = http.client.HTTPSConnection(BASE_URL)
    headers = {'Authorization': 'Bearer ' + particle_token, "Content-type": "application/x-www-form-urlencoded"}
    params = urllib.parse.urlencode({'@arg': value})
    conn.request('POST', resource_uri, params, headers)

    response = conn.getresponse()
    response = response.read().decode()
    json_obj = json.loads(response)
    return json_obj["return_value"]

def set_lamp_color(color):
    print("$$$$ Setting Device Color $$$$")
    print("New Color: " + color)
    return_code = send_cmd("setColor", color)
    if return_code != 1:
        pytest.fail("Failed to set device color")
    print("$$$$   Successfully Set   $$$$")

def turn_device_on():
    print ("++++ Turning Device On ++++")
    testboard.digitalWrite(RELAY_PIN, 'HIGH')
    print ("++++        Done       ++++")

def turn_device_off():
    print ("++++ Turning Device Off ++++")
    testboard.digitalWrite(RELAY_PIN, 'LOW')
    print ("++++        Done        ++++")

def toggle_button():
    print("++++ Simulating Button Press ++++")
    testboard.digitalWrite(OUTPUT_PIN, 'LOW') # Simulate Button press
    time.sleep(1)
    testboard.digitalWrite(OUTPUT_PIN, 'HIGH') # And release the button
    print("++++           Done          ++++")

def testDevice():
    turn_device_on()
    time.sleep(15) # Wait for the lamp to connect to the Wifi

    set_lamp_color("ff000000") # Make the lamp Red
    assert testboard.analogRead(INPUT_PIN_RED) > 3000	# Red LED should be ON
    assert testboard.analogRead(INPUT_PIN_GREEN) < 1000	# Green LED should be OFF
    assert testboard.analogRead(INPUT_PIN_BLUE) < 1000	# Blue LED should be OFF
    assert testboard.analogRead(INPUT_PIN_WHITE) < 1000	# White LED should be OFF

    set_lamp_color("00ff0000") # Make the lamp Green
    assert testboard.analogRead(INPUT_PIN_RED) < 1000	# Red LED should be OFF
    assert testboard.analogRead(INPUT_PIN_GREEN) > 3000	# Green LED should be ON
    assert testboard.analogRead(INPUT_PIN_BLUE) < 1000	# Blue LED should be OFF
    assert testboard.analogRead(INPUT_PIN_WHITE) < 1000	# White LED should be OFF

    set_lamp_color("0000ff00") # Make the lamp Blue
    assert testboard.analogRead(INPUT_PIN_RED) < 1000	# Red LED should be OFF
    assert testboard.analogRead(INPUT_PIN_GREEN) < 1000	# Green LED should be OFF
    assert testboard.analogRead(INPUT_PIN_BLUE) > 3000	# Blue LED should be ON
    assert testboard.analogRead(INPUT_PIN_WHITE) < 1000	# White LED should be OFF

    set_lamp_color("000000ff") # Make the lamp White
    assert testboard.analogRead(INPUT_PIN_RED) < 1000	# Red LED should be OFF
    assert testboard.analogRead(INPUT_PIN_GREEN) < 1000	# Green LED should be OFF
    assert testboard.analogRead(INPUT_PIN_BLUE) < 1000	# Blue LED should be OFF
    assert testboard.analogRead(INPUT_PIN_WHITE) > 3000	# White LED should be ON

    toggle_button() # Pressing the button. All LEDs should now be OFF
    assert testboard.analogRead(INPUT_PIN_RED) < 1000	# Red LED should be OFF
    assert testboard.analogRead(INPUT_PIN_GREEN) < 1000	# Green LED should be OFF
    assert testboard.analogRead(INPUT_PIN_BLUE) < 1000	# Blue LED should be OFF
    assert testboard.analogRead(INPUT_PIN_WHITE) < 1000	# White LED should be OFF

    toggle_button()  # The lamp should now return to being WHITE
    assert testboard.analogRead(INPUT_PIN_RED) < 1000	# Red LED should be OFF
    assert testboard.analogRead(INPUT_PIN_GREEN) < 1000	# Green LED should be OFF
    assert testboard.analogRead(INPUT_PIN_BLUE) < 1000	# Blue LED should be OFF
    assert testboard.analogRead(INPUT_PIN_WHITE) > 3000	# White LED should be ON

    turn_device_off()
