# Tic-tac-toe v.2
"""
Aby zapobiec zmianie zawartości komórki, która już poprzednio zawierała
można odczytać etykietę przycisku lub wprowadzić dodatkową zmienną
będącą dwuwymiarową listą (states) pozwalającą sledzić wybrane uprzednio
komórki.

"""


from tkinter import *
def callback(r,c):
    global player
    if player =='X' and states[r][c]==0:
        b[r][c].configure(text='X')
        states[r][c] = 'O'
        player = 'O'

    if player =='O' and states[r][c]==0:
        b[r][c].configure(text='O')
        states[r][c] = 'O'
        player = 'X'

root = Tk()

states= [[0,0,0],
    [0,0,0],
    [0,0,0]]

b= [[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button (font=('Verdana',56), width=3, bg='yellow',
                          command=lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row=i,column=j)

player='X'
mainloop()
