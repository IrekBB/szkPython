# zmiany układu i rozmiaru tablic NumPy
def main(args):
    # zmiana układu i rozmiaru tablic NumPy
    t1 = np.arange(1,11)
    print ("t1=\n", t1)
    t1=t1.reshape((2,5))  # Zmiana kształtu z 1D na 2D (2x5)
    print ("t1=\n", t1)
    t8 = np.arange(1,11)
    print ("t8=\n", t8)
    t8.resize(4,5)  # Rozszerzenie z 10 elementów na 4x5, czyli 20, puste miejsca uzupełnione 0
    print ("po resize: t8=\n", t8)
    t = np.array([[-2,1,7], [4,-5,9], [2,0,3]])
    print("t=\n", t)
    # metoda ravel - spłaszczanie wierszami lub kolumnami
    print("Spłaszczanie wierszami t=\n ",t.ravel(order='C'))
    print("Spłaszczanie kolumnami t=\n ",t.ravel(order='F'))
if __name__=="__main__":
    import sys
    import numpy as np
    sys.exit(main(sys.argv))