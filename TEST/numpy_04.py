def conv():
    msg ="Podaj wartości tablicy oddzielone przecinkami"
    title = "Operacje na tablicach Numpy (tablica t)"
    res=""
    while res =="":
        res = easygui.enterbox(msg, title)
        print("Nic nie wybrano")
    wi = [int(x) for x in res.split(",")]
    return wi

def main(args):
    t = np.array(conv())
    mojekaty=np.array(t)
    sinusy = np.sin(mojekaty*np.pi/180) # Konwersja z katów 0...360 na radiany
    cosinusy = np.cos(mojekaty*np.pi/180)
    tangensy =  np.tan(mojekaty*np.pi/180)
    easygui.msgbox("sinus kata sin =" + str(sinusy), str(mojekaty))
    easygui.msgbox("cosinus kąta =" + str(cosinusy),  str(mojekaty))
    easygui.msgbox("tangens kata =" + str(tangensy), str(mojekaty))


if __name__=="__main__":
    import numpy as np
    import sys
    import easygui
    sys.exit(main(sys.argv))