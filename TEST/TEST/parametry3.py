import sys
import argparse  # parser argumentów 


def main(args):
    parser = argparse.ArgumentParser(description='Odczyt parametrów w wersji PRO')
    # argumenty obowiązkowe
    parser.add_argument('timing1', help="Opóźnienie wywołania modułu I/O")
    parser.add_argument('timing2', help="Maksymalne opóźnienie odczytu rekordów z bazy danych")
    parser.add_argument('limit', help="Limit ilości wykonania pętli odczytu", type=int) # określenie poprawności wartości parametru type=int
    # argumenty opcjonalne
    parser.add_argument('-n','--przebiegi', help="Opcjonalny argument typu int z wartością domyślną 5", type=int, default=5, required=False)
    # wywołanie w wersji krótkiej np.: -n 77
    # wywołanie w wersji rozszerzonej np.: --przebiegi 77
    argumenty = parser.parse_args() # Odczyt
    print ("timing1 (Opóźnienie wywołania modułu I/O:", argumenty.timing1)
    print ("timing2 (Maksymalne opóźnienie odczytu rekordów z bazy danych:", argumenty.timing2)
    print ("limit (Limit ilości wykonania pętli odczytu):", argumenty.limit)
    print ("przebiegi (Opcjonalny argument typu int z wartością domyślną 5):", argumenty.przebiegi)




if __name__ == "__main__":
    sys.exit(main(sys.argv))