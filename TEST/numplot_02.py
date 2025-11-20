def main(args):
    t1 = np.arange(-5, 6)
    t2 = t1**2-5
    t3 = t1*3 - 2
    print ("t1=\n",t1)
    print ("t2=\n",t2)
    print ("t3=\n",t3)

    t3 = np.vstack((t1, t2, t3))  
    print ("t3 po vstack(t1, t2, t3)=\n", t3)

    t3 = t3.transpose()
    print ("t3 po transpose=\n", t3)

    plt.xlabel=("X")
    plt.ylabel=("Wykresy")
    plt.title("Wykres funkcji x**2-5 i 3x-2")  
    plt.plot(t3[:,0:1], t3[:,1:3], # Pierwsza kolumna oś X, pozostałe dwie - wartości osi Y
             marker ='.',  # marker: kropka
             ms=10,       # rozmiar markera
             linewidth = '1',)  # grubość linii
    plt.show()


if __name__=="__main__":
    import sys
    import numpy as np
    from matplotlib import pyplot as plt 
    import matplotlib.patches as mpatches
    sys.exit(main(sys.argv))