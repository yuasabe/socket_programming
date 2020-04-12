#!/usr/bin/env python

import dpkt
import socket
import sys

# UDP_IP = "203.178.135.26"
UDP_IPs = ["127.0.0.1", "192.168.0.116", "yuasabe.hongo.wide.ad.jp"]
# UDP_IP = "<broadcast>"
UDP_PORT = 1024

# f = open("message_test.dat", "wb")

# while True:
# 	name = input("username: ")
# 	if name != "":
# 		break

# print(f"Welcome {name}!")
# join_message = bytes("join", "utf-8")
# join_message_len = bytes([len(join_message)])
# join_message_name = bytes(name, "utf-8")
# byte_join_message = join_message_len + join_message + join_message_name

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# sock.sendto(byte_join_message, (UDP_IP, UDP_PORT))

while True:
	message = str(input(">>> "))
	if message == '/exit':
		print('Exiting.')
		sys.exit()
	DATA = bytes(message + '\n', "utf-8")
	if len(DATA) > 255:
		print("Too long. Try again.")
		continue
	LEN = bytes([len(DATA)])
	byte_message = LEN + DATA

	for UDP_IP in UDP_IPs:
		sock.sendto(byte_message, (UDP_IP, UDP_PORT))

	# data, addr = sock.recvfrom(1024)

	# len_message = int.from_bytes(data[:1], byteorder='big', signed=False)
	# message = data[1:len_message+1].decode()
	# name = data[len_message+1:].decode()

	# if message == "join":
	# 		print(f"{addr[0]}:{addr[1]} :: {name} joined the chat.")
	# else:
	# 	print(f"{addr[0]}:{addr[1]} :: {name}: {message} ({len_message})")




