slownikBledow = {
    '400': "Bad Request",
    # '401' : 'Unauthorized'  # świadomie pominięty
    '408': 'Request Timeout',
    '410': 'Gone',
    '413': 'Request Entity Too Large',
    '415': 'Unsupported Media Type',
    '414': 'RequestURI Too Long',
    '422': 'Unprocessable entity',
    '425': 'Too Early',
    '429': 'Too Many Requests',
    '431': 'Request header Fields Too Large',
}

def main(args):
    wyniki_surowe=list()
    wyniki_surowe.append(list())  #Seria 1
    wyniki_surowe.append(list())  #seria 2
    wyniki_surowe.append(list())  #seria 3
    wyniki_surowe[0] = ["400", "401", "401", "401","401", "410", "410","425","400", "429", "431", "431", "400", "431","413","414","425","401",\
        "410","410","401","408","408","408","400","400","400"]
    wyniki_surowe[1] = ["408", "408", "408","400","401", "401", "410", "425", "400", "429", "431","431","415","408","408","400", "425", "401", \
        "410", "410", "401", "408","408","408", "422", "400", "400"]
    wyniki_surowe[2] = ["400", "400","401", "401","401","400","400","425","400"]

    print ("Wszystkie wyniki serii 1: ", wyniki_surowe[0])
    print ("Wszystkie wyniki serii 2: ", wyniki_surowe[1])
    print ("Wszystkie wyniki serii 3: ", wyniki_surowe[1])

    # Tabel zawierająca otrzymane kody błędów z trech serii pomiarowych przekształcone na  zbiory
    wyniki_zbiory=list()
    wyniki_zbiory.append(set(wyniki_surowe[0]))
    wyniki_zbiory.append(set(wyniki_surowe[1]))
    wyniki_zbiory.append(set(wyniki_surowe[2]))

    print ("Znormalizowana lista wyników (bez duplikatów)")
    print ("  Seria 1:", wyniki_zbiory[0])
    print ("  Seria 2:", wyniki_zbiory[1])
    print ("  Seria 3:", wyniki_zbiory[2])

    # A teraz analiza danych
    print ("Lista wszystkich wykrytych błędów:")
    wszystkie = wyniki_zbiory[0] | wyniki_zbiory[1] | wyniki_zbiory[2]
    for kod in wszystkie:
        print (kod,"  ", slownikBledow.get(kod, "Nieznany kod błędu!"))
    print ("Te same kody błędów wykryte w każdej z serii")
    wspolne = wyniki_zbiory[0] & wyniki_zbiory[1] & wyniki_zbiory[2]
    for kod in wspolne:
        print(kod,"  ", slownikBledow.get(kod, "Nieznany kod błędu!"))
    
    
    
    
    
    
    """
    Zbiory tworzone na podstawie wyrażeń:
    x1 = [-4, -2, -2, 0, 1, 2, 4]
    x2 = {n*n for n in x1}
    print (x2)   # {16, 1, 4, 0}
    """




if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))