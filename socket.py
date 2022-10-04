from flask import Flask, Response, abort, jsonify, request
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO
from time import sleep
from dotenv import load_dotenv, dotenv_values


from gpio.GPIOController import GPIOController


'''
    Server config
'''


# Setup
load_dotenv()

# Configure flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = dotenv_values("SECRET_KEY")
socketio = SocketIO(app)

# Set up GPIO controller
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
    return {"body": data}


@app.route("/")
def index():
    return "<p>Hello, world</p>"


if __name__ == "__main__":

    socketio.run(app)
