
from http.server import HTTPServer, SimpleHTTPRequestHandler

class SecureHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'"
        )
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

server = HTTPServer(("localhost", 8000), SecureHandler)

print("Secure test server running on port 8000")
server.serve_forever()
