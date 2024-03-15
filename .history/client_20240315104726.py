import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.socket(socket.AF_INET, socket.SOCK_STREAM), 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                pass
            else:
                print(message)
        except:
            print("AN error occurred!")
            client.close()
            break
