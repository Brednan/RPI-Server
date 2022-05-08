import RPi.GPIO as GPIO
import time

class MotorControls():
    def __init__(self, R1, R2, L1, L2):
        self.R1 = R1
        self.R2 = R2
        self.L1 = L1
        self.L2 = L2

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.R1, GPIO.OUT)
        GPIO.setup(self.R2, GPIO.OUT)
        GPIO.setup(self.L1, GPIO.OUT)
        GPIO.setup(self.L2, GPIO.OUT)


    def move_forward(self):
        GPIO.output(self.R1, GPIO.HIGH)
        GPIO.output(self.R2, GPIO.LOW)
        GPIO.output(self.L1, GPIO.HIGH)
        GPIO.output(self.L2, GPIO.LOW)

    def stop_motors(self):
        GPIO.output(self.R1, GPIO.LOW)
        GPIO.output(self.R2, GPIO.LOW)
        GPIO.output(self.L1, GPIO.LOW)
        GPIO.output(self.L2, GPIO.LOW)
    
    def turn_right(self):
        GPIO.output(self.R1, GPIO.HIGH)
        GPIO.output(self.R2, GPIO.LOW)
        GPIO.output(self.L1, GPIO.LOW)
        GPIO.output(self.L2, GPIO.HIGH)
    
    def turn_left(self):
        GPIO.output(self.R1, GPIO.LOW)
        GPIO.output(self.R2, GPIO.HIGH)
        GPIO.output(self.L1, GPIO.HIGH)
        GPIO.output(self.L2, GPIO.LOW)