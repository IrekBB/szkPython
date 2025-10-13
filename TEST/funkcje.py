komunikat = "[odmówił podania]"
def pacjent(numer, imie=komunikat, nazwisko=komunikat):    # wartości domyślne
    print(f"Pacjent: nr={numer} imię: {imie} nazwisko: {nazwisko}")

def parametry(*params):   # procedura ze zmienną iloscią parametrów
    for x in range(0, len(params)):
        print(f"Parametr {x} to {params[x]}")  # Wypisuje każdy parametr

def scenariusz_testowy(**params):    # nazwana lista parametrów
    t1 = params["timing1"]
    t2 = params["timing2"]
    s = params["napis"]
    print (f"timing1={t1}, timing={t2}, napis={s} ")


def main(args):
    pacjent(4)
    pacjent(5, "Jan","Kowalski")
    parametry(2, "New York",  6, 6.5)
    scenariusz_testowy(timing1=50, timing2=100, napis="ala")

if __name__=="__main__": 
    import sys
    sys.exit(main(sys.argv))
