#!/usr/bin/python3
"""
Simple API using http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPI(BaseHTTPRequestHandler):
    """
    Custom handler
    """

    def do_GET(self):
        """
        Handle GET requests
        """

        # Route: /
        if self.path == "/":

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"Hello, this is a simple API!"
            )

        # Route: /data
        elif self.path == "/data":

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(
                json.dumps(data).encode()
            )

        # Route: /status
        elif self.path == "/status":

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"OK")

        # Route: /info
        elif self.path == "/info":

            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(
                json.dumps(data).encode()
            )

        # Route: not found
        else:

            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"Endpoint not found"
            )


def run(server_class=HTTPServer,
        handler_class=SimpleAPI):

    server_address = ('', 8000)

    httpd = server_class(
        server_address,
        handler_class
    )

    print("Server running on port 8000...")

    httpd.serve_forever()


if __name__ == "__main__":
    run()
