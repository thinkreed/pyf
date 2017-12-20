import http.server
import os
from socketserver import ThreadingMixIn
from urllib.parse import parse_qs
from urllib.parse import unquote

import requests

from bserver.book_fetcher import BookFetcher


class ThreadBookServer(ThreadingMixIn, http.server.HTTPServer):
    "concurrency book server"


def check_uri(uri, timeout=5):
    try:
        response = requests.request(uri, timeout=timeout)
        return response.status_code == 200
    except requests.RequestException:
        return False


class BookServer(http.server.BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        self.book_fetcher = BookFetcher('http://www.qu.la')
        super().__init__(request, client_address, server)

    def do_GET(self):
        query = unquote(self.path[2:])
        if not query:
            return
        params = parse_qs(query)
        print(params)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write("hha".encode())
        # self.wfile.write(self.book_fetcher.fetch_chapter_content_by_index(params['index'], params['book_name']).encode())


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8168))
    server_address = ('', port)
    httpd = ThreadBookServer(server_address, BookServer)
    httpd.serve_forever()
