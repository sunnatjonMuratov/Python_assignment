import http.server
import socketserver
import urllib.parse
import json
import os

PORT = 8001
DATA_FILE = 'reservations.json'

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        reservations = json.load(f)
else:
    reservations = []


class ReservationHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = urllib.parse.parse_qs(post_data)

        reservation = {
            'name': parsed_data['name'][0],
            'email': parsed_data['email'][0],
            'phone': parsed_data['phone'][0],
            'date': parsed_data['date'][0],
            'time': parsed_data['time'][0],
            'guests': parsed_data['guests'][0],
        }

        reservations.append(reservation)

        with open(DATA_FILE, 'w') as f:
            json.dump(reservations, f)

        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def serve_reservations(self):
        with open('index.html', 'r') as f:
            html = f.read()

        reservation_rows = ''
        for reservation in reservations:
            row = f"""
            <tr>
                <td>{reservation['name']}</td>
                <td>{reservation['email']}</td>
                <td>{reservation['phone']}</td>
                <td>{reservation['date']}</td>
                <td>{reservation['time']}</td>
                <td>{reservation['guests']}</td>
            </tr>
            """
            reservation_rows += row

        html = html.replace('{{ reservations }}', reservation_rows)

        self.wfile.write(html.encode('utf-8'))

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.serve_reservations()
        else:
            super().do_GET()


# Start the server
with socketserver.TCPServer(("", PORT), ReservationHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
