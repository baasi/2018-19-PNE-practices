import http.server
import socketserver

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("  Cmd: " + self.command)
        print("  Path: " + self.path)

        content = ''
        if request == '/':
            with open('index.html', 'r') as file:
                for line in file:
                    content += line
                    content = str(content)
        elif request == '/blue':
            with open('blue.html', 'r') as file:
                for line in file:
                    content += line
                    content = str(content)
        elif request == '/pink':
            with open('pink.html', 'r') as file:
                for line in file:
                    content += line
                    content = str(content)
        else:
            with open('error.html', 'r') as file:
                for line in file:
                    content += line
                    content = str(content)

        status_line = "HTTP/1.1 200 ok\r\n"

        header = "Content-Type: text/html\r\n"
        header += "Content-Length: {}\r\n".format(len(str.encode(content)))

        response_msg = status_line + header + "\r\n" + content

        cs.send(str.encode(response_msg))

    else:
        print("Your request is empty ):")
    # Close the socket
    cs.close()

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header("Content-Length", len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()