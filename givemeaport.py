#!/usr/bin/env python
import socket
import sys

start = 8000
end = 10000

for port in range(start, end):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    if not result == 0:
        print port
        sys.exit(0)

