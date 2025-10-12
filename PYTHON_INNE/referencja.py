def referencja():
    mojNapis ="Cześć"
    mojNapis2=mojNapis
    print ("mojNapis =", mojNapis)
    print ("mojNapis2 =", mojNapis2)
    print ("adres mojNapis ", id(mojNapis))
    print ("adres mojNapis2 ", id(mojNapis2))
    print ("Drugi znak ciągu mojNapis:", mojNapis[1])
    mojNapis2 = mojNapis[1] + mojNapis2
    print ("mojNapis =", mojNapis, "czyli: mojNapis")
    print ("mojNapis2 =", mojNapis2, "czyli: mojNapis[1]+mojNapis2")
    print ("Adres starego obiektu mojNapis= ", id(mojNapis))
    print ("Adres nowego obiektu mojNapis2= ", id(mojNapis2))


def main(args):
    referencja()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
