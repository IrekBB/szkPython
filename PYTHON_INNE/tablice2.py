N = 5
M = 3
t1 = [0] * N                # Deklarujemy tablicę o rozmiarze N=5, wypełnioną zerami
t2 = [i for i in range(N)]  # Deklarujemy tablicę o rozmiarze N=5, wypełnioną wartościami 0,1,2,3,4

# Deklarujemy tablicę t3 o rozmiarze NxM, wypełnioną zerami:

t3 = [0] * N
t3 = [ [0] * N for i in range(M) ] # Inicjalizacja drugiego wymiaru tablicy N x M
                                   # Ten sam efekt w jednej linijce: t3 = [[0]*N for i in range(M)]

# Wpisujemy coś do wybranych komórek
t3[1][1] = 8
t3[2][2] = 9
print("t1=", t1)
print("t2=", t2)
print("t3=", t3)

"""
t3= [
     [0, 0, 0, 0, 0], 
     [0, 8, 0, 0, 0], 
     [0, 0, 9, 0, 0]]

tak: t3 = [ [0] * N for i in range(M) ]
ale NIE!!!!: t3 = M * [[0] *N]

Python np. przy próbie użycia t3[1][1] = 8
                              t3[2][2] = 9 
Utworzy w pamięci taki dziwoląg:
t3= [
     [0, 8, 9, 0, 0], 
     [0, 8, 9, 0, 0], 
     [0, 8, 9, 0, 0]]

Okazuje się bowiem, że operator * w Pythonie nie tworzy faktycznej kopii
tablicy w kolejnych wierszach, tylko buduje referencje do tegon samego
wiersza. Musimy tworząc tablicę o wymiarach N*M jawnie utworzyć nowe 
podlisty symulujące wiersze tablicy, jak uczyniono to w linii 9 i 25.

"""