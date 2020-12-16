import http.server
import socketserver

PORT = 8000

def run(server_class=http.server.HTTPServer, handler_class=http.server.BaseHTTPRequestHandler):
    server_address = ('', PORT)
    with server_class(server_address, handler_class) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

run(server_class = socketserver.TCPServer, handler_class = http.server.SimpleHTTPRequestHandler)

