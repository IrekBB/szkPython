def main(args):
    t0 = np.linspace(0,10,5) # przedział od 0 do 10 podzielony na 5 wartości
    print ("t0=", t0)
    t1 = np.arange(1,11) # Jednowymiarowa tablica, typ domyślny, seria liczb od 1 do 10
    t2 = np.arange(1,11,3)  # j.w. ale co 3
    t3 = np.zeros(9)  # rozmiar 9, wypełniona zerami(float)
    t4 = np.ones(9, dtype='i') # rozmiar 9, wypełniona jedynkami
    t5 = np.random.random(4)  # rozmiar 4, wartości pseudolosowe z przedziału [0.0, 1.0)
    t6 = np.random.randint(5,10,9) # rozmiar 9, wartości pseudolosowe z przedziału [5,10)
    print ("t5=",t5)
    print ("t6=",t6)
    t7 = np.random.randint(3, size=(3,5)) # tablica 3x5, losowe wartości z przedziału [0,3)
    print("t7=", t7) 

if __name__=="__main__":
    import sys
    import numpy as np
    sys.exit(main(sys.argv))
