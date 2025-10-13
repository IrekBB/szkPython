from MojeTypy import klasa0 as k


def main(args):
    n = k.Complex()
    print (f"Obiekt 'n' to [{n}]")
    x =k.Complex(5,8)
    y = k.Complex(1,2)
    print(f"Obiekt 'x' to [{x}]")
    print(f"Obiekt 'y' to [{y}]")
    x.dodaj(y)
    print(f"Obiekt 'x=x+y' to [{x}]")
    print ("Ustawiamy wartość 'Re' obiektu 'x' na -3")
    x.re = -3
    print(f"Obiekt 'x' to [{x}]")
    print ("------  Klasa   ComplexNew  ---------------")
    x = k.ComplexNew(5,8)                # Tworzymy nowy obiekt x = 5 + 8*i
    y = k.ComplexNew(1,2)                # Tworzymy nowy obiekt y = 1 + 2*i
    # x.re=2  #--> Python zgłosi błąd "AttributeError: can't set attribute"
    print(f"Obiekt 'x' to [{x}]")
    print(f"Obiekt 'y' to [{y}]")
    z=x+y
    q=x*y
    print(f"Obiekt z=x+y to [{z}]") # Sprawdźmy wynik dodawania x+y
    print(f"Obiekt q=x*y to [{q}]") # Sprawdźmy wynik mnożenia x*y

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))