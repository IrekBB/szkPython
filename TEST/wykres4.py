from matplotlib import pyplot as plt
import sys

def main(args):
    t= [10, 10, 10, 30, 40, 40, 50, 70, 70, 80, 80, 80, 80, 100, 100, 100]
    statystyki = plt.hist(t, 10)
    plt.show()


if __name__=="__main__":
    sys.exit(main(sys.argv))