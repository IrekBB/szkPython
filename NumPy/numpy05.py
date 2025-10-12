# Tworzenie tablic i wypełnianie ich pożądaną sekwncją

def main(args):
    t0 = np.linspace (0, 10, 5)  # Przedział od 0 do 10 podzilony na 5 wartości
    print ("t0 = ", t0)
    t1 = np.arange(1,11)  # Jednowymiarowa, typ domyślny, seria liczb od 1 do 10
    print ("t1 = ", t1)
    t2 = np.arange(1,11,3) # Jednowymiarowa, typ domyslny, seria liczb od 1 do 10, co 3
    print("t2 = ", t2)
    t3 = np.zeros(9)    # Jednowymiarowa, rozmiar 9, wypełniona zerami (float)
    print("t3 = ", t3)

    #JEDNOWYMIAROWA, ROZMIAR 9, WYPEŁNIONA 1(TU: int, typ domyślny to numpy.float64)
    t4 = np.ones(9, dtype = 'i')
    print("t4 = ", t4)

    #Jednowymiarowa, rozmiar 4,wypełniona wartościami pseudolosowymi z przedziału [0.0, 1.0]
    t5 = np.random.random(4)
    print("t5 = ", t5)

    #jednowymiarowa, rozmiar 9, wypełniona wartościami pseudolosowymi int (przedział [5,10])
    t6 = np.random.randint(5,10,9)
    print("t6 = ", t6)  

    #Tablica 3x5 wypełniona losowymi wrtościami z przedziału [0, 3]
    t7 = np.random.randint(3, size=(3,5))
    print ("t7 = ", t7)
    
    print("t1 = ", t1)
    t1=t1.reshape( (2,5) )  # Zmiana kształtu z 1D na 2D (konkretnie 2x5)
    print ("t1 po reshape(2,5)=", t1)


if __name__== "__main__":
    import numpy as np
    import sys

    sys.exit(main(sys.argv))