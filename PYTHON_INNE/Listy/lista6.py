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
    
def fuzja(x1, y1):   # x1 i y1 to obiekty klasy lista
    nowaLista = Lista()
    nowaLista.dlugosc = x1.dlugosc + y1.dlugosc
    nowaLista.glowa = sortuj(x1.glowa, y1.glowa)

    if x1.glowa == None:
        nowaLista.ogon = y1.ogon
    elif y1.glowa == None:
        nowaLista.ogon = x1.ogon
    else:
        if x1.ogon == None: 
            nowaLista.ogon = x1.ogon
        else:
            nowaLista.ogon = y1.ogon
    return nowaLista




def main(args):
    
    x1, y1 = Lista(), Lista()
    for n in [3, 6, 2, 5, 12, 0, 19]:
        x1.wstawSort(n)
    
    print ("Lista x1 =", end=" ")
    x1.wypisz()

    for n in [5, 2, 2, 1, 9]:
        y1.wstawSort(n)
    
    print ("Lista y1 =", end=" ")
    x1.wypisz()

    pofuzji = fuzja(x1, y1)
    print("Lista x1+y1 (fuzja) =", end=" ")
    pofuzji.wypisz()

    
if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))