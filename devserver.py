#!/usr/bin/env python3
"""Static dev server for the Plank Norge prototype.

Serves the project with no-store cache headers so the browser always
fetches the latest files (avoids stale CSS/JS during iteration).
"""
import functools
import http.server

PORT = 5500
DIRECTORY = "/Users/lordolivermyrvold/Downloads/planknorge-redesign"


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    handler = functools.partial(NoCacheHandler, directory=DIRECTORY)
    httpd = http.server.ThreadingHTTPServer(("", PORT), handler)
    print(f"Serving {DIRECTORY} on http://localhost:{PORT} (no-cache)")
    httpd.serve_forever()
