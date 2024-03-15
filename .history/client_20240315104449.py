import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.socket(socket.AF_INET, socket.SOCK_STREAM), 55555))
