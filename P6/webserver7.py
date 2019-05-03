import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        global seq, op
        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            with open("main.html", "r") as f:
                info = f.read()
            resp = 200

        elif self.path[:4] == '/get':
            resp = 200
            msg = self.path.split('&')
            seqq = msg[0].split('=')[1]
            seqq = seqq.upper()
            if seqq.upper().strip('ACGT') == '':

                seqq = Seq(seqq)

                counting = {'base=A': ('Count A: ' + str(seqq.counting('A'))),
                         'base=C': ('Count C: ' + str(seqq.counting('C'))),
                         'base=G': ('Count G: ' + str(seqq.counting('G'))),
                         'base=T': ('Count T: ' + str(seqq.counting('T')))}
                percentage = {'base=A': ('Percentage A: ' + str(seqq.percentage('A')) + '%'),
                        'base=C': ('Percentage C: ' + str(seqq.percentage('C')) + '%'),
                        'base=T': ('Percentage T: ' + str(seqq.percentage('T')) + '%'),
                        'base=G': ('Percentage G: ' + str(seqq.percentage('G')) + '%')}

                result = {'count': counting, 'perc': percentage}

                if len(msg) == 3:
                    seq = ''
                    operation = msg[2].split('=')[1]
                    bases = msg[1]

                    if bases in result[operation].keys():
                        op = result[operation][bases]

                elif len(msg) == 4:
                    seq = 'Length: ' + str(seqq.len())
                    operation = msg[3].split('=')[1]
                    bases = msg[2]

                    if bases in result[operation].keys():
                        op = result[operation][bases]

                with open('response.html', 'w') as f:
                    data = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>RESPONSE</title></head><body><h1>results page:</h1><p>{}</p><p>len</p><p>op</p><a href="/">[Main Page]</a></body></html>"""
                    print(op)
                    data = data.replace("{}", seqq.strbases.upper()).replace("len", seq).replace("op", op)
                    f.write(data)
                    f.close()
                    with open('response.html', 'r') as f:
                        info = f.read()
            else:
                with open('sequenceerror.html', 'r') as f:
                    info = f.read()

        else:
            resp = 404
            with open("error.html", "r") as f:
                info = f.read()

        self.send_response(resp)

        self.send_header('Content-Type', 'text/html')

        self.send_header('Content-Length', len(str.encode(info)))

        self.end_headers()

        self.wfile.write(str.encode(info))
        return


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server stopped")