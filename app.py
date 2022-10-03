from tokenize import Double
from flask import Flask, Response, abort, jsonify, request
from flask_cors import CORS, cross_origin
from time import sleep

from gpio.GPIOController import GPIOController

# Configure Flask server
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def index():
    ''' Home page '''
    return "<p>This is the server for Raspi 3 Model B GPIO controller</p>"


@app.route("/ping")
def ping():
    ''' Test connection '''
    return {}, 200


@app.route("/get-pin-info")
def get_pin_info():
    ''' Retrieve full state of GPIO '''

    global gpio_controller

    # get serialized pin data
    pin_data = []
    for i in range(len(gpio_controller.pins)):
        pin = {
            "name": gpio_controller.pins[i + 1].name
        }
        pin_data.append(pin)

    return jsonify({"body": gpio_controller.jsonify()})


@app.route("/blink", methods=['POST'])
def blink():
    ''' Make pin blink '''

    # Get values
    pin = int(request.args.get("pin") or -1)
    duration = float(request.args.get("duration") or 2.0)
    interval = float(request.args.get("interval") or 0.1)

    # Validate
    if (pin < 1 or pin > 40):
        return abort(400)

    # Blink
    time_left = duration
    while (time_left >= 0):
        global gpio_controller
        gpio_controller.toggle_pin(pin)
        sleep(interval)
        time_left -= interval

    return {}, 200


@app.route("/toggle-pin", methods=['POST'])
def toggle_pin():
    ''' Toggle a pin (LOW to HIGH or HIGH to LOW) '''

    try:
        # Get values
        request_data = request.get_json(True)
        pin = request_data['pin']

        # Toggle pin
        global gpio_controller
        gpio_controller.toggle_pin(pin)
    except:
        return abort(400)

    return {}, 200


@app.route("/custom-loop", methods=['POST'])
def custom_loop():
    # TODO
    return {}, 200


@app.route("/update-pin-voltage", methods=['POST'])
def update_pin_voltage():
    ''' Activate or deactivate a pin '''

    try:
        # Get variable data
        request_data = request.get_json(True)

        pin = int(request_data['pin'])
        state = request_data['state']

        # Activate / deactivate pin
        if (state == "HIGH"):
            gpio_controller.pins[pin].activate()
        elif (state == "LOW"):
            gpio_controller.pins[pin].deactivate()
        else:
            raise
    except:
        return abort(400)

    return "<p>Pin updated</p>"


if __name__ == "__main__":

    # Set up GPIO Controller
    global gpio_controller
    gpio_controller = GPIOController()

    # Run
    app.run(debug=True, host="0.0.0.0")
