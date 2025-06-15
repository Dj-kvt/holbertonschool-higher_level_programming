from http.server import BaseHTTPRequestHandler, HTTPServer
import json
"""Désole pour mes commzntaires en français."""


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Gérer les différentes URL demandées
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(status_data).encode())

        else:
            # Endpoint non trouvé
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found: Endpoint not found.")


# Démarrer le serveur
def run():
    server_address = ('', 8000)  # écoute sur le port 8000
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on http://localhost:8000...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
