import sys

def main(args):
    print (f"Nazwa pliku: {args[0]}")                     # tablica pythona sys.argv, tu main pobiera ją jako argument sys
    print ("Liczba parametrów: ",len(args)-1)
    lista_parametrow = args[1:]
    print ("Lista parametrów: ", lista_parametrow)

    for x in range(len(lista_parametrow)):
        print(f"Parametr nr {x+1}: {lista_parametrow[x]}" )
    
    print ("Ścieżka interpretera Pythona:", sys.executable)

if __name__ == "__main__":
    sys.exit(main(sys.argv))