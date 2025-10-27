"""
Hierarchia dziedziczenia i kolejność wyszukiwania metod.
 W Pythonie klasę można utworzyć dziedzicząc z dowolnej klasy, 
 w szczególności z takiej, która już dziedziczy z innej. 

"""

class First:
    def fun1(self):
        print("fun1")


class Second(First): # Second dziedziczy z First
    def fun2(self):
        print("fun2")


class Third(Second): # Third dziedziczy z Second
    def fun3(self):
        print("fun3")

def main(args):
    # Relacja bycia podklasą jest zatem przechodnia: podklasa podklasy klasy jest podklasą klasy. 
    x = Third() # w klasach nie definiowaliśmy konstruktora - użyty jest domyślny, "pusty"
    print(isinstance(x, Third))
    print(isinstance(x, Second))
    print(isinstance(x, First))
    x.fun3() # Third.func3(x)
    x.fun2() # Second.func2(x)
    x.fun1() # First.func1(x)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
