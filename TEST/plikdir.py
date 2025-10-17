import pathlib
import sys

def main(args):
    katalogBiezacy = pathlib.Path("E:") / "Users"/"Opiekun" /  "Documents"
    katalogBiezacy = katalogBiezacy / "szkPython" / "TEST"
    print ("***   Przeglądamy katalog bieżący  ***")
    
    print ("*Wypisz zawartość (format długi):")
    for element in katalogBiezacy.iterdir():  # .iterdir() przetworzy wszystkie pliki i katalogi
        print(element)
    
    print ("*Wypisz zawartość (format krótki):")
    for element in katalogBiezacy.iterdir():  # .iterdir() przetworzy wszystkie pliki i katalogi
        print(element.name)
    
    print ("Wypisz wyłącznie pliki zgodne ze wzorcem *.py*:")
    for element in katalogBiezacy.glob("*.py"):  # .glob()  wszystkie pliki i katalogi zgodnie ze wzorcem bez podkatalogów / rglob() razem z podkatalogami
        print(element.name)
    
    print ("*** Przeglądamy bieżący katalog oraz podkatalogi ****")
    print ("*Wypisz wyłącznie pliki zgodne ze wzorcem i*.py:")
    for element in katalogBiezacy.rglob("i*.py"):
        print (f"Znalazłem: {element.name}", end="   ")
    print()

if __name__=="__main__":
    sys.exit(main(sys.argv))