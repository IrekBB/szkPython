def main(args):
    print ("***   Odczyt pliku GIF w trybie binarnym   ***")
    plik = open ("plik-graficzny.gif","rb")
    dane = plik.read()
    dlugosc = len(dane)
    print ("Otwarto plik: ", plik.name)
    print ("Tryb otwarcia: ", plik.mode)
    print ("Plik zajmuje ", dlugosc," bajtów na dysku")
    plik.seek(0)
    print ("10 początkowych bajtów:")
    for i in range(0, 10):
        c = plik.read(1)
        print ("Bajt nr: ", i, " : ",c," hex: ",c.hex())
    plik.close()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))