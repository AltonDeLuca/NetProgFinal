from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import re as re






def broadcast(message, prefix=""):  
    

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+message)

def accept():
    
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s connected." % client_address)
        client.send(bytes("Enter your name: ", "utf8"))
        addresses[client] = client_address
        Thread(target=handle, args=(client,)).start()

def handle(client): 
    

    name = client.recv(BUFSIZ).decode("utf8")
    welcome =  'type {quit} to quit.'
    client.send(bytes(welcome, "utf8"))
    message = "%s connected" % name
    broadcast(bytes(message, "utf8"))
    clients[client] = name

    while True:
        message = client.recv(BUFSIZ)
        if message != bytes("{quit}", "utf8"):
            broadcast(message, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s disconnected" % name, "utf8"))
            break

clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection")
    ACCEPT_THREAD = Thread(target=accept)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()