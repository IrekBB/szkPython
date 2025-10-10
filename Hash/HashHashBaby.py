def main(args):
    lokaty_lista = [None] * H.RMAX
    katalogBiezacy = pathlib.Path.cwd() 
    file = katalogBiezacy / "MojePliki" / "petenci.csv"
    if file.exists():
        with open(file) as f:
            for linijka in f:
                odczyt = linijka.split(",")
                indeksik = hash(odczyt[0]) % H.RMAX  # Za indeks przyjmujemy datę

                # Szukamy miejsca na wstawienie
                while (lokaty_lista[indeksik] != None):    # Mamy kolizę !
                    indeksik = (indeksik + 1) % H.RMAX
                
                wpis = [odczyt[0], odczyt[1], float(odczyt[2])]  # Cała zawartość do tablicy danych

                lokaty_lista[indeksik] = wpis    # Zapis zawartości do listy
        
        # W celach kontrolnych drukujemy minibazę słownikową
        for i in range (H.RMAX):
            if lokaty_lista[i] != None:
                print(lokaty_lista[i])
        # Szukamy wpisu dla podanego klucza
        klucz = "15.04.2022"
        res = H.szukaj(lokaty_lista, klucz)
        print (f"szukamy rekordu dla klucza {klucz}, wynik: {res}")




    else:
        print ("Plik  'petenci.csv' nie istniej w lokalizacj: ",  katalogBiezacy / "Moje Pliki"  )    

if __name__ == "__main__":
    from MojeTypy import Hash as H
    import pathlib
    import sys
    sys.exit(main(sys.argv)) 