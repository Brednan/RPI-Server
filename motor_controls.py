from adafruit_motorkit import MotorKit


class MotorControls():
    def __init__(self):
        self.motors = MotorKit()
    
    def move_forward(self):
        self.motors.motor1.throttle = 0.5
        self.motors.motor2.throttle = 0.5

    def stop_motors(self):
        self.motors.motor1.throttle = 0.0
        self.motors.motor2.throttle = 0.0
    
    def move_backward(self):
        self.motors.motor1.throttle = -0.5
        self.motors.motor2.throttle = -0.5
    
    def turn_right(self):
        self.motors.motor1.throttle = -0.5
        self.motors.motor2.throttle = 0.5
    
    def turn_left(self):
        self.motors.motor1.throttle = 0.5
        self.motors.motor2.throttle = -0.5