def main(args):
    zbiornik = {"żaba", "komar", "insekt"}
    print ("Zbiór: ", zbiornik)
    print("Spróbujmy dodać do zbiornika kolejną żabę...")
    zbiornik.add("żaba")
    print ("Aktualny stan zbiornika")
    print ("Zbiór: ", zbiornik)

    lista1 = [2,3,4,5,6,6,6,9,9,0]
    print("Budowanie zbioru na podstawie listy:", lista1)
    zbior2 = set(lista1)
    print ("Zbior 'zbior2' utworzony z 'lista1'=", zbior2)

    print ("Zbiory zawierajace elementy różnych typów:")
    kodHX = {0, 1, 2, 3 ,4, 5, 6,7 ,8,9, 'A','B','C','D','E','F'}
    print ("Dozwolone znaki kodu szesnastkowego:\n", kodHX)
if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))