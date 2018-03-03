from flask import Flask
from flask import jsonify
from flask import request

import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, 1)
state = False

@app.route("/toggle", methods = ['GET', 'POST'])
def toggle():
    global state
    if request.method == 'POST':
        state = (not state)
        GPIO.output(4, (0 if state else 1))
    x = 'Wlaczone' if state else 'Wylaczone'
    return jsonify({"status": x})

