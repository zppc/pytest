# coding:utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 2001

s.connect((host, port))

http_request = 'GET / HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)
request_str = http_request.encode('utf-8')
s.send(request_str)
ip, post = s.getsockname()
print("ip{},address{}".format(ip, post))
read_size = 1024
reponse_rev = ''
while True:
    reponse_rev += s.recv(read_size)
    if len(s.recv(read_size)) < 1024:
        break;
s.close()
reponse_str = reponse_rev.decode('utf-8')

print(request_str)
