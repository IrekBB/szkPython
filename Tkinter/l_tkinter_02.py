from tkinter import *

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button= Button(frame, text="QUIT", fg="red", command=master.destroy)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
            print("hi there, everyone!")
root = Tk()
                  
app = App(root)
root.mainloop()
"""
Widget ramki(frame) zapisany jest w zmiennej lokalnej kontruktota __init__
Widgety przycisków zapisane są w zmiennych instancji klasy. Co się zatem
stanie gdy funkcja __init__ zostanie wykonana i zmienna lokalna zostanie
usunięta z zakreu widoczności?
Nie ma tu problemu, ponieważ nie ma potrzeby zachowania referencji do zmiennej
frame. Tkinter automatycznie zachowuje drzewko widgetów, tak że widget nie
zniknie podczas działania aplikacji. Żeby tak się stało musi zostać bezpośrednio
zniszczony (za pomocą metoda destroy). Jeśli jednak chcemy korzystać z referencji
widgetu w dalszej części programu, to lepiej ją zachować.

Bezpieczniej jest oddzielić konstruktor widgetu od metody pack, która jako wartość
zwraca None. Czyli zamiast

Button(frame, text="QUIT", fg="red", command=master.destroy).pack(side=LEFT)

lepiej

self.button= Button(frame, text="QUIT", fg="red", command=master.destroy)
self.button.pack(side=LEFT)

"""
