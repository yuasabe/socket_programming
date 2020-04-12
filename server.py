#!/usr/bin/env python

import dpkt
import socket

UDP_IP = ""
UDP_PORT = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Listening...")

while True:
	data, addr = sock.recvfrom(1024)

	len_message = int.from_bytes(data[:1], byteorder='big', signed=False)
	message = data[1:len_message+1].decode()
	name = data[len_message+1:].decode()

	if message == "join":
			print(f"{addr[0]}:{addr[1]} :: {name} joined the chat.")
	else:
		print(f"{addr[0]}:{addr[1]} :: {name}: {message} ({len_message})")