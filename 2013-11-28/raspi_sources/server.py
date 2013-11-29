#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import x_parser
import message_parser

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    def respond(self, code, content):
        self.send_response(code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(content)

    #Handler for the GET requests
    def do_GET(self):
        self.respond(200, "Hello there")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            if self.path == '/message':
                if len(post_data) > 140:
                    raise Exception('Message is too long (max 140 chars allowed)')
                pattern = message_parser.parse(post_data)
            else:
                x_parser.parse(post_data)
                pattern = post_data

            f = open('pattern', 'w')
            f.write(pattern)
            f.close()
            self.respond(200, "OK")
        except Exception as e:
            self.respond(400, "Not OK: " + e.message)

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
