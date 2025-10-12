# metoda brute force
def szukaj(w, t):  # Konwencja: w - wzorzec, t - przeszukiwany tekst
    i, j = 0, 0
    M = len(w)
    N = len (t)
    while j<M and i<N:
        if t[i] != w[j]:    # Poziome przesuniecie wzorca
            i = i - (j-1)
            j = -1
        i = i + 1
        j = j + 1
    if j==M:
        return i - M
    else:
        return -1 
# Metoda KMP
shift = list()

def kmp(w, t):
    N = len(t)
    M = len(w)
    i,j = 0, 0
    while i<N and j<M:
        while j>=0 and t[i] != w[j]:
            j = shift[j]
        i = i + 1
        j = j + 1
    if j==M:
        return i - M
    else:
        return  -1
    
def init_shifts(w):
    M = len(w)
    global shift
    shift = [0] * len(w)
    shift[0] = -1
    i, j = 0, -1
    while i < M - 1:
        shift[i] = j
        while j >= 0 and w[i] != w[j]:
            j = shift[j]
        i = i + 1
        j = j + 1

K = 26 * 2 + 2 *2 + 1
shift_bm =  [0] * K

def indeks_bm(c):         # Konwersja znaku 'c' na indeksy tablicy
    if c==' ':
        return 0
    elif c=='ę':
        return 53
    elif c=='Ę':
        return 54
    elif c=='ł':
        return 55
    elif c=='Ł':
        return 56
    # itd., miejsce na kolejne znaki polskie
    elif (c>= 'a') and (c <= 'z'):
        return ord(c) - ord('a') + 1 # Od 1 do 25
    elif (c>='A') and ( c <= 'Z'):
        return ord(c) - ord('A') + 27 # Od 27 do 52
    else:
        print ("Błedny znak!")
        return -1

def init_shifts_bm(w):
    global shift_bm
    M = len(w)
    for i in range(K):
        shift_bm[i] = M
    for i in range(M):
        shift_bm[indeks_bm(w[i])] = M - i - 1

def bm(w,t):
    global shift_bm
    init_shifts_bm(w)
    N = len(t)
    M = len(w)
    i, j = M - 1, M -1
    while j >=0:
        while t[i] != w[j]:
            x = shift_bm[indeks_bm(t[i])]
            if M - j > x:
                i = i + M - j
            else:
                i = i + x
            if i >= N:
                return -1
        i = i -1
        j = j -1
    return i + 1

p = 33554393   # Duża liczba pierwsza
MAX = 64       # Liczba znaków alfabetu
def rk(w,t):
    Hw = 0    # Funkcja H dla wzorca
    Ht = 0    # Funkcja H dla tekstu
    M = len(w)
    N = len(t)
    bM_1 = 1
    for i in range(1, M):  # Wyliczymy wartość pow(MAx, M-1) % p
        bM_1 = (MAX*bM_1) % p
    for i in range(M):
        Hw = (Hw * MAX + indeks_bm(w[i])) % p   # Inicjacja funkcji H dla wzorca
        Ht = (Ht * MAX + indeks_bm(t[i])) % p   # Inicjacja funkcji H dla tekstu
    i=0
    while Hw != Ht:   # Przesuwanie się w tekście
        if i+M >= N:
            return -1  # Niepowodzenie poszukiwań
        else:
            Ht = (Ht + MAX * p - indeks_bm(t[i])*bM_1)%p 
            Ht = (Ht * MAX + indeks_bm(t[i+M]))%p
        i = i + 1
    return i

if __name__=="__main__":
    print("Wywołałes moduł! Testuj z poziomu pliku MainszukajTXT.py")