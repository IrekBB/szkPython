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
         



   

        

def main(args):
     print("Lista zwykła, wstawiam kolejno: 3 ,5, 7, 0, 1,35, 55, 75, 50\n")
     l = Lista()
     l.wstawNaKoniec(3)
     l.wstawNaKoniec(5)
     l.wstawNaKoniec(7)
     l.wstawNaKoniec(0)
     l.wstawNaKoniec(1)
     l.wstawNaKoniec(35)
     l.wstawNaKoniec(55)
     l.wstawNaKoniec(75)
     l.wstawNaKoniec(50)
     print ("Usuwamy pierwszy element")
     l.UsunPierwszy()
     l.wypisz()
     l.usunWybrany(1)
     l.wypisz()
     l.usunWybrany(7)
     l.wypisz()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
