def pobierz():
    print('Podaj współrzędne punktu A: ')
    xa, ya = eval(input("xa=")),eval(input("ya="))
    print('Podaj współrzędne punktu B: ')
    xb, yb = eval(input("xb=")),eval(input("yb="))
    print('Podaj współrzędne punktu C: ')
    xc, yc = eval(input("xc=")),eval(input("yc="))
    print('Podaj współrzędne punktu D: ')
    xd, yd = eval(input("xd=")),eval(input("yd="))
    return xa, ya, xb, yb, xc,yc, xd, yd

def wsp_rownania_pr(xa,ya,xb,yb):
    """
      układ równań:
      ya = a*xa+  b
      yb = a*xb + b
      rozwiązanie:
      a = (yb-ya)/(xb-xa)
      b = ya - ((yb-ya)/(xb-xa)) * xa
    """
    a,b = (yb-ya)/(xb-xa), ya - ((yb-ya)/(xb-xa)) * xa
    return a,b




def main(args):
    xa,ya,xb,yb,xc,yc,xd,yd = pobierz()
    wsp_k_AB_a, wsp_k_AB_b = wsp_rownania_pr(xa,ya,xb,yb)
    wsp_k_CD_a, wsp_k_CD_b = wsp_rownania_pr(xc,yc,xd,yd)

    if xa== xc and xb==xd and ya==yc and yb==yd:
        print ('Odcinki się pokrywają')
        return 

    if wsp_k_AB_a== wsp_k_CD_a:
        print ('Odcinki równoległe')
        return
    """
    y = a1*x + b1
    y = a2*x + b2
    to
    x = (b2-b1) / (a1 - a2)
    """
    x = (wsp_k_CD_b-wsp_k_AB_b) / (wsp_k_AB_a -  wsp_k_CD_a)
    y = wsp_k_AB_a*x+wsp_k_AB_b  # wstawiamy do dowolnej prostej
    if xa <= x and xc<=x and  x<=xb and x<=xd:
        print (f"Odcinki przecinają się w punkcie o współrzędnych ({x:.2f},{y:.2f})")
    else:
        print ("Odcinki nie przecinają się")

    return
    
    

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
