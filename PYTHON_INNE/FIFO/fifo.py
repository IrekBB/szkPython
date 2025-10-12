class FIFO:
    def __init__(self, pRozmiar):
        self._kolejka = list()
        self._MaxElt = pRozmiar
        self._licznik = 0
        print("Tworzę kolejke o pojemności " + str(self._MaxElt))
    def wstaw(self, obj):
        if self._licznik < self._MaxElt:
            self._kolejka.append(obj)
            self._licznik = self._licznik + 1
        else:
            print(f"* Gdzie się Pan {obj} wpycha? Tu obowiązuje lista kolejkowa! *")
    def obsluz(self):
        if self._licznik  != 0:         # Ktoś stoi w kolejce...
            temp = self._kolejka.pop(0) # pobierz wartość z przodu
            self._licznik = self._licznik -1
            return temp
        else:
            print ("** Kolejka pusta **")
    def pusta(self):   # czy kolejka pusta
        return self._licznik == 0
    def wypisz(self,s):
        print(s)
        if self._licznik != 0:
            print(" Zawartość kolejki: [", end=" ")
            for x in self._kolejka:
                print(x, end=" ")
            print("]")    
    
def main(args):
    kolejka = FIFO(4)
    kolejka.wstaw("Kowalska")
    kolejka.wstaw("Fronczak")
    kolejka.wstaw("Becki")
    kolejka.wstaw("Pigwa")
    kolejka.wstaw("Cwaniak")
    kolejka.wstaw("Spóźnialski")
    kolejka.wypisz("1 -Stan kolejki")
    szczesliwiec = kolejka.obsluz()
    print ("Obsłuzony został klient: " + str(szczesliwiec))
    kolejka.wypisz("2 -Stan kolejki")
    print("Przyszedł Pan 'Spóźnialski'")
    kolejka.wstaw("Spóźnialski")
    kolejka.wypisz("3 - Stan kolejki ")
    print ("Ekspresowa obsługa całej kolejki przed zamknięciem sklepu!")
    while not kolejka.pusta():
        k = kolejka.obsluz()
        print ("Obsłuzony został klient: " + str(k))
    print ("Kolejka pusta, zamykamy sklep!")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))


