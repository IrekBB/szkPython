# GUI Events
"""
zdarzeniem może być naciśnięcie klawisza, przeciąganie obiektu po kanwie,
ruch kółka myszki itd.

Zdarzenie                    Opis
<Button-1>                    nacisnięty lewy przycisk myszy
<Double-Button-1>             Podwójne kliknięcie na lewym przycisku myszy
<Button-Release-1>            Zwolnienie lewego przycisku myszy
<B1-Motion>                   Przeciąganie lewym przyciskiem myszy
<MouseWheel>                  Poruszanie kółkiem myszy
<Motion>                      Ruch myszy
<Enter>                       Mysz jest nad widgetem
<Leave>                       Mysz opuściła obszar widgetu
<Key>                         Naciśnięto klawisz
<key name>                    nacisnięto klawisz key name

Atrybuty (najczęściej używane) obiektu Event

Atrybut                      Opis
keysym                       nazwa nacisnietego klawisza
x,y                          współrzędne wskaźnika myszy
delta                        wartość kółka myszy

"""

# Key events

"""
# Program 1
from tkinter import *

def callback(event):
    print (event.keysym)

root = Tk()
root.bind('<Key>',callback)

mainloop()
"""

"""
# Program 2
from tkinter import *

def callback1(event):
    print ('You pressed the enter key.')

def callback2 (event):
    print ('You pressed te up arrow.')

root = Tk()
root.bind('<Return>', callback1)
root.bind ('<Up>', callback2)

mainloop()

"""
# mozemy także powiązać zdarzenia z określonym widgetem a nie tylko
# oknem głównym
# np.  canvas.bind (<Left>, callback)
# jesli Canvas nie rozpoznaje naciśnięcia klawisza możemy użyć metody
# focus, np.   canvas.focus_set()


