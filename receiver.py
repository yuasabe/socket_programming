#!/usr/bin/env python

import socket

UDP_IP = ""
UDP_PORT = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Listening...")

while True:
	data, addr = sock.recvfrom(1024)
	print("received message from ", addr)
	print("data: ", data[1:].decode("utf-8"))
	print("len: ", int.from_bytes(data[:1], byteorder='big', signed=False))

