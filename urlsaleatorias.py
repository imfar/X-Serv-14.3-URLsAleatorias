#!/usr/bin/python3

# Aplicacion web generadora de URLs aleatorias

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    num = random.randint(12312312, 83242387)  # rango de numeros aleatorios
    url = "'http://localhost:1234/" + str(num) + "'"
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                    b"<html><body><h1>Hola. " +
                    b"<a href=" + bytes(url, 'utf-8') +
                    b">Dame otra</a>" +
                    b"</h1></body></html>" +
                    b"\r\n")
    recvSocket.close()
