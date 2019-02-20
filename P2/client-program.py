# We are programing our first client
import socket
from Seq2 import Seq

while True:
# We create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket created")

    PORT = 8080
    IP = "192.168.1.38"


    file = input("Type a message: ")
    seq = Seq(file)
    rev = Seq.reversed(seq)
    comp = Seq.complement(rev)
    comp1 = comp.strbases

    s.connect((IP ,PORT))

    s.send(str.encode(comp1))

    msg = s.recv(2048).decode('utf-8')

    s.close()

