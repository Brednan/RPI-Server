from server import SocketServer

server = SocketServer('192.168.1.68', 65432)

while True:
    data, conn = server.request_listener()
    content = data.decode()

    if data != None:
        if content == 'Forward':
            server.send_response(conn, content)