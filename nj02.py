"""
import math

x = eval(input("x="))
y= eval(input("y="))
r= eval(input("r="))

P=[]
P.append(x)
P.append(y)

l = math.sqrt(P[0]**2 + P[1]**2)

if l<=r:
    print (f"Punkt P({P[0]},{P[1]}) należy do koła o promieniu {r}.")
else:
    print (f"Punkt P({P[0]},{P[1]}) nie należy do koła o promieniu {r}.")
"""
p = eval(input("p="))
q = eval(input("q="))

potega=1
for i in range(q):
    potega = potega * p

print (f"potega: {potega}")
