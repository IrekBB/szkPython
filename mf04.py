'''
L=[123,56,90.00,11,23,100,78.12]
sum = 0
for e in L:
    sum = sum + e
print (L)   
print (f"Suma elementów listy wynosi: {sum}")

max = L[0]
for e in L:
    if e>max:max=e
print (f"Maksymalny element listy to {max}.")
'''

L=[12,90,1,2,3,4,5,6,7,8]
# operator modulo % : 6%2=0, 7%2=1
P=[]
N=[]
for e in L:
    if e%2==0:
        P.append(e)
    else: N.append(e)
print (P)
print(N)
