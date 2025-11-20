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
"""
[:, 1:3] in Python is a slicing operation, typically used on multi-dimensional objects like NumPy
arrays or Pandas DataFrames. It selects all rows (due to the : before the comma) and a specific slice 
of columns (columns with index 1 and 2, as the slice is 1:3, which includes the start but excludes the end index). 
"""

if __name__=="__main__":
    import sys
    import numpy as np
    from matplotlib import pyplot as plt 
    import matplotlib.patches as mpatches
    sys.exit(main(sys.argv))