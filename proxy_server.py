import http.server
import socketserver
import requests
import urllib.parse

def check_file_value(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_url.query)

        name_value = query.get("name", [None])[0]

        if name_value:
            with open("search_query.txt", "w") as file:
                file.write(name_value)

            file_value = check_file_value("machine_learning_output.txt")

            if file_value == "1":
                self.send_response(403)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Access Denied")
                return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response = requests.get("http://localhost:8080" + self.path)
        self.wfile.write(response.content)

if __name__ == "__main__":
    PORT = 8000
    Handler = CustomHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving on port", PORT)
        httpd.serve_forever()
