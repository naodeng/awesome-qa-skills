#!/usr/bin/env python3
import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def _json(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return

    def do_GET(self):
        if self.path == "/":
            self._json(200, {"ok": True, "service": "local-perf-mock", "path": self.path})
        else:
            self._json(404, {"ok": False, "error": "not_found", "path": self.path})

    def do_POST(self):
        if self.path == "/api/login/":
            length = int(self.headers.get("Content-Length", "0") or "0")
            raw = self.rfile.read(length) if length > 0 else b"{}"
            try:
                req = json.loads(raw.decode("utf-8", errors="ignore") or "{}")
            except Exception:
                req = {}
            self._json(200, {
                "ok": True,
                "token": "mock-token",
                "userTier": req.get("userTier", "UNKNOWN"),
                "skuId": req.get("skuId", "UNKNOWN"),
            })
        else:
            self._json(404, {"ok": False, "error": "not_found", "path": self.path})


def main():
    parser = argparse.ArgumentParser(description="Local mock server for performance skill demos")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=18080)
    args = parser.parse_args()

    server = HTTPServer((args.host, args.port), Handler)
    print(f"local mock server listening on http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
