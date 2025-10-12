"""
Ćwiczenie 7.2
Zmień nieco logikę klasy Lista i noisz metodę realizujacą usuwanie elementu
z tyłu (ogona) listy - metoda UsunOstatni() z użyciem zwykłego przeszukania listy
rekordów, bez uzywania zawartości pola ogon
"""

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
        
                
                   
def main(args):
     print("Lista zwykła, wstawiam kolejno: 3 ,5, 7, 0, 35, 55, 75, 50\n")
     l = Lista()
     l.wstawNaKoniec(3)
     l.wstawNaKoniec(5)
     l.wstawNaKoniec(7)
     l.wstawNaKoniec(0)
     l.wstawNaKoniec(35)
     l.wstawNaKoniec(55)
     l.wstawNaKoniec(75)
     l.wstawNaKoniec(50)
     print (f"Długość listy przed usunięciem pierwszego elementu: {l.dlugosc}")
     l.wypisz()
     l.UsunPierwszy()
     print(f"Długość listy po usunięciu pierwszego elementu: {l.dlugosc}")
     l.wypisz()
     print (f"Długość listy przed usunięciem ostatniego elementu: {l.dlugosc}")
     l.wypisz()
     l.usunOstatni()
     print(f"Długość listy po usunięciu ostatniego elementu: {l.dlugosc}")
     l.wypisz()




if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))