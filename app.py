from flask import Flask
from gpio.GPIOController import GPIOController

# Configure Flask server
app = Flask(__name__)

# Set up GPIO Controller
gpio_controller = GPIOController()


@app.route("/")
def index():
    print("Hello world")
    gpio_controller.toggle_pin(32)
    return "<p>Hello world</p>"


if __name__ == "__main__":
    app.run(debug=True)
