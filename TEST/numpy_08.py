"""
Rozszerzenia i transpozycje(metody):
hstack() - skleja tablice, poprzez ustawienie ich poziomo obok siebie
vstack() - skleja tablice poprzez ustawienie ich pionowo jedna pod drugą
transpose() - transpozycja, zamiany wierszy z kolumnami
concatenate() - join a sequence of arrays along an existing axis.
stack() - join a sequence of arrays along a new axis.
block() - assemble an nd-array from nested lists of blocks.
hstack() - stack arrays in sequence horizontally (column wise).
dstack() - stack arrays in sequence depth wise (along third axis).
column_stack() - stack 1-D arrays as columns into a 2-D array.
vsplit() - split an array into multiple sub-arrays vertically (row-wise).
unstack() - split an array into a tuple of sub-arrays along an axis.
"""

def main(args):
    t1 = np.arange(1,6)  # od 1 do 5
    print ("t1=\n", t1)
    t2 = np.arange(6,11)  # od 6 do 10
    print ("t2=\n", t2)
    
    t3b = np.vstack(t1)
    print ("Kształt t3b to: ", t3b.shape)
    print("t3b po zastosowaniu vstack():\n", t3b)
    
    t3a = np.vstack(t2)
    print ("Kształt t3a to: ", t3a.shape)
    print("t3a po zastosowaniu vstack():\n", t3a)

    t3 = np.vstack((t1,t2))   # argument to tuple
    print ("Kształt t3 to: ", t3.shape)
    print("t3 po zastosowaniu vstack():\n", t3)
    
    t3 = t3.transpose()
    print ("t3 po transpozycji:\n", t3)
    print("Nowy kształt t3 to:", t3.shape)
    print ("Liczba wymiarów tablicy t3 to: ", t3.ndim)

    t4 = np.hstack((t1, t2))
    print ("t4= t1 sklejona horyzontalnie z t2:", t4)
   
              
if __name__=="__main__":
    import sys
    import numpy as np
    sys.exit(main(sys.argv))