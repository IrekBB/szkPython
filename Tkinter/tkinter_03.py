# Buttons
"""
Prosty przycisk:
ok_button = Button(text='Ok')

Argument command pozwala dodać akcję do przycisku (tzw. callback function).


"""
 
from tkinter import *

def callback():
    label.configure(text='Button clicked')

root = Tk()
label = Label (text='Not clicked')
button = Button(text='Click me', command = callback)

label.grid (row =0, column = 0)
button.grid(row=1, column=0)

mainloop()
