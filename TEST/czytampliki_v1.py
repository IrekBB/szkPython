"""
zmiana rozszerzenia pliku:
nazwa = pathlib.Path("sample.log")
nazwa = nazwa.rename(str(nazwa.stem)+ ".bak")

"""
# Wykorzystanie pathlib do odczytu plików
import pathlib
import sys

def main(args):
    katalogBiezacy = pathlib.Path.cwd() # Obiekt wskazujący na katalog bieżący
    nazwapliku = "inputs.txt"
    plik = katalogBiezacy / nazwapliku
    print ("Odczytujemy plik testowy, uzywając metody 'open' z klasy 'Path'")
    print("Czytamy cały plik tekstowy, za jednym zamachem:")
    with plik.open(mode="r", encoding="utf-8") as f:
        tekst = f.read() # Czytamy cały plik
    print (tekst)

    print ("- Czytamy pojedyncze linie:")
    with plik.open() as f:
        for wiersz in f.readlines():  # Czytamy pojedyncze wiersze
            print (f" Odczytany wiersz: {wiersz}", end ="")

    print()


if __name__ =="__main__":
    sys.exit(main(sys.argv))