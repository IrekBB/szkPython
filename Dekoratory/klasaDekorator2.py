import sys

class Methods(object): 
    def imeth(self, x): # Zwykła metoda: przekazane self (odwołanie do obiektu klasy)      
        print([self, x])
    
    @staticmethod
    def smeth(x): # Metoda statyczna: nie przekazano żadnego obiektu
        print([x])
    
    @classmethod
    def cmeth(cls, x): # Klasa: przekazana klasa, nie instancja klasy
        print([cls, x])

    @property # Property: właściwość - wiadomo co robi
    def name(self):
        return 'Bob ' + self.__class__.__name__


def main(args):
    obj = Methods()
    obj.imeth(1)
    obj.smeth(2)
    obj.cmeth(3)
    print(obj.name)


if __name__ == "__main__":
    sys.exit(main(sys.argv))