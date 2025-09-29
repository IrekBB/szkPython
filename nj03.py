'''
L = [10,1,3,4,6,7,11,101,7,9]
# % - modulo
LP=[]
LNP=[]
sumap=0
sumanp=0
for e in L:
    if e%2==0:
        sumap=sumap+e
        LP.append(e)
    else:
        LNP.append(e)
        sumanp=sumanp+e

print (f"parysta: {LP}; suma elementów: {sumap}")
print (f"nieparysta: {LNP}; suma elementów: {sumanp}")
'''
print ("Parametry trójmianu kwadratowego:")
a = eval(input("a="))
b = eval(input("b="))
c = eval(input("c="))

#delta
delta = b**2-4*a*c
if delta>0:
    import math
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print(f"x1={x1}, x2={x2}")
elif delta==0:
    x0=-b/(2*a)
    print (f"x0={x0}")
else:
    print ("Brak rozwiazań")
