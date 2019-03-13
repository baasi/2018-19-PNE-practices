import http.server
import socketserver


PORT = 8000
MAX_OPEN_REQUESTS = 5

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
        elif self.path == '/blue':
            with open('blue.html', 'r') as f:
                for i in f:
                    contents += i
                    contents = str(contents)
        elif self.path == '/pink':
            with open('pink.html', 'r') as f:
                for i in f:
                    contents += i
                    contents = str(contents)
        else:
            with open('error.html', 'r') as f:
                for i in f:
                    contents += i
                    contents = str(contents)

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header("Content-Length", len(str.encode(contents)))
        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()

