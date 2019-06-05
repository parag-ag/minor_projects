from http.server import HTTPServer,BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)

		self.send_header('content-tyoe','text/plain; cahrset=utf-8')
		self.end_headers()

		self.wfile.write("Helllllllloooooooooooo".encode())

if __name__ == '__main__':
	server = ('',8000)
	httpd = HTTPServer(server,Handler)
	httpd.serve_forever()