#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


HOST = 'localhost'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
def receive():
    while True:
        try:
            message = client_socket.recv(BUFSIZ).decode("utf8")
            message_list.insert(tkinter.END, message)
            message_list.see(tkinter.END)
        except OSError:  
            break

def close(event=None):
    my_message.set("{quit}")
    send()

def send(event=None):  
    message = my_message.get()
    my_message.set("")  
    client_socket.send(bytes(message, "utf8"))
    if message == "{quit}":
        client_socket.close()
        top.quit()

#Main Window
top = tkinter.Tk()
top.title("Chat Program")

#Information Labels
label = tkinter.Label(top, text="Your IP: " + HOST)
label1 = tkinter.Label(top, text = "Port: " + str(PORT))
label2 = tkinter.Label(top, text = "Status: Connected")
label.pack()
label1.pack()
label2.pack()

#Frame to hold message_list and entry_field
messages_frame = tkinter.Frame(top)
my_message = tkinter.StringVar()  
my_message.set("")

#Scrolling Bar
scrollbar = tkinter.Scrollbar(messages_frame)  
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

#Message Display
message_list = tkinter.Listbox(messages_frame, height=50, width=150, yscrollcommand=scrollbar.set)
message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_list.configure(background = 'black', foreground = "white")
message_list.pack()
messages_frame.pack()

#Entry field for message entry
entry_field = tkinter.Entry(top, width = 100, textvariable=my_message)
entry_field.bind("<Return>", send)
entry_field.pack(side=tkinter.LEFT)

#Send
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack(side=tkinter.LEFT)


top.protocol("WM_DELETE_WINDOW", close)




client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  