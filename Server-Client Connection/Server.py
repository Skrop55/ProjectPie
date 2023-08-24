import socket

s = socket.socket()
print("Socket connected! ")
port = 56789
s.bind(('', port))
print(f'socket bound to port{port}')
s.listen(1)
print('Socket is listening')

while True:
    c, addr = s.accept()
    print("got connection from", addr)
    message = 'Thank you for connecting'
    c.send(message.encode())
    c.close()

