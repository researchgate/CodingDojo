#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import parser

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

	def respond(self, code, content):
		self.send_response(code)
		self.send_header('Content-type','text/plain')
		self.end_headers()
		self.wfile.write(content)
	
	#Handler for the GET requests
	def do_GET(self):
		self.respond(200, "Hello there")

	def do_POST(self):	
	        content_length = int(self.headers['Content-Length'])
        	post_data = self.rfile.read(content_length)
		try:
			parser.parse(post_data)
		        f = open('pattern', 'w')
			f.write(post_data)
			f.close()
			self.respond(200, "OK")
		except Exception as e:
			self.respond(400, "Not OK: " + e.message)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
