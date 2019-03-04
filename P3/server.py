import socket
from Seq3 import Seq

PORT = 8080
IP = "192.168.1.38"
MAX_OPEN_REQUEST = 5


def process_client(cs):

    # reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    msg = msg.split('\n')

    se = Seq(msg[0])
    response = ""
    ac = "ACTG"


    if msg[0] == "asdf":
        response += "EMPTY"
        cs.send(str.encode(response))

    nmbr = 0
    for n in msg[0].upper():
        if n in ac:
            nmbr += 1
    if nmbr == len(msg[0]):
        response += "OK!"
        response += "\n"
    elif nmbr != len(msg[0]):
        response += "ERROR"
        cs.send(str.encode(response))



    for i in msg[1:]:
        if i == 'len':
            response += se.len()
        elif i == 'complement':
                response += se.complement().strbases

        elif i == 'reverse':
            response += se.reversed().strbases

        elif i == 'countA':
            response += se.counting('A')

        elif i == 'countC':
            response += se.counting('C')

        elif i == 'countT':
            response += se.counting('T')

        elif i == 'countG':
            response += se.counting('G')

        elif i == 'percA':
            response += se.percentage('A')

        elif i == 'percC':
            response += se.percentage('C')

        elif i == 'percT':
            response += se.percentage('T')

        elif i == 'percG':
            response += se.percentage('G')


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