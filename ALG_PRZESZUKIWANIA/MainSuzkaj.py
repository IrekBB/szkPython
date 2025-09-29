def main(args):
    tab0=[]
    tab1 = [1,2,"Ala", 3, -7, 44, 'C', 1, 0, -3]
    tab2 = ['A', 'L', 'A', 'M', 'A', 'K', 'O', 'T', 'A' ]
    print ("tab0: ", tab0, " Rozmiar: ", len(tab0) )
    print ("Szukam 3: ", s.szukaj(tab0,3) != len(tab0))
    print ("tab1: ", tab1, " Rozmiar: ", len(tab1) )
    print ("Szukam 3: ", s.szukaj(tab1,3) != len(tab1))
    print ("Szukam 99: ", s.szukaj(tab1,99) != len(tab1))
    



if __name__=="__main__":
    from MojeTypy import szukaj as s
    import sys
    sys.exit(main(sys.argv))
    