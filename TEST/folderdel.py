import pathlib
import sys

def main(args):
    katalogBiezacy = pathlib.Path (r"E:\Users\opiekun\Documents\szkPython\TEST")    # E:\Users\opiekun\Documents\szkPython\TEST
    folderDel = katalogBiezacy / pathlib.Path (r"testdir3")  # Usuwamy katalog 'testdir3'
    print(f"Sprawdzamy, czy katalog {folderDel} istnieje:", folderDel.exists())
    print (f"Kasujemy katalog {folderDel}:")
    for element in folderDel.iterdir():
        print ("Usuwam:", element.name)  # Usuwamy pliki z tego katalogu, a co z innymi folderami? 'rglob("*")'
        element.unlink()
    print (f"Teraz usuwam {folderDel}")
    folderDel.rmdir()

    print (f"Sprawdzamy, czy katalog {folderDel} istnieje:", folderDel.exists())



    

if __name__ =="__main__":
    sys.exit(main(sys.argv))