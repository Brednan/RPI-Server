import socket
from xxlimited import foo
from motor_hat_controller import MotorControls
import os

class SocketServer():
    def __init__(self, HOST, PORT):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen()
        self.motors_manager = MotorControls()

    #This function waits for a request and returns the content from the request
    def request_listener(self):
        conn, addr = self.server.accept()
        data = conn.recv(2048)

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
                    self.motors_manager.move_forward()
                
                elif content == 'Stop':
                    self.motors_manager.stop_motors()
                
                elif content == 'Right':
                    self.motors_manager.turn_right()
                
                elif content == 'Left':
                    self.motors_manager.turn_left()

                elif content == "Footage":
                    self.send_footage(conn)

    def send_footage(self, conn):
        footage_file = open('./Vision/test-image.PNG', 'rb')
        footage = footage_file.read(2048)

        while footage:
            conn.sendall(footage)
            footage = footage_file.read(2048)
        
        print('done sending')
        footage_file.close()
