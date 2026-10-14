"""Minimal HTTP Health and Telemetry service for CI/CD demonstration."""

import json
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler


def get_system_health() -> dict:
    """Returns application health payload."""
    return {
        "status": "HEALTHY",
        "service": "ci-template-service",
        "version": "1.0.0",
        "environment": os.getenv("APP_ENV", "development"),
        "python_version": sys.version.split()[0]
    }


class HealthRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            payload = json.dumps(get_system_health())
            self.wfile.write(payload.encode("utf-8"))
        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"CI/CD Template Service Active. Check /health for status.")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Override to suppress excessive stdout logs during tests
        pass


def run_server(port: int = 8080):
    server = HTTPServer(("0.0.0.0", port), HealthRequestHandler)
    print(f"Service listening on port {port}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down service.")
        server.server_close()


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    run_server(port=port)
