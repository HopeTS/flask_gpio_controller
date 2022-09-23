from msilib.schema import Error
from flask import Flask, Response, abort, jsonify
from gpio.GPIOController import GPIOController

# Configure Flask server
app = Flask(__name__)

# Set up GPIO Controller
gpio_controller = GPIOController()


@app.route("/")
def index():
    ''' Home page '''

    print("Hello world")
    gpio_controller.toggle_pin(32)
    return "<p>Hello world</p>"


@app.route("/get-pin-info")
def get_pin_info():
    ''' Retrieve full state of GPIO '''

    print("Returning this data", gpio_controller.pins)
    return jsonify(gpio_controller.pins)


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
    app.run(debug=True, host="0.0.0.0")
