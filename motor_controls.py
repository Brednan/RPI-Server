import RPi.GPIO as GPIO
import time

class MotorControls():
    def __init__(self, R1, R2):
        self.R1 = R1
        self.R2 = R2

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.R1, GPIO.OUT)

    def test(self):
        GPIO.output(self.R1, GPIO.HIGH)
        GPIO.output(self.R1, GPIO.LOW)

    def move_forward(self):
        pass


motors = MotorControls(40, 38)
motors.test()