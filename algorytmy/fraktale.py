def dywan_sierpinskiego(z, stopien, dl_bok):

    def kwadrat(bok, kolor):
        z.color(kolor)
        z.begin_fill()
        for i in range(4):
            z.forward(bok)
            z.right(90)
        z.end_fill()

    if stopien == 0:
        kwadrat(dl_bok, 'black')
        return None
    else:
        kwadrat(dl_bok, 'white')
        for i in range(4):
            for j in range(2):
                dywan_sierpinskiego(z, stopien-1, dl_bok/3)
                z.forward(dl_bok/3)
            z.forward(dl_bok/3)
            z.right(90)

def fraktal_cantora(z, dlugosc_lini, ile):
    for i in range(ile):
        zbior_cantora(z, dlugosc_lini, 1/3, i)
        z.back(dlugosc_lini)
        z.lt(90)
        z.back(100 / ile - 1)
        z.rt(90)

def platek_kocha(z, stopien, dl_bok):

    def bok(stopien, dl_bok):
        if stopien == 0:
            z.forward(dl_bok)
        else:
            bok(stopien-1, dl_bok/3)
            z.left(60)
            bok(stopien-1, dl_bok/3)
            z.right(120)
            bok(stopien-1, dl_bok/3)
            z.left(60)
            bok(stopien-1, dl_bok/3)

    z.right(30)
    for i in range(3):
        bok(stopien, dl_bok)
        z.right(120)

    z.left(30)

def drzewo_binarne(z, stopien, dl_bok):
    if stopien == 0:
        pozycja = z.pos()
        z.forward(dl_bok)
        z.goto(pozycja)
    else:
        pozycja = z.pos()
        z.forward(dl_bok)
        z.left(45)
        drzewo_binarne(z, stopien-1, dl_bok/2)
        z.right(90)
        drzewo_binarne(z, stopien-1, dl_bok/2)
        z.left(45)
        z.goto(pozycja)


def main(args):
    from turtle import Turtle
    zl = Turtle()

    # przenosimy żółwia w konkretne miejsce układu współrzędnych
    # aby narysowany obraz dobrze mieścił się w oknie
    zl.penup()
    zl.goto(-300,300)
    zl.pendown()

    # dywan_sierpinskiego(zl, 3, 500)
    # fraktal_cantora(zl, 300, 5)
    # platek_kocha( zl, 3, 200)
    # zl.goto(-20,-20)
    # drzewo_binarne(zl, 3, 50)

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))

    
    
