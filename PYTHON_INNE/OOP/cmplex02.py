"""
__add__()        +
__sub__()        -
__mul__()        *
__truediv__()    /
__pow__()        pow() lub **
"""
class Complex:
    def __init__(self, pRe=0, pIm=0):   # Inicjalizator
        self.__re = pRe   # Atrybut __re -  część rzeczywista
        self.__im = pIm   # Atrybut __im - część urojona
    
    def __str__(self):
        return  str(self.__re) + "+" + str(self.__im) +"*i"
    
    def __add__(self, x2):
        return Complex(self.__re + x2.__re, self.__im + x2.__im)
    
    def __mul__(self,x2):
        return complex(self.__re*x2.__re - self.__im * x2.__im, self.__re * x2.__im + self.__im * x2.__re)
    
    @property
    def re(self):
        return self.__re
    
    @property
    def im(self):
        return self.__im
    
    
def main(args):
    x = Complex(5,8)
    y = Complex(1,2)

    #x.re=2    # Python zgłosi błąd "AttributeError: can't set attribute"
    print (f"Obiekt 'x' to [{x}]")
    print (f"Obiekt 'y' to [{y}]")

    z = x + y
    q = x * y

    print (f"Obiekt z=x+y to [{z}]")
    print (f"Obiekt q=x*y to [{q}]")

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))


