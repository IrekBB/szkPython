def trzy_tablice(X,Y,Z):
    licznik = 0
    for x in X:
        for y in Y:
            for z in Z:
                licznik+=1
                if x==y==z:
                    print ("Znalazłem elemet wspólny:",x)
    print ("Liczba operacji:", licznik)

def main(args):
    X = [2,3,5,6,7]
    Y = [5, 5, "sss", 1, 6, 'A', 12]
    Z = ["kot", 4, 5, 6 ]
    trzy_tablice(X,Y,Z)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
