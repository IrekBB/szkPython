import sys
"""
Okazuje się, że konstrukcja z przykładu funkcjaDekorator2.py - definicja funkcji, po której następuje podmiana jej na 
wynik nałożenia funkcjonału na nią samą - jest na tyle przydatna, że doczekała się pewnego skrótu (przykład tak zwanego
lukru syntaktycznego, syntactic sugar - wprowadzonych dla wygody skrótowych reguł syntaktycznych):
"""



def main(args):
    
    def do_twice(func):
        def new_func():
            func()
            func()
        return new_func
    
    @do_twice
    def f():
        print('!')
    
    """
    Poprzedzenie definicji funkcji przez @ i nazwę dekoratora do_twice jest równoważne z konstrukcją z poprzedniego przykładu. 
    Pozwala to na zgrabny zapis, oznaczający, że funkcja ma zostać podmieniona.
    Funkcjonały, pojawiąjące się w takim kontekście nazywają się dekoratorami 
    (ściślej: dekoratorami funkcji). Ich celem jest rozszerzenie lub zmiana działania funkcji
    bez konieczności zmiany jej treści. Raz napisany dekorator można "zaaplikować" do dowolnej 
    funkcji o zgodnych parametrach - inaczej mówiąc, "udekorować" ją.
    """
    f()
    
if __name__ == "__main__": 
    main(sys.argv)