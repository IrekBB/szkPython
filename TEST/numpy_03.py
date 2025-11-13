import numpy as np
import sys
import easygui



def main(args):
    msg ="Podaj wartości tablicy oddzielone przecinkami"
    title = "Operacje na tablicach Numpy (tablica t)"
    res = easygui.enterbox(msg, title).split(",")
    wi = [int(x) for x in res]
    t = np.array(wi)
    easygui.msgbox("t+5=" + str(t+5), str(t))
    easygui.msgbox("t-5=" + str(t-5),  str(t))
    easygui.msgbox("t*2=" + str(t*2), str(t))
    easygui.msgbox("t/2=" + str(t/2), str(t))
    easygui.msgbox("t//2=" + str(t//2), str(t))
    easygui.msgbox("-t=" + str(-t), str(t))
    easygui.msgbox("t**2=" + str(t**2), str(t))
    easygui.msgbox("t%2=" + str(t%2), str(t))
    print("koniec...")

if __name__=="__main__":
    sys.exit(main(sys.argv))