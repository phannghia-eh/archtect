#!/usr/bin/env python
import os
import re
import platform
from time import sleep, perf_counter
from http.server import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import start_http_server, Counter, REGISTRY, Gauge
class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        start = perf_counter()
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes("<b> Hello World !</b>", "utf-8"))
            request_counter.labels(status_code='200', instance=platform.node()).inc()
        else:
            self.send_error(404)
            request_counter.labels(status_code='404', instance=platform.node()).inc()
        request_time = perf_counter() - start
        request_gauge.set(request_time)
        print("Request handle time:", request_time)



if __name__ == '__main__':
    # Start exporter
    start_http_server(9000)
    # Create metrics with 2 labels instance and status_code
    request_counter = Counter('http_requests', 'HTTP request', ["status_code", "instance"])
    request_gauge = Gauge('http_response_time', 'HTTP response time')
    webServer = HTTPServer(("0.0.0.0", 8080), HTTPRequestHandler).serve_forever()
    print("Server started")