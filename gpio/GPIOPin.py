import RPi.GPIO as GPIO


class GPIOPin:
    '''
        Store data about a GPIO pin
    '''

    def __init__(self, name: str, number: int):
        self.name: str = "".join(name)
        ''' Pin NAME  (Refer to J8 header) '''
        self.type = "GPIO"
        ''' Pin TYPE (Refer to J8 header) '''
        self.state = 0
        ''' Pin HIGH/LOW state '''
        number: int = sum(number, 0),
        self.number = number
        ''' Pin NUMBER (Refer to J8 header) '''

        try:
            GPIO.setup(self.number, GPIO.OUT, initial=GPIO.LOW)
        except:
            print("Pin", self.number, "is not GPIO")
        return

    def __str__(self) -> str:
        return "Pin", self.number

    def jsonify(self):
        '''
            Serialize pin data
        '''

        return {
            "name": self.name,
            "number": self.number,
            "type": self.type,
            "state": self.state
        }

    def activate(self):
        ''' Set to HIGH state'''

        GPIO.output(self.number, GPIO.HIGH)
        self.state = 1
        return

    def deactivate(self):
        ''' Set to LOW state '''

        GPIO.output(self.number, GPIO.LOW)
        self.state = 0
        return

    def toggle(self):
        ''' Toggle from HIGH to LOW or LOW to HIGH'''

        if (self.state == 0):
            self.activate()
        else:
            self.deactivate()
        return
