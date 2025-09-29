L=[210,22,90,-90,123,4,5,6,7,89,9123,78,1,0,90,512]

def sort_bable():
    for i in range(len(L)):
        for j in range(1,len(L)-i):
            if L[j-1]>L[j]:
                L[j-1],L[j] = L[j],L[j-1]
'''
sort_bable()
print(L)
'''

L=[210,22,90,-90,123,4,5,6,7,89,9123,78,1,0,90,512]
def sort_selection():
    for i in range(len(L)-1):
        index_minimalnego=i
        for j in range(i+1,len(L)):
            if L[j]<L[index_minimalnego]: index_minimalnego=j
        L[i],L[index_minimalnego] = L[index_minimalnego],L[i]

'''
sort_selection()
print(L)      
'''
def sort_insert():
    for  i in range(1,len(L)): #zaczynamy od drugiego elementu
        pom = L[i]
        j=i-1
        while j>=0 and L[j]>pom: #przesuwanie elementów większych od pom
            L[j+1] = L[j]
            j=j-1
        L[j+1] = pom
'''
sort_insert()
print(L)          
'''
