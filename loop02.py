n = eval(input("Podaj ilość liczb, które sumujesz? "))
suma=0
for i in range(n):
    liczba = eval(input("Podaj liczbę: "))
    suma = suma + liczba

print (f"Suma liczb wynosi: {suma}")
srednia = suma/n
print (f"Srednia liczb wynosi: {srednia}")
