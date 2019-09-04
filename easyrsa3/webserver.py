from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import ssl

# config
port = 5000
web_dir = 'html'

# change to web_dir
web_dir = os.path.join(os.path.dirname(__file__), web_dir)
os.chdir(web_dir)

httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile='../pki/private/localhost.key',
    certfile='../pki/issued/localhost.crt',
    server_side=True
)
httpd.serve_forever()
