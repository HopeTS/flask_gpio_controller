from gpio.GPIOPin import GPIOPin


def create_pins_dict():
    '''
        Returns GPIOController pin dictionary, with all pins set to
        default state 
    '''

    pins = {
        1: GPIOPin(
            name="3.3 VDC",
            number=1
        ),
        2: GPIOPin(
            name="5.0 VDC",
            number=2
        ),
        3: GPIOPin(
            name="GPIO 8",
            number=3
        ),
        4: GPIOPin(
            name="5.0 VDC",
            number=4
        ),
        5: GPIOPin(
            name="GPIO 9",
            number=5
        ),
        6: GPIOPin(
            name="Ground",
            number=6
        ),
        7: GPIOPin(
            name="GPIO 7",
            number=7
        ),
        8: GPIOPin(
            name="GPIO 15",
            number=8
        ),
        9: GPIOPin(
            name="Ground",
            number=9
        ),
        10: GPIOPin(
            name="GPIO 16",
            number=10
        ),
        11: GPIOPin(
            name="GPIO 0",
            number=11
        ),
        12: GPIOPin(
            name=" GPIO 1",
            number=12
        ),
        13: GPIOPin(
            name="GPIO 2",
            number=13
        ),
        14: GPIOPin(
            name="Ground",
            number=14
        ),
        15: GPIOPin(
            name="GPIO 3",
            number=15
        ),
        16: GPIOPin(
            name="GPIO 4",
            number=16
        ),
        17: GPIOPin(
            name="3.3 VDC",
            number=17
        ),
        18: GPIOPin(
            name="GPIO 5",
            number=18
        ),
        19: GPIOPin(
            name="GPIO 12",
            number=19
        ),
        20: GPIOPin(
            name="Ground",
            number=20
        ),
        21: GPIOPin(
            name="GPIO 13",
            number=21
        ),
        22: GPIOPin(
            name="GPIO 6",
            number=22
        ),
        23: GPIOPin(
            name="GPIO 14",
            number=23
        ),
        24: GPIOPin(
            name="GPIO 10",
            number=24
        ),
        25: GPIOPin(
            name="Ground",
            number=25
        ),
        26: GPIOPin(
            name="GPIO 11",
            number=26
        ),
        27: GPIOPin(
            name="SDA0",
            number=27
        ),
        28: GPIOPin(
            name="SCL0",
            number=28
        ),
        29: GPIOPin(
            name="GPIO 21",
            number=29
        ),
        30: GPIOPin(
            name="Ground",
            number=30
        ),
        31: GPIOPin(
            name="GPIO 22",
            number=31
        ),
        32: GPIOPin(
            name="GPIO 26",
            number=32
        ),
        33: GPIOPin(
            name="GPIO 23",
            number=33
        ),
        34: GPIOPin(
            name="Ground",
            number=34
        ),
        35: GPIOPin(
            name="GPIO 24",
            number=35
        ),
        36: GPIOPin(
            name="GPIO 27",
            number=36
        ),
        37: GPIOPin(
            name="GPIO 25",
            number=37
        ),
        38: GPIOPin(
            name="GPIO 28",
            number=38
        ),
        39: GPIOPin(
            name="Ground",
            number=39
        ),
        40: GPIOPin(
            name="GPIO 29",
            number=40
        ),
    }

    return pins
