from MojeTypy import pomiar as p


def main(args):
    p1=p.Pomiar("Tester1", 220.1)
    print (f"Obiekt 'p1' to [{p1}]")
    print ("Licznik obiektów: ", p.Pomiar.Licznik)
    
    p2=p.Pomiar("Tester2", 200)
    print (f"Obiekt 'p2' to [{p2}]")
    print ("Licznik obiektów: ", p.Pomiar.Licznik)

    p3=p.Pomiar("Tester1", -221)
    print (f"Obiekt 'p3' to [{p3}]")
    print ("Licznik obiektów: ", p.Pomiar.Licznik)

    print (f"Obiekt 'p3' utworzył {p3.autor}, data: {p3.dataczas}")   # właściwości tylko do odczytu
    print("Modyfikujemy p3 - wartość zmieniona na -230:")
    p3.odczyt = -230  #właściwość do odczytu i modyfikacji
    print (f"Obiekt 'p3' to teraz [{p3}")  
    
    print ("Przechodzimy do domeny obiektów klasy PomiarV")
    print (f"Pierwotny limit dolny: {p.PomiarV.DolnyLimit} i limit górny: {p.PomiarV.GornyLimit}")
    p.PomiarV.DolnyLimit = 0
    p.PomiarV.GornyLimit = 30
    print (f"Nowy limit dolny: {p.PomiarV.DolnyLimit} i limit górny: {p.PomiarV.GornyLimit}")

    p2 = p.PomiarV("Tester1", 5,"F123123B")
    print ("Obiekt klasy pochodnej PomiarV 'p2' to [{p2}]")
    print ("Licznik obiektów:", p.Pomiar.Licznik)

    p3 = p.PomiarV("Tester1", 30,"Z123123B")
    print ("Obiekt klasy pochodnej PomiarV 'p3' to [{p3}]")
    print ("Licznik obiektów:", p.Pomiar.Licznik)

    p3.odczyt = 22.3
    print (f"Obiekt 'p3' po modyfikacji to [{p3}]")
    print ("Odczytujemy właściwości obiektu, używając metody klasy bazowej")
    print ("Czytamy pole 'autor' obiektu p3:", p3.autor)
    p3.komunikat()


if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))