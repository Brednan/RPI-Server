from server import SocketServer

server = SocketServer('192.168.1.102', 65432)
server.server_manager()
