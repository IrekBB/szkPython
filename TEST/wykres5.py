from matplotlib import pyplot as plt
import sys
import numpy as np
import matplotlib.patches as mpatches

def main(args):
    L = list()
    for x in range (0,361,1):
        L.append(x)

    mojekaty = np.array(L)
    sinusy = np.sin(mojekaty*np.pi/180)

    sinus=plt.plot(mojekaty, sinusy, marker='H', linestyle=':', color='b', ms=10, linewidth='1', label='sinux(x)')
    blue_patch = mpatches.Patch(color='blue', label='sinus')
    plt.legend(handles=[blue_patch])
    
    plt.title("Wykres funkcji sinus")
    plt.xlabel("[kąt]")
    plt.ylabel("sinus(kąta)")
    plt.xticks([0, 50, 100, 150, 200, 250, 300, 350, 400])
    plt.show()



if __name__=="__main__":
    sys.exit(main(sys.argv))