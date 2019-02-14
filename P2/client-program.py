# We are programing our first client

from Seq import sequence

import socket

while True:
# We create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket created")

    PORT = 8080
    IP = "212.128.253.90" #My IP

    file = input("Type a message: ")
    rev = file.reversed(file)
    comp = file.complement(rev)

# Connect to the server
    s.connect((IP ,PORT))

    s.send(str.encode(comp))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM SERVER")
    print(msg)

    s.close()

    print("the end")
