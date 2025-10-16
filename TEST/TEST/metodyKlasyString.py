def main(args):
    napis = "M e N u"
    print (napis.center(50,"*"))   # napis wyśrodkowany, domyślne spacje wypełnione *
    print (napis.lower().center(50,"*"))  # napis małymi literami
    print (napis.upper().center(50,"*"))  # napis duzymi literami
    print (napis.ljust(50,"*"))  # napis wyrównany do lewej
    print (napis.rjust(50,"*"))  # napis wyrównany do prawej
    s = "      Programujemy w Python"
    print (s.lstrip())  # Usuwa spacje z lewej strony napisu
    s = "******    Programujemy w Python"
    print(s)
    print (s.lstrip("*"))  # Usuwamy wyłącznie gwiazdki
    s = "     Programujemy w Python    **********"
    print (s)
    print (s.rstrip("*"))  # usuwa gwiazdki z prawej strony (domyslnie spacje)
    s = "     M E N U     "
    print(s)
    print (s.strip()) # usuwa spacje z tyłu i z przodu
    s= "$$$$$$$$$   MENU   $$$$$$$$$"
    print(s)
    print(s.strip("$"))   # usuwa znaki $ z przodu i z tyłu
    print (napis)
    print (napis.swapcase())  # Zamienia duże litery na małe i na odwrót
    napis = napis.swapcase()
    napis = "Alicja w krainie czarów"
    print(napis)
    print (napis.title()) # Każde słowo zaczyna sie z dużej litery

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))