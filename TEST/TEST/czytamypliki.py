"""
/Users/piotr/Documents/test.xls    (wersja Linux lub macOS)
r"C:\Windows\temp\awr200e.log"  (wersja Windows, pisownia naturalna, 
                                literka r oznacza tryb ignorowania znaków \, 
                                czyli tzw. symboli i kodów specjalnych)
C:/Windows/temp/awr200e.log  (Windows, wersja dopasowana do wymogów Pythona)
"""
"""
tryb	znaczenie
r	Odczyt (ang. read)
r+	Odczyt i zapis
w	Zapis (ang. write). Jeśli plik istnieje, zostaje nadpisany.
x	Zapis, ale tylko jeśli plik nie istnieje.
a	Dopisanie na końcu pliku (ang. append).
ab+  Otwarcie pliku binarnego w trybie odczytywania i dopisywania na jego końcu. Jesli plik 
     nie istnieje to zostanie utworzony nowy do zapisywania. Jesli plik istnieje, to wskaźnik 
     do niego jest umieszczony na jego końcu, umożliwiając dopisywanie
rb  Odczyt z pliku w trybie binarnym . Wskazany plik musi istnieć, aby uniknąć wyjątku
    FileNotFoundError
w+  Odczytywanie i zapisywanie do do pliku w trybie tekstowym. Jeśli plik istnieje , to zostanie nadpisany,
    jesli nie istnieje, to zostanie utworzony nowy do odczytywania i zapisywania
wb  Zapis do pliku w formacie binarnym. Jesli nie istnieje zostanie nadpisany
wb+ Odczytywanie i zapisywanie do pliku w trybie binarnym. Jeśli plik istnieje, to zostanie nadpisany,
    jesli nie istnieje to zostanie utworzony nowy do odczytywania i zapisywania
a+  Otwarcie pliku tekstowego w trybie odczytywania i dopisywania na jego końcu.Jesli plik nie istnieje
    to zostanie utworzony nowy do zapisywania. Jesli plik istnieje, to wskaźnik do niego jest umieszczony
    na jego końcu.
ab  Otwarcie pliku binarnego w trybie dopisywania na jego końcu. Jesli plik nie istnieje, to zostanie 
    utworzony nowy do zapisywania. Jesli plik istnieje, to wskaźnik do niego jest umieszczony na jego końcu

"""
def main(args):
    nazwapliku = "inputs.txt"
    print ("***   Odczyt pojedynczych znaków   ***")
    try:
        plik = open (nazwapliku, "r")
    except FileNotFoundError:
        print ("Hm, gdzie ten plik")
        exit()
    print ("Otwarto plik: ", plik.name)
    print ("Tryb otwarcia: ", plik.mode)
    print ("Pozycja kursora: ", plik.tell())
    print ("4 znaki:[",plik.read(4),"]")
    print ("Pozycja kursora po przeczytaniu 4 znaków: ", plik.tell())
    print ("5 kolejnych znaków znaki: [", plik.read(5), "]")
    print("Ostatni znak to będzie znak nowej linii:[", plik.read(1),"]")
    plik.close()

    print ("***   Odczyt pojedynczych wierszy   ***")
    try:
        plik = open (nazwapliku, "r")
    except FileNotFoundError:
        print ("Hm, gdzie ten plik")
        exit()
    print ("Linia 1. (3 znaki):", plik.readline(3))
    print ("Linia 2.(pozostałe znaki):", plik.readline(), end="")
    print ("Linia 2.:", plik.readline(), end="")
    print ("Linia 3: ", plik.readline())
    # Wiersz 4 nie istnieje i ta instrukcja nic nie zwróci
    print ("Linia 4. (tu nic nie ma, bo nie ma takiej linii): ", plik.readline())
    print ("*** Konwersja zawartości pliku do listy  zawierającej odczytane wiersze ***")
    plik = open (nazwapliku)
    wiersze = plik.readlines()
    print ("Lista zawierajaca wiersze odczytane z pliku: ", wiersze)
    print ("Odczytamy wiersze zapisane na liście:")
    for biezacyWiersz in wiersze:
        print (biezacyWiersz, end="")
    plik.close()

    print ("\n*** Iteracyjne odczytywanie wierszy ***")
    i=0
    plik = open(nazwapliku)
    for biezacyWiersz in plik:
        i=i+1
        print("Linia nr: ", i, ":", biezacyWiersz, end="")
    plik.close()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))