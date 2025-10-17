"""
import os
if os.path.exists(r" testdir\test.py")..............
if os.path.exists("testdir/test.py) ..................

os.rmdir("testdir2")
os.mkdir ("testdir")

Dekompozycja na składowe ściezki Path:
.name - nazwa pliku bez elementów ścieżki katalogu
.parent - katalog, w którym znajduje się plik lub katalog nadrzędny
.stem - ostatni element scieżki, nazwa pliku bez rozszerzenia
.suffix - rozszerzenie
.anchor - początek ścieżki

Istnienie katalogu/pliku w klasie Path:
if cosTam.exists():
    print (f"Katalog lub plik {cosTam} istnieje")

"""
import pathlib
import sys

def main(args):
    katalogDomowy = pathlib.Path.home() # Obiekt wskazujący na katalog
    katalogBiezacy = pathlib.Path.cwd()
    pewien_plik = katalogBiezacy / pathlib.Path("witamy.py")  # Obiekt wskazujący na plik
    print (f"Katalog domowy: {katalogDomowy} \nBieżący katalog: {katalogBiezacy}")
    print (f"Nasz pierwszy program w Pythonie: {pewien_plik} ")

    print (f"Dekompozycja składowych - nazwa: {pewien_plik.name}")
    print (f"Dekompozycja składowych - trzon: {pewien_plik.stem}")
    print (f"Dekompozycja składowych - suffiks: {pewien_plik.suffix}")
    print (f"Dekompozycja składowych - parent: {pewien_plik.parent}")
    print (f"Dekompozycja składowych - anchor: {pewien_plik.anchor}")

    katalogBiezacy = pathlib.Path.cwd()
    katalogDel = katalogBiezacy / pathlib.Path("testdir2")   # katalogNowy = katalogBiezacy / pathlib.Path("testdir3")
    try:
        print (f"Chcemy usunąć {katalogDel}")
        katalogDel.rmdir()                                   #katalogNowy.mkdir()
    except OSError:
        print ("Coś poszło nie tak. Sprawdź, czy katalog istnieje lub czy nie zawiera plików")


if __name__=="__main__":
    sys.exit(main(sys.argv))