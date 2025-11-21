# DataFrame - tablicowa struktura 2D, ładowana ręcznie, z CSV lub Excela
def main(args):
    dni = {"DNI": ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]}
    odczyty = {"Odczyty":[50, 60, 80, 50, 60, 90, 100]}
    dane={} # Pusty słownik
    dane.update(dni)     # Dokładamy pierwsza kolumnę    
    dane.update(odczyty)  # Dokładamy drugą kolumnę

    seria2D = pd.DataFrame(dane)
    print ("seria2D=\n", seria2D)
    print ("seria2D[\"Odczyty\"]=\n", seria2D["Odczyty"])
    print ("Ta i każda inna kolumna danych w DataFrame jest obiektem 'Series':\n",type(seria2D["Odczyty"]))

    indeksik = ["Runda1", "Runda2","Runda3", "Runda4","Runda5", "Runda6","Runda7",]
    seria2D.index=indeksik
    print ("seria2D=\n", seria2D)

    # Zmiana nazwy kolumn
    seria2D.index.name="Rundy:"
    seria2D.rename(columns={"DNI": "Dni", "Odczyty":"Odczyty"}, inplace=True)
    print ("seria2D=\n", seria2D)

if __name__=="__main__":
    import sys
    import pandas as pd
    sys.exit(main(sys.argv))