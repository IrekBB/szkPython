class Osoba:
    def __init__(self,pImie, pNazwisko):
        print("* Inicjalizator klsasy bazowej 'Osoba'")
        self.imie = pImie
        self.nazwisko = pNazwisko

    def __str__(self):
        return self.imie + " " + self.nazwisko

    def komunikat1(self):
        print ("Kominikat 1: metoda klasy 'Osoba'")

    def komunikat2(self):
        print ("Kominikat 2: metoda klasy 'Osoba'") 
    
class Uczen(Osoba):    # Klasa pochodna
    def __init__(self, pImie, pNazwisko, pNrKlasy):
        print("* Inicjalizator klsasy pochodnej 'Uczen'")
        # Wywołujemy inicjalizator klasy bazowej
        super().__init__(pImie, pNazwisko)
        self.nrklasy = pNrKlasy
    
    def __str__(self):
        s = super().__str__()
        return s + ", Klas: "+self.nrklasy

    def komunikat2(self):
        print ("Komuniklat 2: nowa metoda klasy 'Uczen' ")

def main(args):
    
    o = Osoba("Janek", "Kowalski")
    print("Obiekt klasy bazowej 'Osoba': ", o)
    o.komunikat1()
    o.komunikat2()

    u = Uczen("Anna", "Kotecka", "2A")
    print("Obiekt klasy pochodnej 'Uczen': ", u)
    u.komunikat1()
    u.komunikat2()


if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
