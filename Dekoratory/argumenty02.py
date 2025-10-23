import sys

# przekazywania argumentów nazwanych

def h(a, b, c, x=10, y=20, z=30):
    print(a, b, c, x, y, z)

def main(args):
    print ("***    Przekazywanie argumentów nazwanych     ***")
    h(1, 2, 3)
    h(1, 2, 3, x=4, y=5)
    h(1, 2, 3, z=6, y=5)

# Ponieważ niektóre z parametrów funkcji są opcjonalne (nazwane), rozpakowywanie 
# ich z krotki nie byłoby wystarczające
# Zamiast tego, parametry można przekazać jako słownik, którego parami klucz-wartość są napisy nazywające parametry
#  i stowarzyszone z nimi wartości do przekazania. Takie stowarzyszenie nazw parametrów i ich wartości przekazuje się
#  przez wyrażenie z dwoma gwiazdkami:
    print ("***    Przekazywanie argumentów nazwanych przez słownik    ***")
    d = {'x': 100, 'y': 200}
    h(1, 2, 3, **d)
# Przekazywanie argumentów możemy dokonywać w dowolny sposób mieszając przekazywanie
#  ich explicite i przez wyrażenia z jedną lub dwoma gwiazdkami:
    print ("***    Przekazywanie argumentów mieszane     ***")
    h(*(1, 2), 3, z=5, **{'x': 'iks'})

    print ("*** Przekazywanie argumentów przez konstruktor słownika ****") 
    # Konstruowanie poprzez przekazywanie do zwykłego konstruktora dowolnych argumentów nazwanych. 
    # Napisy reprezentujące te argumenty stają się wtedy kluczami w słowniku z odpowiadającymi wartościami:
    d = dict(x='X', z='Z')
    h(1, 2, 3, **d)

if __name__=="__main__":
    sys.exit(main(sys.argv))