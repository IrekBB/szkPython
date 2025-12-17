# (x,y) - współrzędna punktu P
# (x0,y0), (x1,y1) - początek i koniec odcinka

def czy_polprosta_przecina_odcinek(x,y, x0,y0, x1,y1):

        # odcinek poziomy
        if y1==y0:
                return 0

        # sortowanie: y0 < y1
        if y0 > y1:
            x0, y0, x1, y1 = x1, y1, x0, y0

        # odcinek A powyzej lub ponizej
        if y0 < y and y1 <= y:  # odcinek powyżej
            return 0

        if y0 > y and y1 > y:  # odcinek poniżej półprostej
            return 0

        # odcinek B - po lewej od polprostej
        if x0 < x and x1 < x:
                return 0

        # odcinek C
        if x0 >= x and x1 >= x:
                return 1

        # odcinek D
        # 1. liczymy punkt przecięcia (xp, yp)
        t  = (y-y0)/float(y1-y0)
        xp = x0 + t*(x1-x0)      # yp=y

        # 2. klasyfikujemy
        if xp >= x:
                return 1
        else:
                return 0

def czy_punkt_jest_w_srodku(x, y, krawedzie, wierzcholki):
    ile_razy = 0

    for e in krawedzie:
        a, b = e

        x0, y0 = wierzcholki[a]
        x1, y1 = wierzcholki[b]

        ile_razy += czy_polprosta_przecina_odcinek(x, y, x0, y0, x1, y1)

    return ile_razy % 2 == 1

lista_wierz = []
lista_kr = []

x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

ile = int(input("zdefiniuj obszar. ile ma wierzchołków: "))
if ile < 3:
    print("nie ma obszaru")
    exit()
for i in range(ile):
    print ("wierzchołek", [i], end=" : \n")
    wx = int( input("podaj wx: "))
    wy = int( input("podaj wy: "))

    lista_wierz.append((wx,wy))
    lista_kr.append((i,i+1))

lista_kr[ile-1] = (ile-1, 0)

if czy_punkt_jest_w_srodku(x, y, lista_kr, lista_wierz) == 1:
    print("jest w srodku")
else:
    print("jest poza")
