L=[]
L.append("Natalia")
L.append("Małgorzata")
print (L)
L.append(24.56)
print (L)
K=[123, 67.67, "znaki","c","1",True]
print (K)
K.append(100)
print(K)

print(K[6])
print (len(K))
print(f" index ostatniego elementu to {len(K)-1}.")

for i in range(len(K)):
    print(K[i], end="####")
print()
for element in K:
    print(element,end=" ")
