def Obszar(x1, y1, x2, y2, x3 , y3):
    return 0.5 * abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))


def CzyWewnatrz(x1, y1, x2, y2, x3, y3, xp, yp):
    T = Obszar(x1, y1, x2, y2, x3, y3)
    T1 = Obszar(xp, yp, x2, y2, x3, y3)
    T2 = Obszar(x1, y1, xp, yp, x3, y3)
    T3 = Obszar(x1, y1, x2, y2, xp, yp)
    return (T == T1 + T2 + T3)

def pobierzPunkt(tekst):
    punkt = input(tekst)
    x,y = punkt.split(",")
    x=eval(x)
    y=eval(y)
    return x,y
    

def main(args):
    x1, y1  = pobierzPunkt("Podaj współrzędn wierzchołka trójkąta  x1,y1 :  ")
    x2, y2  = pobierzPunkt("Podaj współrzędn wierzchołka trójkąta  x2,y2 :  ")
    x3, y3  = pobierzPunkt("Podaj współrzędn wierzchołka trójkąta  x3,y3 :  ")
    xp, yp  = pobierzPunkt("Podaj współrzędn punktu xp, yp :  ")
    
    if CzyWewnatrz(x1,y1,x2,y2, x3,y3,xp,yp):
        print (f"Punkt ({xp},{yp}) leży w trójkącie ({x1},{y1}), ({x2},{y2}), ({x3},{y3}) ")
    else:
        print (f"Punkt ({xp},{yp}) nie  należy do trójkąta ({x1},{y1}), ({x2},{y2}), ({x3},{y3}) ")
            
if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
