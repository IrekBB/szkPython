def main(args):
    t = np.array([10,10,10,10,30,40,40,50,70,70,80,80,80,80,100,100,100])
    kubelki = [0,20,40,60,80,100]
    hist = np.histogram(t, bins = kubelki)
    print(hist[0])
    print(kubelki)
    """
    przedział [0,20): 10, 10, 10, 10                  --> 4
    przedział [20-40): 30                             --> 1
    przedział [40-60): 40, 40, 50                     --> 3
    przedział [60-80): 70, 70                         --> 2
    przedział [80-100): 80, 80, 80, 80, 100, 100, 100 --> 7
    
    """
    plt.hist(t, bins= kubelki)
    plt.title("Histogram")
    plt.show()

if __name__=="__main__":
    import sys
    import numpy as np
    from matplotlib import pyplot as plt 
    sys.exit(main(sys.argv))