# check buttons and radio buttons

from tkinter import *

def callback():
    if show_totals.get() > 0 :
        label.configure(text='Zaznaczony!')
    else:
        label.configure(text='Niezaznaczony!')

def zwrot():
    if color.get() == 1:
        label.configure(text='RedButton',bg='red')
    elif color.get() == 2:
        label.configure(text='GreenButton',bg='green')
    elif color.get() == 3:
        label.configure(text='BlueButton',bg='blue')
    

root = Tk()

# dodajemy check box

# musimy powiązać przycisk ze zmienną, musi to być specjalna zmienne tkintera
# IntVar (u nas show_totals). Zmienna ta gdy checkbox nie zostanie zaznaczony
# będzie przyjmować wartość 0, 1 - po jego zaznaczeniu.
# dostęp do wartości zmiennej uzyskamy korzystając z metody get()
#                        show_totals.get()
show_totals = IntVar()
check =  Checkbutton (text='Show totals', var = show_totals,command = callback)
label = Label(text='Niezaznaczony!',width=14,bg='blue',fg='white')

#dodajemy radio buttons

# działa to podobnie, jesli mamy grupę przycisków to wystarczy jedna zmienna
# pierwszy przycisk na wartość jeden, drugi 2, trzeci 3
color = IntVar()
redbutton = Radiobutton(text='Red', var = color, value=1,command=zwrot)
greenbutton = Radiobutton(text='Green', var = color, value=2, command=zwrot)
bluebutton = Radiobutton(text='Blue', var = color, value=3, command=zwrot)

check.grid(row=0,column=0)
label.grid(row=0,column=1)
redbutton.grid(row=1,column=0)
greenbutton.grid(row=1,column=1)
bluebutton.grid(row=1,column=2)


mainloop()

"""
 Można także ustawić wartość zmiennej (show_totals) za pomocą metody set

            show_totals.set(1)
            check = Checkbutton ( text = 'Blue', var = show_totals)

            
"""
