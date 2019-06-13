from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import requests

class UriShortner(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
