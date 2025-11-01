from matplotlib import pyplot as plt
import sys

def main(args):
    osX = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    osY = [5, 5.6,8, 9,11, 20, 14, 12, 10, 9.5]
    plt.plot(osX, osY,
             marker='*',
             linestyle='--',
             color='k',
             ms=10,
             linewidth = '1')
    plt.show()
if __name__=="__main__":
    sys.exit(main("sys.argv"))
