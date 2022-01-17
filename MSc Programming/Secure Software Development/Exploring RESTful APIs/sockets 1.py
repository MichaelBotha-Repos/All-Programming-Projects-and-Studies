"""
    Below is a program which connects to an HTTP server and requests the
    root page
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 5000))
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes("127.0.0.1", "utf8") +
          b"\r\nConnection: close\r\n\r\n")

reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply))
