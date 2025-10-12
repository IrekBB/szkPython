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

    def UsunPierwszy(self):    # Usuń pierwszy element z listy
        if self.glowa != None:
            self.glowa = self.glowa.nastepny
        self.dlugosc = self.dlugosc - 1

    def usunOstatni(self):
        przed = None
        po = self.glowa
        while po.nastepny != None:
            przed = po
            po = po.nastepny
        
        przed.nastepny = None
        self.ogon = przed
        self.dlugosc = self.dlugosc - 1

    def szukajRef(self, x):
        biezacy = self.glowa
        poprzedni = None
        while biezacy != None:
            if biezacy.dane == x:
                return poprzedni, biezacy, True
            poprzedni = biezacy
            biezacy = biezacy.nastepny
        return poprzedni, biezacy, False

    def usunWybrany(self, x):   # Odszukaj i usuń element z listy
        poprzedni, biezacy, znaleziono = self.szukajRef(x)   # Szukamy elementu i jeo pozycji

        if znaleziono==False:
            print("Nie znaleziono elementu")
            return
        self.dlugosc  = self.dlugosc - 1  # Skracamy parametr opisujący długośc listy o 1

        if self.dlugosc == 0:  # Przypadek lista pusta
            self.glowa = None
            self.ogon  = None
            self.dlugosc = 0
            return 
        
        if self.glowa == biezacy:    # Usuwamy z przodu
            self.glowa = biezacy.nastepny
            return
        
        if self.ogon == biezacy:
            self.ogon = poprzedni
            poprzedni.nastepny = None
            return
        
        
        poprzedni.nastepny = biezacy.nastepny   
    
    
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

    def __add__(self, x2):
        suma = Lista()
        q1 = self.glowa
        q2 = x2.glowa
        
        while q1 != None:
            suma.wstawSort(q1.dane)
            q1 = q1.nastepny
        
        while q2 != None:
            suma.wstawSort(q2.dane)
            q2 = q2.nastepny
        return suma

def sortuj(a,b):
    if a==None:
        return b
    
    if b==None:
        return a
    
    if a.dane <= b.dane:
        a.nastepny = sortuj(a.nastepny,b)
        return a
    else:
        b.nastepny = sortuj(b.nastepny, a)
        return b
    
    


def main(args):
     print("Lista zwykła, wstawiam kolejno: 3 ,5, 1000, 0, 1,35, 55, 75, 50\n")
     l1 = Lista()
     l1.wstawNaKoniec(3)
     l1.wstawNaKoniec(5)
     l1.wstawNaKoniec(7)
     l1.wstawNaKoniec(0)
     l1.wstawNaKoniec(1)
     l1.wstawNaKoniec(35)
     l1.wstawNaKoniec(55)
     l1.wstawNaKoniec(75)
     l1.wstawNaKoniec(50)
     print("Lista zwykła, wstawiam kolejno: 113 ,115,11 711,110, 1111,1135, 1155, 1175, 1150\n")
     l2 = Lista()
     l2.wstawNaKoniec(113)
     l2.wstawNaKoniec(115)
     l2.wstawNaKoniec(11)
     l2.wstawNaKoniec(711)
     l2.wstawNaKoniec(110) 
     l2.wstawNaKoniec(1111)
     l2.wstawNaKoniec(1155)
     l2.wstawNaKoniec(1175)
     l2.wstawNaKoniec(1150)
     l = l1 + l2
     print("Suma list: ", end="")
     print(sortuj(l1,l2))
     l.wypisz()
   

    

    
if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))