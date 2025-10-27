import sys
import pathlib

def main(args):
     katalogBiezacy = pathlib.Path("E:") / "Users"/"Opiekun" /  "Documents" / "szkPython" / "TEST"
     # Od tego folderu rozpoczniemy operację "Nieszkodliwy dotyk"
     folderStartowy = katalogBiezacy / "test-touch"
     if not folderStartowy.exists():
          print (f"Katlog: '{folderStartowy}' nie istnieje!")
          exit()
     nazwaZnacznika = "NasiTuByli.txt"
     plikZnacznik = folderStartowy / nazwaZnacznika  # Nazwa pliku znacznika dla folderu startowego
     plikZnacznik.touch(exist_ok=True) # Tworzymy pierwszy plik w katalogu startowym
     print ("Odwiedzam folder startowy:", folderStartowy.name)
     # Przegladamy zawartość katalogu startowego i jego "potomków"
     for element in folderStartowy.rglob("*"):
          if element.is_dir():
               print ("Odwiedzam: ", element.name, end="-->")
               #Tworzę pliki znaczników w podkatalogach
               (element / nazwaZnacznika).touch(exist_ok=True)
               print ("Maks i Albert tu byli")
     print()



if __name__ == "__main__":
    sys.exit(main(sys.argv))
