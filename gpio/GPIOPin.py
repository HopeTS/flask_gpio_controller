import RPi.GPIO as GPIO


class GPIOPin:
    '''
        Store data about a GPIO pin
    '''

    def __init__(self, name: str, number: int, type: str):
        self.name: str = "".join(name)
        ''' Pin NAME  (Refer to J8 header) '''
        self.type: str = "".join(type)
        ''' Pin TYPE (Refer to J8 header) '''
        self.state = 0
        ''' Pin HIGH/LOW state '''
        self.number = number
        ''' Pin NUMBER (Refer to J8 header) '''

        # Set up pin based on type:
        if self.type == "Power":
            self.state = 1
        try:
            if not self.type == "Power" and not self.type == "Ground":
                GPIO.setup(self.number, GPIO.OUT, initial=GPIO.LOW)
        except:
            print("Pin", self.number, "is not GPIO")
        return

    def __str__(self) -> str:
        return "Pin " + self.number

    def jsonify(self):
        ''' Serialize pin data '''
        return {
            "name": self.name,
            "number": self.number,
            "type": self.type,
            "state": self.state
        }

    def activate(self):
        ''' Set to HIGH state'''
        # Can pin be activated?
        if (self.type is "Ground" or self.type is "Power"):
            print("Can't activate pin of type", self.type)
            return

        # Activate
        GPIO.output(self.number, GPIO.HIGH)
        self.state = 1
        print("Pin activated", self.number)
        return

    def deactivate(self):
        ''' Set to LOW state '''
        # Can pin be activated?
        if (self.type is "Ground" or self.type is "Power"):
            print("Can't activate pin of type", self.type)
            return

        # Activate
        GPIO.output(self.number, GPIO.LOW)
        self.state = 0
        print("Pin deactivated", self.number)
        return

    def reset(self):
        ''' Reset pin '''
        self.deactivate()
        return

    def toggle(self):
        ''' Toggle from HIGH to LOW or LOW to HIGH'''
        if (self.state == 0):
            self.activate()
        else:
            self.deactivate()
        return
