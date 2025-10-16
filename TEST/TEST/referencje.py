def main(args):
    mojNapis="Napis"
    mojNapis2 = mojNapis
    print("adres mojNapis=", id(mojNapis))
    print("adres mojNapis2=", id(mojNapis2))
    print ("Wynik porównania 'mojNapis is mojNapis2':  ", mojNapis is mojNapis2)
    mojNapis2 = mojNapis[0] + mojNapis2
    print('mojNapis =', mojNapis)
    print('mojNapis2 =', mojNapis2)
    print('adres mojNapis =', id(mojNapis))
    print('adres mojNapis2 =', id(mojNapis2))


if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))