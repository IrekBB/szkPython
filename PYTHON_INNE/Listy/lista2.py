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
    

def main(args):
    print("Lista zwykła, wstawiam kolejno: 3 ,5, 7, 0")
    l = Lista()
    l.wstawNaKoniec(3)
    l.wstawNaKoniec(5)
    l.wstawNaKoniec(7)
    l.wstawNaKoniec(0)
    print("Lista l=", end=" ")
    l.wypisz()

 



if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))

