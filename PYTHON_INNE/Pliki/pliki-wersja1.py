# Kilka popularnych metod odczytywania zawartości plików tekstowych
nazwapliku="inputs.txt"

print("*** Odczyt pojedynczych znaków ***")

try:
    plik = open(nazwapliku, "r", encoding="utf-8")  # Wpisz złą nazwę pliku, np. inputs.txz, aby sprawdzić wyjątku!
except FileNotFoundError:
    print("Hm, gdzie ten plik??")
    exit()

print("Otwarto plik: ",plik.name)
print("Tryb otwarcia: ",plik.mode)

print("Pozycja kursora:", plik.tell())

print("4 znaki:[", plik.read(4),"]")
print("Pozycja kursora po przeczytaniu 4 znaków:", plik.tell())
print("5 kolejnych znaków:[", plik.read(5),"]")
print("Ostatni znak to będzie znak nowej lini:[", plik.read(1),"]")
plik.close()            # Pamiętaj o zamykaniu pliku!

print("*** Odczyt pojedynczych wierszy ***")
# plik = open(nazwapliku, "r", encoding="ascii") # To się nie uda, jeśli w pliku będa polskie znaki...
plik = open(nazwapliku, "r") # Domyślnie: encoding="utf-8"

print("Linia 1.(3 znaki):", plik.readline(3))
print("Linia 2.(pozostałe znaki):", plik.readline(), end="")
print("Linia 2.:", plik.readline(), end="")

print("pozycja.:", plik.tell())

print("Linia 3.:", plik.readline())
print("Linia 4.(tu nic nie ma, bo nie ma takiej linii):", plik.readline())
plik.close()

print("*** Konwersja zawartości pliku na listę zawierającą odczytane wiersze  ***")
plik = open(nazwapliku, "r")
wiersze = plik.readlines()
print("Lista zawierająca wiersze odczytane z pliku:", wiersze)
print("Odczytamy wiersze zapisane w liście:")
for biezacyWiersz  in wiersze:
    print(biezacyWiersz, end="")
plik.close()

print("\n*** Iteracyjne odczytywanie wierszy ***")

i =0
plik = open(nazwapliku, "r")
for biezacyWiersz in plik:
    i=i+1
    print("Linia nr: ", i, ":", biezacyWiersz, end="")
plik.close()