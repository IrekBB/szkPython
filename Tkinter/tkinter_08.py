# frame - zadaniem ramki jest przechowywanie innych widgetów (kontener)
# w naszym przykładzie stworzymy ramkę do przechowywania przycisków,
# program analogiczny do napisanego wcześniej - przyciski alfabetu,
# z wykorzystanie ramki.

from tkinter import *



alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
root = Tk()

button_frame = Frame()
buttons = [0] * 26
for i in range(26):
    #i-ty przycisk ma rodzica button_frame, czyli należy do ramki
    buttons[i] = Button(button_frame, text=alphabet[i])
    buttons[i].grid(row=0,column=i)

ok_button = Button (text='Ok', font = ('Verdana', 24))

button_frame.grid (row = 0, column =0)
ok_button.grid(row=1, column = 0)

mainloop()
