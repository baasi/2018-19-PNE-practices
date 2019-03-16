import http.server
import socketserver
import termcolor


PORT = 8001


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        if self.path == '/':
            f = open("form1.html", 'r')
            contents = f.read()
            f.close()
        elif '/echo' in self.path:
            message = self.path.split('=')[1]
            contents = """<html><body style="background-color: pink;"><h4>RECIEVED:</h4>"""+ message+ """<br><a href="/">[Main Page]</a><html><body>"""
        else:
            f = open('error.html','r')
            contents = f.read()
            f.close()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return




# Main program

Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)


    httpd.serve_forever()

print("")
print("Stopped")