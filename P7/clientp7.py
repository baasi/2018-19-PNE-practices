
import http.client
import termcolor
import json
from Seq import Seq
import collections
PORT = 80
SERVER = 'rest.ensembl.org'


print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
con = http.client.HTTPConnection(SERVER, PORT)

# Send the request message
con.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

# Read the response message from server
r1 = con.getresponse()

# Print the status line
print("Response received: {} {}\n".format(r1.status, r1.reason))

# Read the response's body
d = r1.read().decode("utf-8")

print("CONTENT: ")
print(d)
sequence = json.loads(d)
frat1 = Seq(sequence['seq'])

print("this is the sequence: {}".format(frat1.strbases))
print("FRAT1´s length is {}".format(len(frat1.strbases)))
count_T = frat1.counting("T")
print("number of T bases: {}".format(count_T))
popular = collections.Counter(frat1.strbases).most_common(1)[0]

print("most frequent character in the sequence: ", popular[0], "and percentage: {}".format(frat1.percentage(popular[0])))

pa = frat1.percentage("A")
pt = frat1.percentage("T")
pg = frat1.percentage("G")
pc = frat1.percentage("C")
print("percentage of base A :", (pa))
print("percentage of base T : ", (pt))
print("percentage of base G : ", (pg))
print("percentage of base C : ", (pc))

