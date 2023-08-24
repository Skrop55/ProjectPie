import socket

s = socket.socket
port = 56789
s.connect(('ip', port))  # change ip to your internal ip... cuz I'm not gonna give you mine
print(s.recv(1024))
s.close()
