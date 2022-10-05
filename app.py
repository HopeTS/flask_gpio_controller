from flask import Flask, Response, abort, jsonify, request
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send, emit
from time import sleep
from dotenv import load_dotenv, dotenv_values

from gpio.GPIOController import GPIOController


'''
    Setup
'''

# Set up config
load_dotenv()
global config
config = dotenv_values(".env")


# Configure Flask app
global app
app = Flask(__name__)
app.config['SECRET_KEY'] = config['SECRET_KEY']
#CORS(app, resources={r"/*": {"origins": "*"}})

# Configure websocket
global socketio
socketio = SocketIO(app, cors_allowed_origins=['*'])
socketio.init_app(app, cross_origin=True)

# Set up GPIO Controller
global gpio_controller
gpio_controller = GPIOController(socketio)


'''
    Websocket routes
'''


@socketio.on("echo")
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send(message)


@socketio.on("get-gpio")
def get_gpio(ws):
    global gpio_controller
    data = (gpio_controller.jsonify())
    return {"body": data}


@socketio.on("gpio-update")
def gpio_update(ws):
    global gpio_controller
    data = (gpio_controller.jsonify())
    send(data, json=True)


'''
    Static routes
'''


@app.route("/")
def index():
    ''' Home page '''
    return "<p>This is the server for Raspi 3 Model B GPIO controller</p>"


@app.route("/ping")
def ping():
    ''' Connection test '''
    return {}, 200


@app.route("/get-gpio")
def get_pin_info():
    ''' Retrieve full state of GPIO '''

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

    try:
        # Get values
        request_data = request.get_json(True)
        pin = int(request_data['pin'])
        duration = float(request_data['duration'] or 2.0)
        interval = float(request_data['interval'] or 0.1)

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
    except:
        return abort(400)


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

        return {}, 200
    except:
        return abort(400)


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

    try:
        # Validate environment variables
        if not config['SECRET_KEY']:
            print("No secret key")
            raise
        elif not config['WS_PORT']:
            print("No ws port")
            raise
        elif not config['HTTP_PORT']:
            print("No http port")
            raise

        # Run
        socketio.run(app=app, host='0.0.0.0',
                     port=config['WS_PORT'])
        #app.run(debug=True, port=config['HTTP_PORT'], host="0.0.0.0")

    except:
        print("Something went wrong")
