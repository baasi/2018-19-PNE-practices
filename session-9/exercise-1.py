import socket
import termcolor
import sys

PORT = 8080
IP = "212.128.253.90"
MAX_OPEN_REQUEST = 5


def process_client(cs):

    # reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("message from the client: {}".format(termcolor.cprint(msg, "blue")))

    if msg == "EXIT":
        sys.exit()
    else:
        pass

    # Sending the message back to the client
    # because we are an eco server
    cs.send(str.encode(msg))

    cs.close()

# We create a socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # ...procress the client request
    print("Attending client: {}".format(address))

    process_client(clientsocket)

    # ...Close the socket
    clientsocket.close()







