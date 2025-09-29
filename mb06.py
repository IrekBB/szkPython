
n = eval(input("ilość liczb do sumowania: "))
suma = 0
for j in range(n):
    liczba = eval(input("x="))
    suma = suma + liczba
print (f"Suma {n} - liczb wynosi {suma}.")


"""
suma = 0
i=1
while True:
    liczba = eval(input ("x="))
    suma = suma + liczba
    koniec = input("'koniec' - aby zakończyć: ")
    if koniec =="koniec":
        break
    i=i+1
print (f"Suma {i} - liczb wynosi {suma}.")
"""
