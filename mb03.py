while True:
    dzien = input("Podaj dzień tygodnia: ")
    if dzien=="poniedziałek":
        print("1. 1400 - 1600 Idę do kina")
        print("2. 1800 - 2000 Korki z Fizyki ")
    elif dzien=="wtorek":
        print("1. 1200 - 1300 Idę na narty")
        print("2. 1300 - 1500  Maluję ")

    else:
        if dzien=="zakończ":
            break
        else:
            print (f"loop.pywybór to: poniedziałek,...,niedziela")



'''
liczba = int(input("podaj liczbę całkowitą: "))
if liczba%2==0:
    print (f"{liczba} jest parzysta")
else:
    print (f"{liczba} jest nieparzysta")
'''    
