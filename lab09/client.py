#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

HOST = '10.3.141.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected to 10.3.141.1:8000")
while True:
    outdata = input('please input message: ')
    print('send:' + outdata)
    s.send(outdata.encode())
    
    indata = s.recv(1024)
    if outdata =='EXIT': # connection closed
        s.close()
        print('Closed connection.')
        break
    print(indata.decode())
