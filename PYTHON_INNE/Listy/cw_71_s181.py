class Element:
    def __init__(self, pDane=None, pNastepny = None):
        self.dane = pDane
        self.nastepny = pNastepny

class Lista:
    def __init__(self):
        self.glowa= None
        self.ogon = None
        
    
    def wstawNaKoniec(self, pDane):
        x = Element(pDane)
        if self.glowa == None:  # Lista pusta
            self.glowa = x
            self.ogon = x
        else:
            self.ogon.nastepny = x
            self.ogon = x
    @property
    def dlugosc(self):
        counter=0
        x = self.glowa
        while x != None:
            counter+=1
            x = x.nastepny
        return counter    

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
    
    def szukajKty(self, k):
        tmp=self.glowa
        counter = 0
        if k==0:
            print("Elementy listy numerujemy od 1 wgórę...")
            return 
        if tmp == None: 
            print ("Element nie został odnaleziony. Lista jest pusta.")
            return 
        else:
            counter=1
            while tmp != None:
                if k==counter:
                    print (f"{k}-y element został odnaleziony: {tmp.dane}")
                    return
                tmp = tmp.nastepny
                counter = counter + 1
            if tmp==None:
                print (f"Na liscie jest tylko {self.dlugosc} elementów: {self.dlugosc} < {k}")
                return


    def usunKty(self, k):
        len = self.dlugosc
        if k==1:
            self.glowa = self.glowa.nastepny
        elif k==2:
            usuwany = self.glowa.nastepny
            self.glowa.nastepny = usuwany.nastepny
        elif k in range(3,len-1):
            tmp = self.glowa.nastepny
            counter = 3
            while counter<k-1:
                tmp=tmp.nastepny
                counter = counter + 1
            usuwany = tmp.nastepny
            tmp.nastepny = usuwany.nastepny
        elif k==len:
            tmp = self.glowa
            counter=1
            while  counter<len-1:
                 tmp = tmp.nastepny
                 counter=counter+1
               
            tmp.nastepny = None
            self.ogon = tmp
            
        else:
            print (f"Nie można usunąć elementu {k}")
            




def main(args):
    print("Lista zwykła, wstawiam kolejno: 3 ,5, 7, 0")
    l = Lista()
    l.wstawNaKoniec(3)
    l.wstawNaKoniec(5)
    l.wstawNaKoniec(7)
    l.wstawNaKoniec(0)
    print (f"Ilość elementów na liście: {l.dlugosc}")
    k = int(input("k="))
    print(f"Szukamy {k}-go elementu listy: ")
    l.szukajKty(k)
    print("\n --- Uzupełniam  listę dla testu i usuwam k-aty element ----")
    l.wstawNaKoniec(117)
    l.wstawNaKoniec(15)
    l.wstawNaKoniec(27)
    l.wstawNaKoniec(10)
    print(f"Lista l przed usunieciem {k}-tego elementu=", end=" ")
    print (f"Ilość elementów na liście: {l.dlugosc}")
    l.wypisz()
    k = int(input("k="))
    l.usunKty(k)
    print(f"Lista l po usunieciu {k}-tego elementu l=", end=" ")
    l.wypisz()
    


 



if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))

