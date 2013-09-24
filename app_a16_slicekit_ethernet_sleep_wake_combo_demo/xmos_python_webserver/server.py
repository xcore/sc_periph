#!/usr/bin/python
import socket
  
server_port = 501
self_ip = socket.gethostbyname(socket.gethostname())
print('Web Server Address = %s' % self_ip)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((self_ip, server_port))
server_sock.listen(1)

while True:

  conn, client_address = server_sock.accept()
  
  while True:
    data = conn.recv(1024).decode()  
    if data:
      print('XMOS: %s' % data)
    else:
      print('Connection closed')
      conn.close()
      break
