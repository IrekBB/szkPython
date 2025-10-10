def main(args):
    lokaty_slownik = dict()
    lokaty_lista = list()
    katalogBiezacy = pathlib.Path.cwd() 
    file = katalogBiezacy / "MojePliki" / "petenci.csv"
    if file.exists():
        with open(file) as f:
            for linijka in f:
                odczyt = linijka.split(",")
                data = odczyt[0]
                depozyt = [odczyt[1], float(odczyt[2])]
                lokaty_slownik[data] = depozyt            # Zapisujemy pary wartości do SŁOWNIKA
                lokaty_lista.append([data, depozyt])      # Zapisujemy pary wartości do LISTY

        print(lokaty_lista)
        print(lokaty_slownik)

        klucz = "12.03.2022"
        print("[Przeszukiwanie liniowe listy]: Szukam wpisu dla daty ", klucz)
        for i in range (len(lokaty_lista)):
            if lokaty_lista[i][0] == klucz:
                print (lokaty_lista[i][1])
        print("[Przeszukiwane bezpośrednie słownika]: Szukam wpisu dla daty ", klucz)
        if lokaty_slownik.get(klucz) != None:
            print (lokaty_slownik[klucz])
        else:
            print ("Brak rekordu")     
                

    else:
        print ("Plik  'petenci.csv' nie istniej w lokalizacj: ",  katalogBiezacy / "Moje Pliki"  )    

if __name__ == "__main__":
    # from MojeTypy import Hash as H
    import pathlib
    import sys
    sys.exit(main(sys.argv)) 