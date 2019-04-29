import http.server
import termcolor
import socketserver
from Seq import Seq
import json
import http.client
import requests

PORT = 8000
headers={ "Content-Type" : "application/json"}
SERVER = "https://rest.ensembl.org"
ENDPOINT = ["/info/species?", "/overlap/region/human/{}:{}-{}?feature=gene;feature=transcript;feature=cds;feature=exon", '/info/assembly']
EPORT = 80

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("  Cmd: " + self.command)
        print("  Path: " + self.path)


        contents = ""
        try:
            if self.path == '/':
                with open('index.html', 'r') as f:
                    for i in f:
                        contents += i
                        contents = str(contents)
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html')


            else:
                end = self.path.split("?")[0]
                print ("End =>", end)
                if end == '/listSpecies':
                        contents = self.handle_info_species()
                        self.send_response(200)
                        self.send_header('Content-Type', 'text/html')


                elif end == '/karyotype':
                    contents = self.handle_info_assembly()
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html')


                elif self.path == '/overlap/region/human/{}:{}-{}?feature=gene;feature=transcript;feature=cds;feature=exon':
                    contents = self.handle_overlap_region()
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/plain')

                else:
                    with open('error.html', 'r') as f:
                        for i in f:
                            contents += i
                            contents = str(contents)
                    self.send_response(404)
                    self.send_header('Content-Type', 'text/html')
        except Exception:
            self.send_response(404)
            with open('hugeerror.html', 'r') as f:
                contents = f.read()


        self.send_header("Content-Length", len(str.encode(str(contents))))
        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


    def handle_info_species(self):
        request = SERVER + ENDPOINT[0]
        r = requests.get(request, headers=headers)
        print("Sending request:", request)
        d = r.json()
        print("CONTENT: ")
        print(d)

        contents = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Species List</title></head>' \
                   '<body><h1>List of species</h1><ol>'

        for index in range(len(d['species'])):
            contents += "<li>"
            contents += d['species'][index]['common_name']
            contents += "</li>"

        contents += "</ol></body></html>"

        return contents


    def handle_info_assembly(self):
        #http://rest.ensembl.org/info/assembly/homo_sapiens?
        specie = self.path.split("=")[1]
        specie = specie.replace("+", "_")
        #print("Specie=", specie)
        request = SERVER + ENDPOINT[2] + "/" + specie
        print ("Sending request:", request)

        r = requests.get(request, headers=headers)
        d = r.json()
        print("CONTENT: ")
        print(d)

        contents = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Karyotype of ' + specie + '</title></head>' \
                   '<body><h1>Karyotype of ' + specie + '</h1><ol>'

        for index, elem in enumerate(d['karyotype']):
            contents += "<li>"
            contents += elem #d['karyotype'][index]['common_name']
            contents += "</li>"

        contents += "</ol></body></html>"

        return contents

        return d

    def handle_overlap_region(self):
        print("\nConnecting to server: {}:{}\n".format(SERVER, EPORT))

        # Connect with the server
        con = http.client.HTTPConnection(SERVER, EPORT)

        # Send the request message
        con.request("GET", "/overlap/region/human/{}:{}-{}?feature=gene;feature=transcript;feature=cds;feature=exon")

        # Read the response message from server
        r1 = con.getresponse()

        # Print the status line
        print("Response received: {} {}\n".format(r1.status, r1.reason))

        # Read the response's body
        d = r1.read().decode("utf-8")
        print("CONTENT: ")
        print(d)
        return d



Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stop by the user")
        httpd.server_close()

