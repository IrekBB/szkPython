def usunK (L):
    K = list()
    for e in L:
        K.append(int(e.replace("\n"," ")))
    return K

def scalaj(T1, T2):
    N = len(T1)
    M = len(T2)
    T3 = [None] * (N+M)
    i, j, k = 0, 0, 0
    while i < N and j < M:
        if T1[i] < T2[j]:
            T3[k] = T1[i]
            k, i = k + 1, i + 1
        else:
            T3[k] = T2[j]
            k, j = k + 1, j + 1
    while i < N:
        T3[k] = T1[i]
        k, i = k + 1, i + 1
    
    while j < M:
        T3[k] = T2[j]
        k, j = k + 1, j + 1
    
    return T3

def pisz(L, s):
    print (s)
    for e in L:
        print (e, end = " ")
    print()    

def main(args):
    katalogBiezacy = pathlib.Path.cwd()
    scdostp01 = pathlib.PureWindowsPath(katalogBiezacy,"MojePliki","input01.txt")
    scdostp02 = pathlib.PureWindowsPath(katalogBiezacy,"MojePliki","input02.txt")
    
    try:
        with open(scdostp01) as f1:
            L=list()
            for line in f1:
                L.extend(line.split(","))
    except FileNotFoundError:
        print (f"Nie odnaleziono pliku {scdostp01}")            

    try:
        with open(scdostp02) as f2:
            K= list()
            for line in f2.readlines():
                K.extend(line.split(",")) 
    except FileNotFoundError:
        print (f"Nie odnaleziono pliku {scdostp02}")
    
  
    print ("Zbiory do scalenia:")
    KL = usunK(L)
    KL.sort()
    pisz (KL, "L: ")
    KK = usunK(K)
    KK.sort()
    pisz (KK, "K: ")
    T = scalaj(KL, KK)
    print()
    pisz(T, "Tablica po scaleniu K i L:")

    

    
if __name__ == "__main__":
    import sys
    import pathlib
    sys.exit(main(sys.argv))