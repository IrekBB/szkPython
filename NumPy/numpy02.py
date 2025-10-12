import numpy as np

def main(args):                               # Operacje tablicowe numpy
    t = np.array([5,10,15,20])
    print ("t      =", t, end= " ")
    print()
    print("t + 5  =", t+5)          
    print("t - 5  =", t-5)
    print("t * 2  =", t*2)
    print("t / 2  =", t/2)
    print("t // 2 =", t//2)
    print("-t     =", -t)
    print("t ** 2 =", t**2)
    print("t % 2   =", t%2)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))