"""
Sortowanie przez scalanie
+ Dzielimy N-elementowy ciąg na dwa podciągi po N/2 elementów każdy
+ Sortujemy za pomocą metody przez scalanie każdy z podciągów osobno
+ Łączymy posortowane podciągi w jeden posortowany ciąg  
"""
def scalaj (T1, left, mid, right):   # Scalanie podtablic
    # left - poczatek
    # right - koniec
    # mid - środek
    
    # Procedura łaczy dwie posortowane tablice T1[left...mid] i T1[mid+1...right]
    left1 = left          # Podtablica 1
    right1 = mid
    left2 = mid+1         # Podtablica 2
    right2 = right

    T2 = [None] * len(T1)  # T2 tablica pomocnicza
    i = left1

    # Aż o wyczerpania obu podtablic scal za pomocą tablicy pomcniczej
    while ((left1 <= right1) and (left2 <= right2)):
        if T1[left1] < T1[left2]:
            T2[i] = T1[left1]
            left1 = left1 + 1
        else:
            T2[i] = T1[left2]
            left2 = left2 + 1
        i = i + 1
    while left1 <= right1:
        T2[i] = T1[left1]
        left1 = left1 + 1
        i = i +1
    
    while left2 <= right2:
        T2[i] = T1[left2]
        left2 = left2 + 1
        i = i + 1
    
    for i in range(left, right+1):
        T1[i] = T2[i]

def MergeSort(T, left, right):   # Sortowanie przez scalanie - MergeSort
    if left < right:
        mid = (left + right) // 2   # Środek
        MergeSort(T, left, mid)     # Sortowanie podtablic lewej i prawej
        MergeSort(T, mid+1, right)  # Sortuj prawą połowę
        scalaj(T, left, mid, right)
        
def usunK (L):
    K = list()
    for e in L:
        K.append(int(e.replace("\n","")))
    return K

def pisz(L, s):
    print (s)
    for e in L:
        print (e, end = " ")
    print()    

def main(args):
    katalogBiezacy = pathlib.Path.cwd()
    scdostp02 = pathlib.PureWindowsPath(katalogBiezacy,"MojePliki","input02.txt")

    try:
        with open(scdostp02) as f2:
            KB= list()
            for line in f2.readlines():
                KB.extend(line.split(",")) 
    except FileNotFoundError:
        print (f"Nie odnaleziono pliku {scdostp02}")
    
    KB = usunK(KB)
    pisz (KB, "Zawarość pliku przed posortowaniem: ")
    MergeSort (KB, 0, len(KB)-1)
    pisz (KB, "Zawarość pliku po posortowaniem: ")
    
    

if __name__ == "__main__":
    import sys
    import pathlib
    sys.exit(main(sys.argv))