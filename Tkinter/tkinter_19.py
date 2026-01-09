# Title bar - nazwa okna
"""
root.title('Your title')
"""

# Dezaktywacja przycisku
"""
atrybut: state

# Dezaktywacja
button = Button(text='Hi', state = DISABLED, command=function)
# Aktywacja
button.configure(state=NORMAL)
"""

# Odczytywanie stanu widgetu
"""
cget

label.cget('text')  # pobiera tekst etykiety label

Tkinter dostarcza operatora [], który służy temu samemu celowi

label['text']
"""

# Message Boxes

from tkinter.messagebox import *

showinfo(title='Message for you', message='Hi There!')
askquestion (title='Quit?', message='Do you really want to quit?')
showwarning(title='Warning', message='Unsupported format')

"""
inne okna wiadomości:
  askokcancel
  askretrycancel
  askyesnocancel
  showerror
"""

# Wartości zwracane przez okna wiadomości
"""
showinfo         zawsze zwraca 'ok'
askokcancel      OK-True,  Cancel(lub zamknięcie okna) - False
askquestion      Yes -'yes', No -'no'
askretrycancel   Retry-True,  Cancel (lub zamknięcie okna) - False
askyesnocancel   Yes-True,  No-False, inny wybór None
showerror        zawsze 'ok'
showwarning      zawsze 'ok'
"""


  
