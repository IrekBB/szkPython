"""
Wycinki:
[<od>:<do>:<krok>]
"""

def main(args):
    t = np.arange(10)
    t1 = t[:3]  # Wycinek [0, 2], tj. [0 1 2]
    t2 = t[3:]  # wycinek [2, 9], tj. [3 4 5 6 7 8 9]
    t3 = t[5:7] # Wycinek [5, 6], tj. [5 6]
    t4 = t[::3]  # Co trzeci element [0 3 6 9]
    t5 = t[4::2] # Co drugi element zaczynając od indeksu 4, tj. [4 6 8]
    t6 = t[::-1]  # Wszystko, ale od końca [9 8 7 6 5 4 3 2 1 0]
    t7 = t[4::-2]  # Wszystkie co drugie od końca i zaczynając od indeksu 4, tj. [4 2 0]
    print ("t:")
    print (t)
    print ("t1:")
    print (t1)
    print ("t2:")
    print (t2)
    print ("t3:")
    print (t3)
    print ("t4:")
    print (t4)
    print ("t5:")
    print (t5)
    print ("t6:")
    print (t6)
    print ("t7:")
    print (t7)
    print("----------------------------------------------------")
    v = np.array (
        [
            [1, 2, 3, 4, 5],
            [5, 6, 7, 8, 9],
            [9, 10, 11, 12, 13],
            [14, 15, 16, 17, 18],
        ]
    )
    # Wycinek 2x4 (2 wiersze i 4 kolumny)
    v1 = v[:2, :4]
    print(v1)
    print()

    # Wycinek (3 wiersze)x(co 2 kolumny)
    v2 = v[:3, ::2]
    print(v2)
    print()
    
    # Wycinek (wszystkie wiersze)x(kolumny 1. i 2.)
    v3 = v[:, 1:3]
    print(v3)
    print("-----------------------------------------------------------")
    """
    Co wazne, wycinek tablicy NumPy dalej operuje na tym samym obszarze pamieci i modyfikacja komórki w wycinku
    także  zmieni oryginalną wartość. 
    Jest to różnica w porównaniu z listami. Jak uzyskać wycinek będący kopią oryginalnych danych?
    t_wycinek = t[0:2].copy()  
    """
    t = np.array([1, 5, 10, 15, 20 ])
    print(t)
    t_wycinek = t[0:2]
    t_wycinek[0] = -1
    t_wycinek[1]=-5
    print(t)


if __name__=="__main__":
    import numpy as np
    import sys
    sys.exit(main(sys.argv))