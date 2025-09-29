import math
epsilon = 0.000001

def pierwiastek (P):
    a,b=1,P
    while math.fabs(a-b)>=epsilon:
        a=(a+b)/2
        b=P/a
    return (a+b)/2

print(pierwiastek(3))
        
