def main(args):
    pomiary = pd.read_csv(r"E:\Users\opiekun\Documents\szkPython\TEST\dane1.csv",sep=";")
    print ("Interpretacja pomiarów:", pomiary.info())
    print ("dane1.csv=\n",pomiary)
    print ("\tCzytamy 3 wiersze z przodu:\n", pomiary.head(3))
    print ("\tCzytamy 2 wiersze z tyłu:\n", pomiary.tail(2))
    print ("------------- Rozmiar tabeli ---------------")
    print ("Wymiary: ", pomiary.shape)  # W Tu: (19,4)
    print ("Liczba wierszy:", pomiary.shape[0]) # Tu: 19


if __name__=="__main__":
    import sys
    import pandas as pd
    sys.exit(main(sys.argv))
    """
    * brak parametru w head i tail -> wypisanie 5 wierszy (odpowiednio z produ i tyłu)
    * print ("Czytamy cały plik oprócz 6 ostatnich wierszy:\n", pomiary.head(-6))
    """