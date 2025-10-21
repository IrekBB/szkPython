""""
is_dir()  - czy elemeny jesyt katalogiem
is_file() - czy element jest plikiem 
parts() - zwraca tuple składające się z elementów ścieżki
match(wz) - czy ścieżka jest zgodna z oddanym wzorcem wz
stat() - zwraca informacje o pliku lub katalogu, np. stat().st_size - pokaże jego nrozmiar,
         stat().st_mode - typ i uprawnienia

"""
import pathlib
import sys
import os

def main(args):
    katalogBiezacy = pathlib.Path("E:") / "Users"/"Opiekun" /  "Documents" / "szkPython"
    for e in katalogBiezacy.iterdir():
        if e.is_dir():
            print ("katalog: ", e.name, " typ i uprawnienia: ", e.stat().st_mode, " rozmiar:", e.stat().st_size )
            podfolder = pathlib.Path(e)
            for e in podfolder.iterdir():
                print ("\t", "podkatalog=",e.is_dir(), " ", e.name)
        elif e.is_file():
            print ("plik: ", e.name, " typ i uprawnienia: ", e.stat().st_mode, " rozmiar:", e.stat().st_size )

    print (f"Dekompozycja katalogu {katalogBiezacy} na składowe (tupla): {katalogBiezacy.parts}")

if __name__ == "__main__":
    sys.exit(main(sys.argv))
