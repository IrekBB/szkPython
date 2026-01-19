# Pozbywanie się widgetów
"""
metoda destroy:

     button.destroy() # usuwanie przycisku
     root.destroy()   # usuwanie okna głównego
     
"""

# Blokowanie automatycznego zamykania okna

from tkinter import *
from tkinter.messagebox import askquestion

def quitter_function():
    answer = askquestion(title='Quit?', message='Really quit?')
    if answer == 'yes':
        root.destroy()

root = Tk()
# próba zamknięcia okna głównego
root.protocol('WM_DELETE_WINDOW',quitter_function)
mainloop()
