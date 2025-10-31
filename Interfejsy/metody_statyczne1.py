"""
Statyczne metody klasy w Pythonie to funkcje należące do klasy, ale niezwiązane z konkretną
 instancją obiektu. Używają dekoratora @staticmethod i nie otrzymują automatycznie self ani 
 cls jako pierwszego argumentu. Służą jako funkcje narzędziowe, które można wywołać bezpośrednio
przez nazwę klasy, np. MojaKlasa.moja_metoda_statyczna(). 

*** Niezależność od stanu: Metody statyczne nie mają dostępu do stanu klasy ani instancji, 
    co oznacza, że nie mogą modyfikować atrybutów klasy ani jej instancji.

*** Funkcje narzędziowe: Są idealne do grupowania funkcji, które są logicznie powiązane z klasą,
    ale nie muszą operować na jej danych, np. funkcja pomocnicza do obliczeń matematycznych 

*** Wywołanie: Można je wywoływać bezpośrednio z poziomu klasy, bez konieczności tworzenia obiektu.

*** Definicja: Do zdefiniowania metody statycznej używa się dekoratora @staticmethod. 

"""
class NarzedziaMatematyczne:
    # @staticmethod jest używany, gdy chcemy tworzyć metody, które są związane z klasą,
    # ale nie potrzebują dostępu ani do atrybutów klasy ani do instancji.
    @staticmethod 
    def podnies_do_potegi(x, n):
        return x ** n

def main(args):
    liczba = 2
    wykladnik = 3
    wynik = NarzedziaMatematyczne.podnies_do_potegi(liczba, wykladnik)  
    print(liczba, "do potęgi", wykladnik, "to:", wynik)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))


