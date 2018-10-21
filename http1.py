# coding:utf-8

import socket

host = ''
port = 2001
server = socket.socket()

server.bind((host, port))

while True:
    server.listen(5)
    connection,addr = server.accept()
    request_size = 1024
    request_str = ''
    while True:
        request_str += connection.recv(request_size)
        if len(connection.recv(request_size)) < 1024:
            break

    print('request:{}'.format(request_str.decode('utf-8')))

    reponse_str = b'<h1>Hello,zppc welcome you!</h1>'
    connection.sendall(reponse_str)
    connection.close()
