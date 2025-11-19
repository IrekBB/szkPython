# Podzakresy w tablicach 2D
def main(args):
    v = np.array([
        [1, 2, 3, 4, 5],
        [5, 6, 7, 8, 9],
        [9, 10, 11, 12, 13],
        [14, 15, 16, 17, 18]
    ])
    print ("v=\n",v)
    # wycinek 2x4 (2 wiersze i 4 kolumny)
    v1 = v[:2,:4]
    print ("v1=\n",v1)
    # wycinek 3 wiersze x co dwie kolumny
    v2 = v[:3,::2]
    print ("v2=\n", v2)
    # wszystkie wiersze x (druga, trzecia)kolumna
    v3 = v[:,1:3]
    print ("v3=\n", v3)
    """
    Wycinek numpy operauje na tym samym obszarze pamięci
    i modyfikacja komórki w wycinku także zmieni oryginalną wartość
    """
    print ("##################################################")
    t =np.array([1, 5, 10, 15, 20])
    t_wycinek = t[0:2]   # aby nie naryszyć t: t_wycinek=t[0:2].copy()
    print("t=\n",t)
    print ("wycinek t[0:2]=\n",t_wycinek)
    print ("---- Modyfikacja wycinka -----")
    t_wycinek[0] = -1                  
    t_wycinek[1] = -5
    print ("t_wycinek[0] = -1")
    print("t_wycinek[1] = -5")
    print("t=\n", t)


if __name__=="__main__":
    import sys
    import numpy as np
    sys.exit(main(sys.argv))