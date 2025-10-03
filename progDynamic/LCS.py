# Zmiana dla GITA
# FIT Test - zmiana w zawartości pliku
def LCS_dlugosc(X,  Y, C):   # Najdłuzsza wspólna podsekwencja
    M = len(X)
    N = len(Y)
    for i in range(M):
        C[i][0] = 0
    for i in range(N):
        C[0][i] == 0
    for i in range(1,M+1):
        for j in range(1, N+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                # max() zwracanych wartości z maksymalna z listy przekazanej jako argumenty
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C[M][N]

# Rekurencyjne przejście 'od tyłu' sladem decyzji podejmowanych przez algorytm
def LCS_wypisz(X, Y, C, i, j):  # W tej funkcji odtwarzamy ciąg LCS
    if (i==0) or (j==0):
        return ""
    if X[i-1] == Y[j-1]:
        return LCS_wypisz(X, Y,C, i-1, j-1) + X[i-1]
    else:
        if C[i][j-1] > C[i-1][j]:
            return LCS_wypisz(X, Y, C, i, j-1)
        else:
            return LCS_wypisz(X, Y, C, i-1, j)

def main(args):
    X="PKOYTEK"
    Y="MKJAIEOTI"
    M = len(X)
    N = len(Y)
    # Tablica długości LCS C[M+1][N=1]
    C =  [0] * (M+1)
    for i in range(M+1):
        C[i] = [0] * (N+1)
    print ("Napis X=", X + " npisY=", Y)
    print("LCS długość: ", LCS_dlugosc(X, Y, C))
    print("Wypisz LCS: ", LCS_wypisz(X, Y, C, M, N))

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
    
    
    
