# Okna dialogowe (Dialogs)

"""
Wiele programów korzysta z okien dialogowych w celu otwierania lub zamykania
plików itp.
Aby z nich skorzystać musimy je naprzód zaimportować:

from tkinter.filedialog import *

Okno dialogowe                         Opis
askopenfilename                        Otwiera typowe okno wyboru pliku
askopenfilenames                       Otwiera okno wyboru wielu plików
asksaveasfilename                      Otwiera typowe okno zapisu pliku  
askdirectory                           Otwiera okno wyboru katalogów

Wartość zwracana przez okna askopenfilename i asksaveasfilename to nazwa wybranego pliku.
Jeśli użytkownik nie dokona wyboru nie jest zwracana żadna wartość.

Wartość zwracana przez okno askopenfilenames to lista wybranych plików.
Jeśli użytkownik nie dokona wyboru nie jest zwracana żadna wartość.

Okno askdirectory zwraca nazwę katalogu.

Można do funkcji okien dialogowych przekazywać różne wartości.
Można przykładowo ustawić katalog początkowy, np.

filename = askopenfilename(initialdir='c:\\python31\\',
                         filetypes=[('Image files','.jpg .png .gif'), ('All files','*')])

"""

from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
textbox = ScrolledText()
textbox.grid()

filename = askopenfilename(initialdir='d:\\python\\', filetypes=[('Text files','.txt'),('All files','*')])
s = open(filename).read()
textbox.insert(1.0, s)

mainloop()
