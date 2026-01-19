# Updating
"""
Tkinter uaktualnia (odświeża) ekran tak szybko jak jest to możliwe, czasami to jednak
nie wystarczy. Na przykład jeśli z przyciskiem związana jest jakaś funkcja
i naciśnięcie przycisku ją uruchomi, to odświeżenie ekranu nąstąpi dopiero po jej wykonaniu.
Jesli w ciele funkcji znajduje się kod, który zmienia coś na ekranie to pojawi się pewne
opóźnienie w realizacji zadania (pauza). Jesli chcemy tego uniknąć, wywołujemy metodę
update:
                                   root.update()
dla całego ekranu, lub przykładowo
                                   canvas.update()    
dla wybranego widgetu.
"""


# Metoda after()
"""
Pozwiązanym zagadnienem jest metoda after().
Przypuśćmy, że chcemy skorzystać z timera aby po jakimś określonym czasie wyzwolić
jakąś akcję. Korzystamy wówczas z metody after. Jej pierwszy argument to czas podawany
w milisekundach po którym nastąpi odświeżenie ekranu, drugi - to funkcja która ma zostać
wywołana.
"""

from time import time
from tkinter import *

def update_timer():
    time_left = int (90-(time()-start))
    minutes = time_left // 60
    seconds = time_left % 60
    time_label.configure(text='{}:{:02d}'.format(minutes, seconds))
    root.after(100, update_timer)

root = Tk()
time_label = Label()
time_label.grid(row=0, column=0)

start=time()
update_timer()

mainloop()


