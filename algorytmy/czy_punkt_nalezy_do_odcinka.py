def pobierz():
    print('Podaj współrzędne punktów A, B i C:')
    xa, ya = eval(input("xa=")),eval(input("ya="))
    xb, yb = eval(input("xb=")),eval(input("yb="))
    xc, yc = eval(input("xc=")),eval(input("yc="))
    return xa, ya, xb, yb, xc,yc

def min(a,b):
    if a <= b : return a
    else: return b

def max(a,b):
    if a >= b : return a
    else: return b   

def czy_nalezy(ax,ay,bx,by,cx,cy):
    return bx*cy + ax*by + cx*ay - ax*cy-bx*ay-cx*by==0 and cx >= min(ax,bx) and cx<=max(ax,bx) and cy>=min(ay,by) and cy<=max(ay,by)

def main(args):
    xa,ya,xb,yb,xc,yc = pobierz()
    if czy_nalezy(xa,ya,xb,yb,xc,yc):
        print (f'Punkt ({xc},{yc}) należy do odcinka AB.')
    else:
        print (f'Punkt ({xc},{yc}) nie należy do odcinka AB.')

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
