from server import SocketServer

server = SocketServer('192.168.1.68', 65432)
server.server_manager()