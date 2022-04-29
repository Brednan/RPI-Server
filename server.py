import socket
from adafruit_motorkit import MotorKit

class SocketServer:
    def __init__(self, HOST, PORT):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen()
    
    def request_listener(self):
        conn, addr = self.server.accept()
        data = conn.recv(1024)
        
        if not data:
            return None
        
        return data, conn

    