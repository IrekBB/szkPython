class Element:
    def __init__(self, pDane=None, pNastepny = None):
        self.dane = pDane
        self.nastepny = pNastepny

class Lista:
    def __init__(self):
        self.glowa= None
        self.ogon = None
        self.dlugosc = 0

def main(args):
    l = Lista()
    q = Element(3)
    l.glowa = q
    l.ogon = q
    r = Element(5)
    q.nastepny = r
    l.ogon = r

    x = 5
    adres_tmp = l.glowa
    while adres_tmp != None:
        if adres_tmp.dane==x:
            print ("Znalazłem poszukiwany element")
            break
        adres_tmp = adres_tmp.nastepny
    
    if adres_tmp == None:
        print ("Nie znaleziono poszukiwanego elementu")



if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))

