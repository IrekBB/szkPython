def main(args):
    nazwapliku1 = "pliki/input1.txt"     # plik wejściowy 1
    nazwapliku2 = "pliki/input2.txt"     # plik wejściowy 2
    nazwapliku3 = "pliki/input3.txt"     # plik wejściowy  = złaczenie plików  1 i 2

    with open(nazwapliku3, 'wb') as outfile:  # Złączamy pliki
        with open(nazwapliku1, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
        with open(nazwapliku2, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)

    subprocess.call('sort pliki/input3.txt /O pliki/outfile.txt')
    print("Przykładowa konwersja zawartości pliku do listy zawierającejodczytane wiersze:")
    plik = open(nazwapliku3, "r")
    wiersze = plik.readlines()
    print(wiersze)
    print("*** Sortujemy ***")
    wiersze.sort() # Alternatywne kopiowanie do innej listy: wynik=sorted(wiersze)
    print(wiersze)



if __name__ == "__main__":
    import  sys
    import shutil
    import subprocess
    sys.exit(main(sys.argv))

