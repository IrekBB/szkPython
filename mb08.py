# Lista liczb całkowitych
L=[1,2,100,3,89,91,1000]

#operator modulo: % wyznacza on resztę z dzielenia całkowitego, np. 4%2=0; 5%2=1
LP=[]  # pusta lista przeznaczona dla liczb parzystych
for el in L:
    if el%2==0:
        LP.append(el)

print (LP)

'''
1. Zadanie 1.
Operając się na powyższym przykładzie utwórz listę liczb nieparzystych

2. Zadanie 2
Oblicz sumę liczb parzystych i liczb nieparzystych z listy L


3. Zadanie 3
Wyznacz element maksymalny i minimalny listy L (w jednym programie).
'''
