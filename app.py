from flask import Flask, Response, abort, jsonify
from flask_cors import CORS, cross_origin

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

    print("Here is gpio controller pins", gpio_controller.pins)

    # get serialized pin data
    pin_data = []

    for i in range(len(gpio_controller.pins)):
        pin = {
            "name": gpio_controller.pins[i + 1].name
        }
        pin_data.append(pin)

    print("Here is pin data", pin_data)

    return jsonify({"data": gpio_controller.jsonify()})


@app.route("/update-pin-voltage", methods=['POST'])
def update_pin_voltage(request):
    ''' Activate or deactivate a pin '''

    # Validate request
    if not request.body:
        return abort(400)
    elif not request.body.number:
        return abort(400)
    elif not request.body.state:
        return abort(400)

    # Activate / deactivate pin
    try:
        if (request.body.state == 1):
            gpio_controller.pins[request.body.number].activate()
        elif (request.body.state == 2):
            gpio_controller.pins[request.body.number].deactivate()
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
