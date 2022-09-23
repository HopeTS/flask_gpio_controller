from xmlrpc.client import Boolean
from gpio.GPIOPin import GPIOPin
from gpio.utils.create_pins_dict import create_pins_dict
from gpio.utils.setup_gpio import setup_gpio


class GPIOController:
    def __init__(self) -> None:
        print("GPIOController initiated.")

        # Setup GPIO board
        setup_gpio()
        self.pins = create_pins_dict()
        print("Pins created", self.pins)

        return

    def toggle_pin(self, pin_number) -> Boolean:
        '''
            Toggle a pin on the GPIO board
        '''
        if (pin_number > 40 or pin_number < 1):
            print(pin_number, "is outside of GPIO pin array")
            return False

        self.pins[pin_number].toggle()
        return True
