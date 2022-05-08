from adafruit_motorkit import MotorKit

class MotorControls(MotorKit):
    def __init__(self):
        super().__init__()
    
    def move_forward(self):
        super().motor1.throttle = 1.0
        super().motor2.throttle = 1.0
        super().motor3.throttle = 1.0
        super().motor4.throttle = 1.0
    
    def stop_motors(self):
        super().motor1.throttle = 0.0
        super().motor2.throttle = 0.0
        super().motor3.throttle = 0.0
        super().motor4.throttle = 0.0
    
    def turn_right(self):
        super().motor1.throttle = 1.0
        super().motor2.throttle = -1.0
        super().motor3.throttle = 1.0
        super().motor4.throttle = -1.0
    
    def turn_left(self):
        super().motor1.throttle = -1.0
        super().motor1.throttle = 1.0
        super().motor3.throttle = -1.0
        super().motor4.throttle = 1.0
