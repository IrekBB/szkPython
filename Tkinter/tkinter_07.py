# Tic-tac-toe v.3
"""
Kto wygrał?
Aby to sprawdzić musimy przeanalizować wszystkie możliwości, np. trzy w linii,
trzy po przekątnej i trzy w pionie.
Aby sprawdzić czy mamy trzy w linii w pierwszym rzędzie od góry, możemy
użyć poniższej instrukcji.

if states[0][0] == states[0][1]==states[0][2] != 0:
    stop_game = True
    b[0][0].configure(bg='grey')
    b[0][1].configure(bg='grey')
    b[0][2].configure(bg='grey')

Aby sprawdzić rząd środkowy, musimy zamienić pierwszą współrzędną na 1,
ostatni środkowy - musimy zamienić pierwszą współrzędną na 2.

Czyli pętla:

for i in range(3):
    if states[i][0] == states[i][1]==states[i][2] != 0:
          b[i][0].configure(bg='grey')
          b[i][1].configure(bg='grey')
          b[i][2].configure(bg='grey')
          stop_game = True

Aby sprawdzić pola planszy w pionie, w musimy zmieniać drugą współrzędną, zamiast
pierwszej.

Musimy także zatroszczyć się o dwie przekątne.

"""



from tkinter import *
def callback(r,c):
    global player
    if player =='X' and states[r][c]==0 and stop_game == False:
        b[r][c].configure(text='X',fg='blue', bg='white')
        states[r][c] = 'X'
        player = 'O'

    if player =='O' and states[r][c]==0 and stop_game == False:
        b[r][c].configure(text='O', fg='orange', bg='black')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()
    
def check_for_winner():
    global stop_game
    for i in range(3):
    #poziomo
        if states[i][0] == states[i][1]==states[i][2] != 0:
          b[i][0].configure(bg='grey')
          b[i][1].configure(bg='grey')
          b[i][2].configure(bg='grey')
          stop_game = True
    #pionowo
    for i in range(3):
        if states[0][i] == states[1][i]==states[2][i] != 0:
          b[0][i].configure(bg='grey')
          b[1][i].configure(bg='grey')
          b[2][i].configure(bg='grey')
          stop_game = True
    # dwie diagonalne
    if states[0][0] == states[1][1]==states[2][2] != 0:
          b[0][0].configure(bg='grey')
          b[1][1].configure(bg='grey')
          b[2][2].configure(bg='grey')
          stop_game = True
    
    if states[2][0] == states[1][1]==states[0][2] != 0:
          b[2][0].configure(bg='grey')
          b[1][1].configure(bg='grey')
          b[0][2].configure(bg='grey')
          stop_game = True





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
stop_game=False
mainloop()
