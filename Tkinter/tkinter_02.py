from tkinter import *

def calculate():
    
        if entry.get()!="":
            
            try:
                temp = eval (entry.get())
                temp = 9/5 * temp + 32
                output_label.configure (text='Converted: {:.1f} F'.format(temp))
            except NameError:
                 output_label.configure (text='Value error!')
            finally: 
                entry.delete(0,END)
        else: output_label.configure (text='Empty field!')
    
        
    
    

root = Tk()
message_label = Label(text='Enter a temperature', font =('Verdana',16))
output_label = Label(font =('Verdana',16))
entry = Entry (font= ('Verdana',16), width =4)
calc_button = Button (text='Ok',font= ('Verdana',16),command = calculate)

message_label.grid(row=0, column =0)
entry.grid(row=0,column=1)
calc_button.grid (row=0, column=2)
output_label.grid(row=1, column=0,columnspan=3)

mainloop()

# Label
"""
Przykładowa etykieta:
hello_label = Label (text='hello', font=('Verdana',24, 'bold'), bg='blue', fg='white')

font
      font(font name, font size, style)

Wymagana jest jedynie nazwa czcionki, rozmiar i styl są opcjonalne
Style: bold, italic,underline,overstrike,roman, normal
Style można łączyć np. 'bold italic'

fg, bg

fg - foreground
bg - background

Można używać stałych kolorów - blue , green

width - długość pola podana w znakach, jeśli pominiemy długość pola
        dostosuje się do długości tekstu

height - wysokość pola (ilość wierszy). Można  uzyskać nowe wiersze także za pomocą
         znaków specjalnych np. text="hi\nthere".

label.configure()
Pozwala zmienić własności etykiety (większości widgetów)

label.configure(text='Bye')
label.configure(bg='white', fg='black')
label.configure(text=' a={}, and b={}'.format(a,b)) 

"""

# grid
"""
pozwala na rozmieszczenie widgetów w oknie.

(row=0, column=0)        (row=0, column=1)       (row=0, column=2)
(row=1, column=0)        (row=1, column=1)       (row=1, column=2)
(row=2, column=0)        (row=2, column=1)       (row=2, column=1)

dodatkowe argumenty grid
rowspan - pozwala rozszerzyć miejsce przeznaczone dla widgetu o jeden wiersz więcej
colspan - pozwala rozszerzyć miejsce przeznaczone dla widgetu o jedną kolumnę więcej

padx i pady - zwiększają  odstęp pomiędzy widgetami
"""

# Entry boxes
"""
Pola tekstowe służą do wprowadzania tekstu.

entry = Entry()
entry.grid(row=0, column=0)

Pobieranie tekstu/wartości z pola tekstowego

string_value = entry.get()
num_value = eval(entry.get())

Czyszczenie pola tekstowego
entry.delete (0,END)

Dodawanie tekstu do pola tekstowego:
entry.insert(0, 'hello')

"""




