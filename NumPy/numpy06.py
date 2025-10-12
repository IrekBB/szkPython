# Zmiany układu i rozmiaru taqblic NumPy
def main(args):
    t1 = np.arange(1,11)
    print (t1.shape)   # Powinno zwrócić domyślny "kształt" tablicy (2,5)
    print ("t1=",t1)
    t1 = t1.reshape( (2,5) ) # Zmiana kształtu z 1D na 2D (konkretnie 2x5). Uwaga! Zwraca tablicę z identyczną zawartością
    print("t1 po reshapingu: ")
    print(t1)
    t8 = np.arange(1,11)
    print("t8= ", t8)
    t8.resize(4,5)   # Rozszerzenie z 10 elementów na 4x5, czyli 20
    print("t8 po resize (4,5): ")   # Przy zmianie rozmiaru wypełni puste miejsca zerami
    print(t8) 
    # ravel() metoda przeciwna do reshape(), spłaszca N-wymiarową tablicę NumPy
    t = np.array ([ [-2,1,7], [4, -5, 9], [2, 0, 3] ]) 
    print(t)
    print("Spłaszczanie wierszami: ", t.ravel(order='C'))  # Tryb domyślny, parametr można ominąć
    print("Spłaszczanie kolumnami: ", t.ravel(order='F'))  
    

if __name__=="__main__":
    import numpy as np
    import sys
    sys.exit(main(sys.argv))