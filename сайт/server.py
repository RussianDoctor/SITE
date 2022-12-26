from http.server import HTTPServer, CGIHTTPRequestHandler
server_date = ("localhost", 8080)
server = HTTPServer(server_date, CGIHTTPRequestHandler)
server.serve_forever()