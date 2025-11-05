import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib.patches as mpatches

def main(args):
    osX, osY, osY2 = np.loadtxt('danedowykresu.csv', delimiter=',', unpack=True)
    seria1=plt.plot(osX, osY, marker='*', linestyle='--', color='k', ms=10, linewidth='1', label='Seria 1')
    seria2=plt.plot(osX, osY2, marker='o', linestyle='-', color='m', ms=10, linewidth='1', label='Seria 2')
    
    black_patch = mpatches.Patch(color='black', label='seria 1')
    purple_patch = mpatches.Patch(color='purple', label='seria 2')
    plt.legend(handles=[black_patch, purple_patch])
    
    plt.title("Pomiary napięcia\n(dane pobrane z pliku CSV")
    plt.xlabel("[t]")
    plt.ylabel("[V]")
    plt.xticks([0, 25, 55, 75, 100])
    plt.show()

if __name__=="__main__":
    sys.exit(main(sys.argv))