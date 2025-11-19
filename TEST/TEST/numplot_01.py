def main(args):
    osX = np.arange(-5, 6)  # liczby od -5 do 5
    osY = osX*osX + 5
    print ("x=", osX)
    print ("y=", osY)
    plt.xlabel("X")
    plt.ylabel("Y=X*X+5")
    
    plt.plot(osX, osY,
             marker='.',
             linestyle='--',
             color='k',
             ms=10,
             linewidth='1')
    
    plt.title=("Wykres utworzony przy użyciu tabel NumPy")
    plt.show()



if __name__=="__main__":
    import sys
    import numpy as np
    from matplotlib import pyplot as plt 
    sys.exit(main(sys.argv))