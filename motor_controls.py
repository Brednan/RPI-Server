from adafruit_motorkit import MotorKit


class MotorControls():
    def __init__(self):
        self.motors = MotorKit()
    
    def move_forward(self):
        self.motors.motor1.throttle(1.0)