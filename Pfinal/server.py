import http.server
import termcolor
import socketserver
from Seq import Seq

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
        if self.path == '/':
            with open('index.html', 'r') as f:
                for i in f:
                    contents += i
                    contents = str(contents)
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')

        elif self.path == '/info/species':
            contents = self.handle_info_species()
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')


        elif self.path == '/info/assembly':
            contents = contents
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')


        elif self.path == '/overlap/region/human/{}:{}-{}?feature=gene;feature=transcript;feature=cds;feature=exon':
            contents = contents

        else:
            with open('error.html', 'r') as f:
                for i in f:
                    contents += i
                    contents = str(contents)
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')


        self.send_header("Content-Length", len(str.encode(contents)))
        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


    def handle_info_species(self):
        print("\nConnecting to server: {}:{}\n".format(SERVER, EPORT))

        # Connect with the server
        con = http.client.HTTPConnection(SERVER, EPORT)

        # Send the request message
        con.request("GET", "/info/species")

        # Read the response message from server
        r1 = con.getresponse()

        # Print the status line
        print("Response received: {} {}\n".format(r1.status, r1.reason))

        # Read the response's body
        d = r1.read().decode("utf-8")
        print("CONTENT: ")
        print(d)
        return d


    def handle_info_assembly(self)
        print("\nConnecting to server: {}:{}\n".format(SERVER, EPORT))

        # Connect with the server
        con = http.client.HTTPConnection(SERVER, EPORT)

        # Send the request message
        con.request("GET", "/info/assembly")

        # Read the response message from server
        r1 = con.getresponse()

        # Print the status line
        print("Response received: {} {}\n".format(r1.status, r1.reason))

        # Read the response's body
        d = r1.read().decode("utf-8")
        print("CONTENT: ")
        print(d)
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

