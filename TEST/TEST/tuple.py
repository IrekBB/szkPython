"""
Zalety:
1. służą do definiowania niezmiennych zestawów danych
2. dostęp do tupli jest szybszy niż do list (bo są statyczne), wzrost wydajności aplikacji
3. umożliwiają tzw. przypisania wielokrotne

"""

def main(args):
    print ("Ilustracja niebezpośredniego modyfikowania zawartości tupli")
    nazwy_skrocone=['pon', 'wt', 'śr', 'czw', 'pt', 'sob']  # na liście brak 'nd'!
    tupla5 = ("dni", nazwy_skrocone)
    print("Tupla oryginalna, dwuelementowa:", tupla5)
    # Modyfikacja listy
    tupla5[1].append("nd")
    print ("Tupla po dodaniu 'nd' do listy wskazywanej przez drugi element tupli:\n", tupla5)
    print ("*****************************************************************************")
    print("Modyfikacja tupli przez konwersję na listę")
    dni_robocze = ('pon', 'wt', 'śr', 'czw', 'pt')
    print ("Dni robocze", dni_robocze)
    dni_robocze_lista=list(dni_robocze)
    dni_robocze_lista.append('sob')
    dni_robocze=tuple(dni_robocze_lista)
    print ("Dni robocze", dni_robocze)
    print ("*****************************************************************************")
    dozwolone_waluty = ('PLN', 'EUR', 'USD')  # Tupla jako statyczna lista referencyjna
    print("Dozwolone waluty to:", dozwolone_waluty)
    s=input("Podaj walutę: ")
    if s.upper() in dozwolone_waluty:
        print ("Poprawna waluta")
    else:
        print("Nieznany kod waluty")
    print ("*****************************************************************************")
    pacjent_domyslny = ("John Doe", 55)  # To jest tupla jako statyczna lista referencyjna
    (nazwisko, wiek) = pacjent_domyslny
    print (f"Dane przyjętej osoby: Nazwisko: {nazwisko}, wiek={wiek}")


if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))