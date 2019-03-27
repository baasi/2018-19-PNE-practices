# Example of getting information stored in github

import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/count"
ENDPOINT2 = "/categories"
ENDPOINT3 = "/jokes/random/"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {"User-Agent": 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn1 = http.client.HTTPConnection(HOSTNAME)
conn2 = http.client.HTTPConnection(HOSTNAME)
conn3 = http.client.HTTPConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn1.request(METHOD, ENDPOINT, None, headers)
conn2.request(METHOD, ENDPOINT2, None, headers)
conn3.request(METHOD, ENDPOINT3, None, headers)

# -- Wait for the server's response
r1 = conn1.getresponse()
r2 = conn2.getresponse()
r3 = conn3.getresponse()

# -- Read the response's body and close
# -- the connection
text_json1 = r1.read().decode("utf-8")
conn1.close()
text_json2 = r2.read().decode("utf-8")
conn2.close()
text_json3 = r3.read().decode("utf-8")
conn3.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
count = json.loads(text_json1)
categories = json.loads(text_json2)
random_joke = json.loads(text_json3)

# -- Get some data
print("Count:", count['value'])
print("Categories:", categories['value'])
print("Random joke:", random_joke['value']['joke'])
