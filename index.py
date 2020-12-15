import http.server
import socketserver

def run(server_class=http.server.HTTPServer, handler_class=http.server.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    with server_class(server_address, handler_class) as httpd:
        httpd.serve_forever()

run(server_class = socketserver.TCPServer, handler_class = http.server.SimpleHTTPRequestHandler)

