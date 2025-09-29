def rozklad_czyn_perwsze(n):
    L=[]
    k=2  # pierwsza liczba pierwsza
    while n>1:
        while n%k==0:
            L.append(k)
            n=n/k
        k=k+1
    return L


            
