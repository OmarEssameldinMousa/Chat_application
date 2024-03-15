import socket
import threading

nickname = input("choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.socket(socket.AF_INET, socket.SOCK_STREAM), 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("AN error occurred!")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


print(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
# receive_thread = threading.Thread(target=receive)
# receive_thread.start()

# write_thread = threading.Thread(target=write)
# write_thread.start()
