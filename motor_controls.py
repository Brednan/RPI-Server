from adafruit_motorkit import MotorKit


class MotorControls(MotorKit):
    def __init__(self):
        super().__init__()
    
    def move_forward(self):
        self.motor1.throttle(1.0)