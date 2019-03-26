# Example of getting information stored in github

import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = ["/jokes/count", "/categories", "/jokes/random"]
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standard one
# -- will be used
for i in ENDPOINT:

    conn = http.client.HTTPConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Optionally you can print the
    # -- received json file for testing
    # print(text_json)

    # -- Generate the object from the json file
    user = json.loads(text_json)

    # -- Get some data
    number = user['value']


    print()
    print("number: {}".format(number))
