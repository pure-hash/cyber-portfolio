from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os
from datetime import datetime

LOG_DIR = "logs"
HTML_FILE = "index.html"

# Make sure logs exist
os.makedirs(LOG_DIR, exist_ok=True)

def log_event(message):
    """Append messages to honeypot.log."""
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(os.path.join(LOG_DIR, "honeypot.log"), "a") as f:
        f.write(f"[{timestamp}] {message}\n")

class CorporateLoginHoneypot(BaseHTTPRequestHandler):

    def serve_html(self):
        """Send the fake login page."""
        try:
            with open(HTML_FILE, "r") as f:
                html = f.read()
        except FileNotFoundError:
            html = "<h1>ERROR: index.html missing</h1>"

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def log_get(self):
        ip = self.client_address[0]
        agent = self.headers.get("User-Agent", "Unknown")
        path = self.path

        log_event(f"GET request from {ip} | Agent: {agent} | Path: {path}")

    def log_post(self, username, password):
        ip = self.client_address[0]
        agent = self.headers.get("User-Agent", "Unknown")

        log_event(
            f"POST attempt from {ip} | username='{username}' password='{password}' | Agent: {agent}"
        )

    def do_GET(self):
        self.log_get()
        self.serve_html()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(length).decode()

        fields = urllib.parse.parse_qs(post_data)

        username = fields.get("username", [""])[0]
        password = fields.get("password", [""])[0]

        self.log_post(username, password)

        # Re-serve login page (looks like “incorrect credentials”)
        self.serve_html()

def run():
    server = HTTPServer(("0.0.0.0", 8080), CorporateLoginHoneypot)
    print("🚨 Corporate Login Honeypot active on port 8080…")
    server.serve_forever()

if __name__ == "__main__":
    run()
