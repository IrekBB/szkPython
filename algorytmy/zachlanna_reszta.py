# https://www.youtube.com/watch?v=YiX0G1MgbyU
Nominaly=[500,200,100,50,20,10]


def zachariasz(reszta):
    K=[]
    i=0
    while reszta>0:
        K.append (reszta // Nominaly[i])
        reszta = reszta%Nominaly[i]
        i=i+1
    return K

L=zachariasz(790)
for i in range(len(L)):
    if L[i]!=0:
        print(Nominaly[i],"=>",L[i])
    
