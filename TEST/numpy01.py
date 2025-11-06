import easygui
import sys
import numpy as np

def main(args):
    msg ="Podaj wartości tablicy oddzielone przecinkami"
    title = "Test tablic w numpy"
    res = easygui.enterbox(msg, title)
    wi = [int(x) for x in res if x!=',']
    tab1Da = np.array(wi)
    print ('tab1Da:', tab1Da)
    print ("Wycinek tab1Da [-3,-1]:", tab1Da[-3:-1])
    tab1Db = np.array (np.arange(1,10), dtype='i')
    print ('tab1Db:', tab1Db)
    tab1Dc = np.array (np.arange(1,10), dtype='U') # seria liczb 1..9 jako napis Unicode -> U
    print ('tab1Dc:', tab1Dc)
    print ("Typ danych w tablicy tab1Dc to:", type(tab1Dc[5]))
    easygui.msgbox(tab1Dc,"Test tablic w numpy")
    # Tablice dwywymiarowe
    tab2Da = np.array ([[1,2,3], [4,5,6]])
    tab2Db = np.array ([[7,8,9], [10,11,12]])
    print ("Tablica 2D:\n", tab2Da)
    print ("tab2Da[1,2]=", tab2Da[1,2]) # Trzeci element z drugiego wiersza (liczymy od zera)
    print ("tab2Da[1][2]=", tab2Da[1][2]) # Inna składnia
    # Tablice 3D
    tab3Da=np.array([ [[1,2,3], [4,5,6]],  [[7,8,9], [10,11,12]]])
    tab3Db=np.array([ tab2Da, tab2Db])
    print ("Tablica 3D:\n", tab3Da)
    print ("Tablica 3D:\n", tab3Db)
    

if __name__=="__main__":
    sys.exit(main(sys.argv))