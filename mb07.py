p = eval(input("p="))
q = eval(input("q="))

potega = 1
for i in range(q):
    potega = potega * p

print (f"{p}^{q} = {potega}")
