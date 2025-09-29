'''
dzielna = eval(input("podaj dzielną: "))
dzielnik = eval(input("podaj dzielnik: "))


if dzielnik==0:
    print ("Error: Błąd dzielenie przez 0.")
else:
    print (dzielna/dzielnik)
'''
dzien = input("podaj dzień tygodnia: ")
# or - lub; and - i
if dzien=="poniedziałek" or dzien=="Poniedziałek":
    print ("1. Idę na basen")
    print ("2. czytam książkę")
elif dzien=="wtorek":
    print ("1. Idę na zakupy")
    print ("2. Kurs Judo")
elif dzien=="środa":
    print ("1. Idę na sanki")
    print ("2. Kurs tańca")
    
else:
    print ("Wprowadź dzień tygodnia, np. poniedziałek")
