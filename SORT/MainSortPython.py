def main(args):
    oryginalna = [4, 6, 8, 2, 12, 7, 0]
    print ("Lista oryginalna=", oryginalna)
    oryginalna.sort()    # sortowanie w miejscu
    print ("Efekt sortowania w miejscu=", oryginalna) 
    oryginalna.append(5)
    print ("Sortowanie wsteczne=", sorted (oryginalna, reverse = True))
    print ("Zmodyfikowana lista posortowana prz pomocy sorted(): ", sorted(oryginalna))
    print ("*** \nSortujemy bardziej złożone obiekty\n ***")
    lokaty =  [
        ['20.02.2022', 'Morawski', 5000], ['22.02.2022', 'Blady', 5500],
        ['23.02.2022', 'Lukaszewski', 5500], ['12.01.2022', 'Nowak', 2200],
        ['15.04.2022', 'Pankracy', 6700], ['15.04.2022', 'Witos', 2050],
    ]
    print ("Lokaty nieposortowane")
    print(lokaty)
    print("Lokaty posortowane według nazwiska")
    print(sorted(lokaty, key=lambda x : x[1]))

    print ("\nKursy walut (nieposortowane)")
    kursywalut = [
        {'waluta': 'EUR', 'data': "15.04.2022", 'kurs': 4.99},
        {'waluta': 'EUR', 'data': "16.04.2022", 'kurs': 5.05},
        {'waluta': 'USD', 'data': "15.05.2022", 'kurs': 3.95},
        {'waluta': 'Rubel', 'data': "18.03.2022", 'kurs': 0.01},
    ]
    print ("Kursy walut posortowane według wartości:")
    print (sorted(kursywalut, key = lambda x: x.get("kurs")))
    


if __name__ == "__main__":
    import  sys
    sys.exit(main(sys.argv))