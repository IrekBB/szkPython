import numpy as np

def main(args):                               # Operacje tablicowe numpy
    t = np.array([ [3,9,1],[-2, 2, 6] ])
    print ("t      =", t, end= " ")
    print()
    print("t.min()  =", t.min())            
    print("t.max()  =", t.max())
    print("t.sum()  =", t.sum())
    print("t.mean() =", t.mean())
    print("t.sort() =", np.sort(t))   # Quicksort
    t1 = np.array([[3, 9,1], [-2, 2, 6]])  # tablica dwuwymiarowa
    t2 = np.array([3,9,1, -2, 2, 6])       # tablica jednowymiarowa
    tsort1 = np.sort(t1)  # tablice dwuwymiarowe 2D - kazdy wiersz sortowany osobno
    tsort2 = np.sort(t2)
    print("tsort1 =",tsort1, end=" ")
    print()
    print ("tsort2 =", tsort2, end=" ")
    print()
    """
    Tablice można sortowac też w "miejscu", wóczas modyfikacji ulegnie 
    bieżący obiekt: t.sort()
    """
    tsort3 = np.array([100,23,89,45,1,2,90,100,67])
    print ("tsort3 =", tsort3, end=" ")
    print()
    tsort3.sort()
    print("tsort3.sort()",tsort3 , end=" ")
    print()
    
    a = np.array([ [3,9,1], [-2,2,6] ])
    print("a = ", a, end=" ")
    print()
    b = np.array([ [2,2,2], [2,2,7] ])
    print("b = ", b, end=" ")
    print() 
    print ("a + b =", a+b, end=" ")
    print()
    print ("a - b =", a-b, end=" ")
    print()
    print ("a * b =", a*b, end=" ")
    print()
    print ("a ** b =", a**b, end=" ")
    print()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))