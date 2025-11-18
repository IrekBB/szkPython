"""
[<start>:<stop>:<step>]
"""

def main(args):
    t = np.arange(10) # 0..9
    t1 = t[:3]    # pierwsze trzy wartości -> t[0], t[1], t[2]
    t2 = t[3:]    # t[3], t[4]...t[9]
    t3 = t[5:7]   # t[5], t[6]
    t4 = t[::3]   # t[0], t[3], t[6], t[9]
    t5 = t[4::2]  # t[4], t[6], t[8]
    t6 = t[::-1]  # t[9], t[8].....t[0] --> tablica odwrócona
    t7 = t[4::2]  # t[4], t[2], t[0]
    print("t=\n",t)
    print ("t[:3]=\n", t1)
    print ("t[3:]=\n", t2)
    print ("t[5:7]=\n", t3)
    print ("t[::3]=\n", t4)
    print ("t[4::2]=\n", t5)
    print ("t[::-1]=\n", t6)
    print ("t[4::2]=\n", t7)

if __name__=="__main__":
    import sys
    import numpy as np
    sys.exit(main(sys.argv))