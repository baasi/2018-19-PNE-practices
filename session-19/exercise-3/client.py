# Example of getting information stored in github

import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input("Introduce an user name: ")
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

user = json.loads(text_json)

# -- Get some data
print("Name: {}".format(user["name"]))
total_number = user["public_repos"]

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + GITHUB_ID + "/repos", None, headers)
# -- Read the response's body and close
# -- the connection
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()

user1 = json.loads(text_json)
counter = 1
for i in user1:
    print("The repository number {} is: {}".format(counter, i["name"]))
    counter += 1

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + GITHUB_ID + "/repos/{}/2018-19-PNE-practices/commits".format(GITHUB_ID), None, headers)

r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
commit = json.loads(text_json)
print("Commits: {}".format(len(commit)))