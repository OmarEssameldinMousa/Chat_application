import threading
import socket

HOST = socket.gethostbyname(socket.gethostname())

PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
