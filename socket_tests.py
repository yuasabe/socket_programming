from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 9000))
s.listen(5)
while True:
  c,a = s.accept()
  print(f"Received connection from {a}")
  c.send(f"Hello {a[0]}\n".encode())
  c.close()