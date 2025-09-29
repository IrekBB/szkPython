'''
for i in range(10):
    print (f"{i} - witaj Monika!")
print ("------------------------------")
for licznik in range(2,12,2):
    print (f"{licznik} - witaj Monika!")
'''

L = ["ala","a","z",123, 123.123, True]
print (L[0])
print (L[1])
print (L[5])
K=[1,2,3,4,33,456,678,123,333,4444,9,900]
n = len(K) - 1  # len zwraca ilość elementów na liście
print (K[n])
print (K[len(K)-1])
K.append(100) #dodawanie lemetów na końcu listy
print (K)

for i in range(len(K)):
    print (K[i], end="|")
print()
for i in range(len(L)):
    print (L[i], end=" ")

for element_listy in L:
    print (element_listy)
