from http.server import HTTPServer, CGIHTTPRequestHandler

server_address=("", 8000)
httpd=HTTPServer(server_address, CGIHTTPRequestHandler)
print('HTTP server sterted on localhost:8000')
httpd.serve_forever()

