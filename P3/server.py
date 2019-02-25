import socket
from Seq import Seq

PORT = 8080
IP = "192.168.1.38"
MAX_OPEN_REQUEST = 5


def operate(se, op):
    print('Perfoming the following operation: ', op)
    se = msg[0]
    op = msg[1]
    if op == 'len':
        return se.length()
    elif op == 'complement':
        return se.complement()

    elif op == 'reverse':
        return se.reversed()

    elif op == 'countA':
        return se.counting('A')

    elif op == 'countC':
        return se.counting('C')

    elif op == 'countT':
        return se.counting('T')

    elif op == 'countG':
        return se.counting('G')

    elif op == 'percA':
        return se.percentage('A')

    elif op == 'percC':
        return se.percentage('C')

    elif op == 'percT':
        return se.percentage('T')

    elif op == 'percG':
        return se.percentage('G')
    else:
        print("there was an error, not valid operation")


def process_client(cs):

    # reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    if msg == "":
        response = "ALIVE"
    else:
        if len(set(se)) == 4:
            response = "OK"
        elif len(set(se)) != 4:
            response = "Error, not valid sequence"


    # Sending the message back to the client
    # because we are an eco server
    cs.send(str.encode(response))

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