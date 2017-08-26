import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qs
import json
from Brazo import Brazo

# HTTPRequestHandler class
class BrazoWebController(BaseHTTPRequestHandler):
	def __init__(self, request, client_address, server):
		BaseHTTPRequestHandler.__init__(self, request, client_address, server)

	# GET
	def do_GET(self):
		o = urlparse(self.path)
		print(parse_qs(o.query))
		# Send response status code
		self.send_response(200)

		# Send headers
		self.send_header('Content-type','text/html')
		self.end_headers()

		# Send message back to client
		# message = "Hello world!"
		# if not self.path.startswith("/servo") :
		# 	message = "HELLO world!"
		path = os.path.abspath(os.path.join("ArmControl.html"))
		f = open(path, "rb")
		# Write content as utf-8 data
		self.wfile.write(f.read())
		f.close()
		return

	# POST
	def do_POST(self):
		# Procesar request
		header_cType = self.headers.get('content-type')
		print ("<debug>");
		print (header_cType);
		print ("</debug>");
		if 'application/json' in header_cType:
			length = int(self.headers.get('content-length'))
			data = self.rfile.read(length)
		else:
			data = "{}"
		print ("<debug>");
		print (data);
		print (data.decode("utf8"));
		print ("</debug>")
		jsonData = json.loads(data.decode("utf8"))
		dataResponse = {}
		# Send message back to client
		if self.path.startswith("/servo") :
			dataResponse["mover"] = "servo"
			dataResponse["data"] = jsonData
			self.server.brazo.mover(jsonData['servo'],jsonData['angulo'])
		else:
			dataResponse["message"] = "Hello POST!"
		# Send response status code
		self.send_response(200)
		# Send headers
		self.send_header('Content-type','application/json')
		self.end_headers()
		# Write JSON response as utf-8 data
		self.wfile.write(bytes(json.dumps(dataResponse,indent=4,sort_keys=True), "utf8"))
		return
