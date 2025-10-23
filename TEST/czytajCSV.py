import csv       # comma separated values
import pathlib
import sys

def main(args):
    nazwapliku = pathlib.Path (r"E:\Users\opiekun\Documents\szkPython\TEST\serie.csv")
    if nazwapliku.exists():
        plik = pathlib.Path(nazwapliku).open(newline='')  # argument newline='' usuwa na końcach linii znaki  '\r\n' (Windows), '\n' (Unix), '\r' (Macintosh)
        CSVreader = csv.reader(plik,delimiter=';')   # Bo Excel zapisuje domyślnie ze średnikiem, zły znak generuje wyjątek ValueError
        print ("Prezentacja w formie tekstowej:")
        for wiersz in CSVreader:
            print (wiersz)
        plik.seek(0) # Wracamy na poczatek pliku, aby ponownie odczytać plik
        pomiary_int = list()  # Pusta lista
        wiersz_int = list()   # Lista robocza
        for wiersz in CSVreader:
            for odczyt in wiersz:
                #Konwersja z napisów na liczby (tu typ int)
                wiersz_int = [int(odczyt) for odczyt in wiersz]
            pomiary_int.append(wiersz_int)
        print ("Prezentacja w formie listy załadowanej seriami liczb:")
        print(pomiary_int)
        plik.close() 
    else:
        print ("Błędna ścieżka dostępu lub brak pliku:", str(nazwapliku))


if __name__ =="__main__":
    sys.exit(main(sys.argv))
