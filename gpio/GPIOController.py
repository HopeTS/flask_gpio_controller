import json
from socket import SocketIO

from gpio.GPIOPin import GPIOPin
from gpio.utils.create_pins_dict import create_pins_dict
from gpio.utils.setup_gpio import setup_gpio

global socketio


class GPIOController:
    def __init__(self, socketio: SocketIO) -> None:

        # Setup GPIO board
        setup_gpio()
        pin_data = create_pins_dict()
        self.pins = pin_data
        self.socketio = socketio
        return

    def emit(self):
        ''' Emit changes through websocket '''
        self.socketio.emit("gpio-update")
        return

    def jsonify(self):
        ''' Returns self in json format '''
        pin_data = {}
        for pin in self.pins:
            pin_data[self.pins[pin].number] = self.pins[pin].jsonify()
        return json.dumps(pin_data)

    def toggle_pin(self, pin_number) -> bool:
        ''' Toggle a pin on the GPIO board '''
        if (pin_number > 40 or pin_number < 1):
            print(pin_number, "is outside of GPIO pin array")
            return False

        self.pins[pin_number].toggle()
        self.emit()
        return True

    def reset(self):
        ''' Reset all GPIO '''
        for pin in self.pins:
            self.pins[pin].reset()

        self.emit()
        return
