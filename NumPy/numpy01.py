"""
pip install numpy

"""

import numpy as np

def main(args):
    tab1Da = np.array([1,2,3,4,5])  # jednowymiarowa, typ domyślny
    print ("tab1Da: ", tab1Da)
    print ("Wycinek tab1Da[-3, -1]: ", tab1Da[-3:-1])
    print ("tab1Da[1]: ", tab1Da[1])
    tab1Db = np.arange(1,10)  # jednowymiarowa, typ domyślny, seria liczb od 1 do 9
    print("tab1Db: ", tab1Db)
    # jednowymiarowa, typ 'napis Unicode', tj. seria napisów od "1" do "9"
    tab1Dc = np.array(np.arange(1,10), dtype='U')
    '''
     '?'  boolean
     'b'  bajt ze znakiem (od -127 do 128)
     'B'  bajt (0-255)
     'i'  liczba całkowita ze znakiem
     'u'  liczba całkowita bez znaku
     'f'  odpowiednikpythonowego float
     'c'  liczba zespolona
     'U'  napis Unicode
    '''
    print("tab1Dc: ", tab1Dc)
    print ("Typ danych w tablicy tab1Dc to: ", type(tab1Dc[5]))

    tab2Da = np.array([[1,2,3],[4,5,6]])  # tablica dwuwymiarowa
    tab2Db = np. array([[7,8,9],[10,11,12]])
    print ("Tablica 2D:\n", tab2Da)
    print("tab2Da[1,2]=", tab2Da[1,2]) # trzeci element z drugiego wiersza (liczymy od zera)
    print("tab2Da[1][2]=", tab2Da[1][2])  # składnia alternatywna

    tab3Da = np.array([ [[1,2,3], [4,5,6]], [[7,8,9], [10, 11, 12]] ])
    tab3Db = np.array([tab2Da, tab2Db])    # taka sama zawartość jak dla tab3Da
    print ("Tablica 3D:\n ", tab3Da)
    print ("Tablica 3D:\n ", tab3Db)

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
    
