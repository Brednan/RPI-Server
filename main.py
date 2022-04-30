# from server import SocketServer
from motor_controls import MotorControls

# server = SocketServer('192.168.1.68', 65432)
# server.server_manager()

motors = MotorControls()
motors.motor1.throttle(1.0) 
