import socket
from motor_controls import MotorControls

class SocketServer(MotorControls):
    def __init__(self, HOST, PORT):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen()
        super().__init__()

    def request_listener(self):
        conn, addr = self.server.accept()
        data = conn.recv(1024)

        if not data:
            return None
        
        return data, conn
    
    #This function sends a response back to the client 
    def send_response(self, conn, content):
        conn.sendall(content)
    
    def server_manager(self):
        while True:
            data, conn = self.request_listener()
            if data:
                content = data.decode()
                if content == 'Forward':
                    self.move_forward()
