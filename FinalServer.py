
# Python program to implement server side of chat room. 
import socket 
import select 
from _thread import *
  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  

IP_address = ""
  

Port = 12345
  
server.bind((IP_address, Port)) 

server.listen(10) 

def remove(connection): 
    if connection in clients: 
        clients.remove(connection) 
  
clients = [] 
def broadcast(message, connection): 
    #sends message to all clients not the sender
    for client in clients: 
        if client!=connection: 
            try: 
                client.send(message) 
            except: 
                client.close()

def threadClient(conn, addr): 
    #accepts message and broadcasts
    while True: 
            message = conn.recv(2048) 
            if message: 

                print(message )
  

                message_to_send = "<" + addr[0] + "> " + message 
                broadcast(message_to_send, conn) 
            else:                  
                    remove(conn) 
  
        
while True: 
    #accept clients, add to list, start new thread
    connection, address = server.accept() 
    clients.append(connection) 
    start_new_thread(threadClient,(connection,address))     
  
connection.close() 
server.close() 