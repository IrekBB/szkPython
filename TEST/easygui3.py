import easygui
import sys

def main(args):
    # Otwieranie katalogu: diropenbox
    print ("Otwieranie katalogu:")
    msg = "Katalogi zawierające repozytorium"
    title = "Pobieranie nazwy katalogu"
    default=""
    res = easygui.diropenbox(msg, title,default)
    print(res)
    # Selektor wyboru pliku: fileopenbox
    print ("Wybieranie pliku do otwarcia")
    msg="Logi aplikacyjne"
    title = "Pobieranie nazwy pliku"
    default=""
    res = easygui.fileopenbox(msg, title, default)
    print(res)
    # Zapis pliku na dysku: filesavebox(msg=None, title=None, default='', filetypes=None)
    """
    Funkcja generuje nazwę pliku do zapisania. Funkcja ta zwraca jedynie
    zwykły napis reprezentujący ścieżkę pliku (lub None po wciśnięciu Anuluj). Na 
    samym dysku nie zostanie nic fizycznie zapisane jesli nie uzyjemy dedykowanej ku temu metody Pythona
    """
    msg = "Zapis do pliku"
    title = "Okienko zapisywania do pliku"
    default="e:/Users/opiekun/Documents/szkPython/TEST/"
    filetypes=None
    print(msg)
    res = easygui.filesavebox(msg, title, default, filetypes)
    print ("Wybrano plik do zapisu:", res)


if __name__=="__main__":
    sys.exit(main(sys.argv))