import math
def is_perfect(n):
    suma = 1  # 1 jest zawsze dzielnikiem
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            suma = suma + i + n/i  # dodajemy od razu dwa dzielniki
        if n==int(math.sqrt(n))^2:    #liczba kwadratowa
            suma=suma-int(math.sqrt(n))   # dwa takie same dzielniki (pierwiastki)
    if n==suma:
            return True
    return False
