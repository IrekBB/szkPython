import sys

# Czy można napisać funkcję, która przyjmuje dowolną ilość parametrów (pozycyjnych lub nazwanych)?
# Zabiegu takiego można dokonać w sposób dualny do rozpakowywania argumentów: 
# przez pakowanie argumentów do krotek i słowników, używając wyrażeń z gwiazdką (lub dwoma) w definicji funkcji:

def f(a, b, *args):
    print(a, b, args)

# Podobnie, dowolnie nazwane argumenty nazwane można przechwycić do słownika przez podanie parametru z dwoma gwiazdkami:
def g(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

def test(*args, **kwargs):    # dowolna ilość argumentów pozycyjnych i nazwanych
    for arg in args:
        print('argument:', arg)
    for k, v in kwargs.items():
        print('keyword argument', k, '=', v)

# następująca funkcja duplikuje funkcjonalność print, ale dodając prefiks do każdej wypisywanej treści:
def new_print(*args, **kwargs):
    print(">>>", *args, **kwargs)

def main(args):
    print ("***   Pakowanie argumentów   ***")
    # Wystąpienie parametru pozycyjnego poprzedzonego gwiazdką prowadzi do przechwycenia wszystkich
    # argumentów pozycyjnych, które nie są przechwytywane przez parametry podane przed wystąpieniem
    #  tego parametru z gwiazdką (tutaj: a i b). Parametr args staje się krotką, zawierającą wszystkie
    #  te dodatkowe argumenty. Parametry a i b są obowiązkowe, zatem tak zdefiniowana f przyjmuje dowolną
    #  ilość argumentów pozycyjnych większą niż 1. Parametr z gwiazdką musi wystąpić jako ostatni parametr pozycyjny.
    f(1, 2, 3, 4, 5)   
    
    print ("***   Pakowanie argumentów dla argumentów nazwanych   ***")
    g(10, 20, x=10, y=20, z=30)  # 10 20 () {'x': 10, 'y': 20, 'z': 30}
                                 # przekazaliśmy tylko dwa argumenty pozycyjne - w konsekwencji krotka args jest długości 0.
    test(10, 20, x=10, y=20, tower='Eiffel')

    new_print('a', 'b', end='XX\n')


if __name__=="__main__":
    sys.exit(main(sys.argv))