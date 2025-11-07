"""
Funkcje i operatory tablicowe w numpy:
min()
max()
sum()
mean()
sort()
+  -  *  **
"""
import numpy as np
import sys

def main(args):
    t = np.array([ [3,9,1], [-2, 2,6]])
    print("MAX:\n{} \nto {}".format(t, t.max()))
    print("MIN:\n{} \nto {}".format(t, t.min()))
    print("SUM:\n{} \nto {}".format(t, t.sum()))
    print("MEAN:\n{} \nto {:.2f}".format(t, t.mean()))
    t1 = np.array([[3,9,1], [-2,2,6]]) # Dwuwymiarowa
    t2 = np.array([3,9,1-2,2,6]) # Jednowymiarowa
    print("NO SORT:\n{}".format(t1))
    print("SORT:\n{}".format(np.sort(t1)))
    print("NO SORT:\n{}".format(t2))
    print("SORT:\n{}".format(np.sort(t2)))
    a = np.array([[3,9,1], [-2,2,6]]) # Dwuwymiarowa
    b = np.array([[2,2,2], [4,0,1]])  # Dwuwymiarowa
    print("a=\n{}".format(a))
    print("b=\n{}".format(b))
    print("a+b=\n{}".format(a+b))
    print("a-b=\n{}".format(a-b))
    print("a*b=\n{}".format(a*b))
    print("a**b=\n{}".format(a**b))       

if __name__=="__main__":
    sys.exit(main(sys.argv))



