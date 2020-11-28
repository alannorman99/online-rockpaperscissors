import socket
from _thread import *
import sys

server = "192.168.1.9"
port = 5555

# create initial server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# how many connections are allowed
s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(connection):
    reply = ""
    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print("DISCONNECTED")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            connection.sendall(str.encode(reply))
        except:
            break


while True:
    # accept any incoming connections
    conn, addr = s.accept()
    print("Connected to: ", addr)

    # allows the thread_client function to run in the background
    start_new_thread(threaded_client, (conn,))
