class Element:
    def __init__(self, pDane=None, pNastepny = None):
        self.dane = pDane
        self.nastepny = pNastepny

class Lista:
    def __init__(self):
        self.glowa= None
        self.ogon = None
        self.dlugosc = 0
    
    def wstawNaKoniec(self, pDane):
        x = Element(pDane)
        if self.glowa == None:  # Lista pusta
            self.glowa = x
            self.ogon = x
        else:
            self.ogon.nastepny = x
            self.ogon = x
        self.dlugosc = self.dlugosc + 1    

    def wypisz(self):
        tmp = self.glowa
        if tmp == None:  
            print("\n lista pusta")
            return
        while tmp != None:
            print (tmp.dane, end=" ")
            tmp = tmp.nastepny
        print("\n")         

    def szukaj(self, x):
        tmp = self.glowa
        while tmp != None:
            if tmp.dane == x:
                print("\n Znalazłem poszukiwany element ", x)
                break
            tmp=tmp.nastepny
        if tmp==None:
            print ("\n Nie znaleziono poszukiwanego elementu ", x)

    def wstawSort(self, x):
        nowy = Element(x)
        self.dlugosc = self.dlugosc + 1
        # Poszukiwanie właściwej pozycji na wstawianie elementu
        if self.glowa == None:  # Lista pusta
            self.glowa = nowy
            self.ogon  = nowy
            return   # Szybkie opuszczenie funkcji
        szukamy = True
        przed = None
        po = self.glowa
        while szukamy and po != None:
            if po.dane >= x:     # Kryterium sortowania
                szukamy = False  # Znaleźliśmy właściwe miejsce
            else:
                przed = po
                po = po.nastepny
        # Wstawiamy elementy, analizując wartości zapamiętane w 'przed' i 'po'
        if przed == None:  # Na poczatek listy
            self.glowa = nowy
            nowy.nastepny = po
        else:
            if po == None:  # Na koniec listy
                przed.nastepny = nowy
                self.ogon = nowy  # nowy koniec listy
            else: # Wstawiamy gdzieś w środku, "rozpinając" łańcuszek danych
                przed.nastepny = nowy
                nowy.nastepny = po

                  
                
            

           
       

def main(args):
    l = Lista()
    print("Lista zwykła, wstawiam kolejno: 3 ,5, 7, 0, 1, 6, 7")
    l.wstawSort(3)
    l.wstawSort(5)
    l.wstawSort(7)
    l.wstawSort(0)
    l.wstawSort(1)
    l.wstawSort(6)
    l.wstawSort(7)
    print("Lista l=", end=" ")
    l.wypisz()

 



if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))

