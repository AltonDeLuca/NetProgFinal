#from netprogserver import messaging
from tkinter import *


def Enter_pressed(event):
    user_input = StringVar()
    input_box = Entry(window, text=user_input)
    input_get = input_box.get()
    print(input_get)
    messages.insert(INSERT, '%s\n' % input_get)
    user_input.set('')
    return "break"

def create_gui():

    messages = Text(window)
    messages.pack()

    user_input = StringVar()
    input_box = Entry(window, text=user_input)
    input_box.pack(side=BOTTOM, fill=X)
    
    frame = Frame(window)  # , width=300, height=300)
    input_box.bind("<Return>", Enter_pressed)
    frame.pack()

    window.mainloop()

create_gui()
