def main(args):
    dozwolone = [1, 2, 3]
    v = None
    if v==None:
        try:
            v = int(input("Podaj wartość: "))
            print ("odebrano: ", v)
        except EOFError:
            print ("... Wykryto CRL+D, ustawiam 'v' = 3")
            v=3
    if v in dozwolone:
        print("OK!")
    else:
        print ("Poza zakresem wartości dozwolonych")    

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
"""
Popularne wbudowane wyjątki:
ValueError: Zgłaszany, gdy funkcja otrzymuje argument lub dane wejściowe niewłaściwego typu lub w niewłaściwej formie. 
TypeError: Występuje, gdy operacja lub funkcja jest stosowana do obiektu niewłaściwego typu, np. próba dodania stringa i liczby. 
KeyError: Jest zgłaszany, gdy próbujesz uzyskać dostęp do klucza, który nie istnieje w słowniku. 
ZeroDivisionError: Pojawia się podczas próby dzielenia przez zero. 
NameError: Występuje, gdy używasz niezdefiniowanej zmiennej lub funkcji. 
IndexError: Zgłaszany, gdy próbujesz uzyskać dostęp do indeksu, który jest poza zakresem listy. 
SyntaxError: Zgłaszany, gdy składnia kodu jest niepoprawna. 
IndentationError: Zgłaszany, gdy występują błędy w wcięciach kodu. 
ArithmeticError: Klasa bazowa obsługująca błędy arytmetyczne, np. OverFlowError, ZeroDivisionError, FloatingPointError
Exception: Obsługuje wszystkie pozostałe wyjątki niekończące się wyjściem do systemu oraz wyjątki zdefiniowane przez programistę\
EOFError: Wyjatek zgłasany, gdy podczas próby ppobierania danych napotkano na koniec pliku (end of file) bez faktycznego pobrania
          danych
FloatimingPointError: Błąd oblliczeń zmienno pozycyjnych
IndentationError: Błędne wcięcie kodu
ImportError: importowany moduł nie istnieje
KeyboardInterrupt: Użytkownik wcisnął CTRL+C, CTRL+Z lub Del
MemoryError: Przepełnienie pamięci (ale nie krytyczne)
OverflowError: Zbyt wielka wartość wartości całkowitej powodująca niemożnmość wyświetlenia lub konwersji
RuntimeError: Błąd wystepujący podczas uruchamiania programu
SyntaxError: Błąd składni
SystemError: Niekrytyczny błąd systemowy
TabError: Błędne użycie tabulatora lub spacji w kodzie
TypeError: Błędny typ(próba użycia metody lub funkcji na obiekcie innego typu). Pojawia się także gdy jako parametr wywołania wstawimy wartość złego typu
"""