# Text widget

from tkinter import *

root = Tk()

# 40 znaków długości, 6 wierszy szerokości, jeśli tekst będzie
# undo=True - możliwość Ctrl+Z i Ctrl+Y

textbox = Text (font=('Verdana', 16), height=6, width=40, undo=True)
textbox.insert(END,'To jest jakiś tekst.')
textbox.pack()

from tkinter.scrolledtext import ScrolledText

scrollbox = ScrolledText (font=('Verdana', 16), height=6, width=40, undo=True, bg='blue', fg='white')
scrollbox .insert(END,'To jest jakiś tekst.')
scrollbox.pack()
mainloop()

"""

Polecenie                                 Opis

 textbox.get (1.0, END)                   zwraca zawartość widgetu

 textbox.delete (1.0, END)                usuwa zawartość widgetu

 textbox.insert  (END, 'hello')            dodaje tekst do widgetu

"""
