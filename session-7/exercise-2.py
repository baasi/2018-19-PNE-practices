# We are programing our first client

import socket

# We create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 8080
IP = "212.128.253.64"

while True:
    file = input("Type a message: ")
# Connect to the server
    s.connect((IP,PORT))

    s.send(str.encode(file))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM SERVER")
    print(msg)

    print("the end")
