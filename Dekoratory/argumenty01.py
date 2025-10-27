import sys

def f(a, b, c):
    print(a, b, c)

def g(a, b, c, d, e):
    print(a, b, c, d, e)

def main(args):
    print("---   Zwykłe parametry   ----")
    x = 1
    y = 2
    z = 3
    f(x, y, z)
    print ("---   Parametry przez krotkę -----")
    t = (3, 4, 5)   # KROTKA
    x, y, z = t
    f(x, y, z)
    # Istnieje sposób, aby przekazać obiekty z dowolnej krotki (ogólniej: obiektu iterowalnego) 
    # jako kolejne argumenty pozycyjne, używając wyrażeń z gwiazdką 
    print ("--- Wyrażenie z gwiazdką ---")
    s = (9, 10, 11)
    f(*s)
    # Wyrażenie *t powoduje "rozpakowanie" zawartości t w miejsce tylu argumentów, ile wynosi długość t
    t = (1, 2)
    g(*t, 3, 4, 5)
    g(1, *[2, 3, 4], 5) # lista zamiast krotki
    g(*(1, 2, 3), *(4, 5)) # dwie krotki


if __name__=="__main__":
    sys.exit(main(sys.argv))
