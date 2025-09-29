L=[1,100,-9,0,23,14,18,19,-2,-9,-9,100,87]
def min():
    min=L[0]
    for i in range(len(L)):
        if min>L[i]: min = L[i]

    return min

def max():
    max=L[0]
    for i in range(len(L)):
        if max<L[i]: max = L[i]

    return max



