import math
x = eval(input("x="))
y = eval(input("y="))
r= eval(input("r="))

l= math.sqrt(x**2 + y**2)
if l <= r:
    print (f"P({x},{y}) należy do koła o promieniu {r}.")
else:
    print (f"P({x},{y}) nie należy do koła o promieniu {r}.")
