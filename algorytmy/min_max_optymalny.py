# technika dziel i zwyciężaj
L=[1,23,56,7,8,-1,0,1000,-100,100,67,90,8,90,8,67,-200000]
MIN=[]
MAX=[]

def min_max():
    if len(L)==0:
        print('\nZbiór pusty')
        return 0
    elif len(L)==1:
        print ('\nZbiór jednoelementowy')
        return L[0]
    else:
        if len(L)%2==0:
            for i in range(1,len(L)):
                if L[i]>L[i-1]:
                    MIN.append(L[i-1])
                    MAX.append(L[i])
                else:
                    MIN.append(L[i])
                    MAX.append(L[i-1])
            return min(MIN), max(MAX)
        else:
            for i in range(1,len(L)-1):
                if L[i]>L[i-1]:
                    MIN.append(L[i-1])
                    MAX.append(L[i])
                else:
                    MIN.append(L[i])
                    MAX.append(L[i-1])
            if min(MIN)>L[len(L)-1]:
                return L[len(L)-1],max(MAX)
            elif max(MIN)<L[len(L)-1]:
                return min(MIN),L[len(L)-1]
            
print(min_max())
    
