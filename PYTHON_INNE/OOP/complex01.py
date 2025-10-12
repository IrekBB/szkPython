class Complex:
    def __init__(self, pRe=0, pIm=0):
        self.re = pRe
        self.im = pIm
        print ("Narodził się nowy obiekt....  Nie zapomnij o deklaracji 500+ ")
    def __str__(self):
        return str(self.re) + "+" + str(self.im) + "*i"
    
    def dodaj(self, x2):
        self.im = self.im + x2.im
        self.re = self.re + x2.re

def main(args):
    n = Complex()
    print (f"Obiekt 'n' to [{n}]")
    x = Complex(5,8)
    y = Complex(1,2)
    print (f"Obiekt 'x' to [{x}]")
    print (f"Obiekt 'y' to [{y}]")
    x.dodaj(y)
    print (f"Obiekt 'x=x+y' to [{x}]")
    print("Ustawiamy wartość 're' obiektu 'x' na -3")
    x.re = -3
    print (f"Obiekt 'x' to [{x}]")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))

