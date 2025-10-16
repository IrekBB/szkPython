class Complex():
    def __init__(self, pRe=0, pIm=0):
        self._re = pRe
        self._im = pIm
        print ("Tworzymy nowy obiekt......")
    
    def __str__(self):            # zwróci zawartość obiektu jako napis
        return str(self._re) + "+" + str(self._im) + "*i"
    
    def dodaj(self, x2):
        self._im = self._im + x2._im
        self._re = self._re + x2._re

    @property
    def re(self):
        return self._re
    @property
    def im(self):
        return self._im
    
    @re.setter
    def re(self, pRe):
        self._re = pRe
    
    @im.setter
    def im(self, pIm):
        self._im = pIm

class ComplexNew(Complex):
    def __init__(self, pRe=0,pIm=0):
        super().__init__(pRe,pIm)
       
       
    
    def __str__(self):
        print ("Klasa [NewComplex]")
        return str(self.re) + "+" + str(self.im) + "*i"

    
    def __add__(self, x2):
        return ComplexNew(self._re + x2._re, self._im + x2._im)

    def __sub__(self, x2):
        return ComplexNew(self._re - x2._re, self._im - x2._im)

    def __mul__(self, x2):  # Ta metoda zwraca obiekt będący iloczynem dwóch liczb zespolonych (np.x·y)       
              # x1=a+b·i,x2=c+d·i
              # x1·x2 = (ac-bd) + (ad + bc)·i
              return Complex( self._re * x2._re - self._im * x2._im,
                              self._re * x2._im + self._im * x2._re)
    
    # inne: __truediv__() ;  __pow__()
    
    

if __name__=="__main__":
    print ("To jest moduł. Aby go przetestować uzyj pliku MainKlasa0.py")
     