__author__ = 'z00152000'

PORT = 8000
HOST = "127.0.0.1"
import http.server
import socketserver


Handler = http.server.CGIHTTPRequestHandler

httpd = http.server.HTTPServer((HOST, PORT), Handler)

print("CGI serving at port: ", PORT)

httpd.serve_forever()
