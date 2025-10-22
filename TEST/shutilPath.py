import pathlib
import sys
import shutil

def main(args):
    katalog = pathlib.Path (r"E:\Users\opiekun\Documents\szkPython\TEST") 
    # Skopiowanie plików z folderu X do Y
    folderSRC = katalog / "text-x" # folder źródłowy
    folderDEST = katalog / "test-x2"  # katalog docelowy
    for element in folderSRC.glob('*.*'):
        shutil.copy(element, folderDEST)   # Kopiowanie
        #shutil.move(element, folderDEST)  # Przenoszenie

if __name__ =="__main__":
    sys.exit(main(sys.argv))