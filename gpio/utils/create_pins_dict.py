from gpio.GPIOPin import GPIOPin


def create_pins_dict():
    '''
        Returns GPIOController pin dictionary, with all pins set to
        default state 
    '''

    pins = {
        1: GPIOPin(
            name="3.3 VDC",
            number=1,
            type="Power"
        ),
        2: GPIOPin(
            name="5.0 VDC",
            number=2,
            type="Power"
        ),
        3: GPIOPin(
            name="GPIO 8",
            number=3,
            type="SDA1 I2C"
        ),
        4: GPIOPin(
            name="5.0 VDC",
            number=4,
            type="Power"
        ),
        5: GPIOPin(
            name="GPIO 9",
            number=5,
            type="SCL1 I2C"
        ),
        6: GPIOPin(
            name="Ground",
            number=6,
            type="Ground"
        ),
        7: GPIOPin(
            name="GPIO 7",
            number=7,
            type="GPIO"
        ),
        8: GPIOPin(
            name="GPIO 15",
            number=8,
            type="UART0_TXD"
        ),
        9: GPIOPin(
            name="Ground",
            number=9,
            type="Ground"
        ),
        10: GPIOPin(
            name="GPIO 16",
            number=10,
            type="UART0_RXD"
        ),
        11: GPIOPin(
            name="GPIO 0",
            number=11,
            type="GPIO"
        ),
        12: GPIOPin(
            name=" GPIO 1",
            number=12,
            type="PCM_CLK"
        ),
        13: GPIOPin(
            name="GPIO 2",
            number=13,
            type="GPIO"
        ),
        14: GPIOPin(
            name="Ground",
            number=14,
            type="Ground"
        ),
        15: GPIOPin(
            name="GPIO 3",
            number=15,
            type="Ground"
        ),
        16: GPIOPin(
            name="GPIO 4",
            number=16,
            type="GPIO"
        ),
        17: GPIOPin(
            name="3.3 VDC",
            number=17,
            type="Power"
        ),
        18: GPIOPin(
            name="GPIO 5",
            number=18,
            type="GPIO"
        ),
        19: GPIOPin(
            name="GPIO 12",
            number=19,
            type="SPI0_MOSI"
        ),
        20: GPIOPin(
            name="Ground",
            number=20,
            type="Ground"
        ),
        21: GPIOPin(
            name="GPIO 13",
            number=21,
            type="SPI0_MISO"
        ),
        22: GPIOPin(
            name="GPIO 6",
            number=22,
            type="GPIO"
        ),
        23: GPIOPin(
            name="GPIO 14",
            number=23,
            type="SPI0_SCLK"
        ),
        24: GPIOPin(
            name="GPIO 10",
            number=24,
            type="SPI0_CE0_N"
        ),
        25: GPIOPin(
            name="Ground",
            number=25,
            type="Ground"
        ),
        26: GPIOPin(
            name="GPIO 11",
            number=26,
            type="SPI0_CE1_N"
        ),
        27: GPIOPin(
            name="SDA0",
            number=27,
            type="I2C ID EEPROM"
        ),
        28: GPIOPin(
            name="SCL0",
            number=28,
            type="I2C ID EEPROM"
        ),
        29: GPIOPin(
            name="GPIO 21",
            number=29,
            type="GPCLK1"
        ),
        30: GPIOPin(
            name="Ground",
            number=30,
            type="Ground"
        ),
        31: GPIOPin(
            name="GPIO 22",
            number=31,
            type="GPCLK2"
        ),
        32: GPIOPin(
            name="GPIO 26",
            number=32,
            type="PWM0"
        ),
        33: GPIOPin(
            name="GPIO 23",
            number=33,
            type="PWM1"
        ),
        34: GPIOPin(
            name="Ground",
            number=34,
            type="Ground"
        ),
        35: GPIOPin(
            name="GPIO 24",
            number=35,
            type="PCM_FS / PWM1"
        ),
        36: GPIOPin(
            name="GPIO 27",
            number=36,
            type="GPIO"
        ),
        37: GPIOPin(
            name="GPIO 25",
            number=37,
            type="GPIO"
        ),
        38: GPIOPin(
            name="GPIO 28",
            number=38,
            type="PCM_DIN"
        ),
        39: GPIOPin(
            name="Ground",
            number=39,
            type="Ground"
        ),
        40: GPIOPin(
            name="GPIO 29",
            number=40,
            type="PCM_DOUT"
        ),
    }

    return pins
