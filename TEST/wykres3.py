# Wykresy słupkowe
from matplotlib import pyplot as plt
import sys

def main(args):
    testy = ['Wydajnościowe', 'Funkcjonalne', 'Niefunkcjonalne', 'Pozostałe']
    passRate = [5, 15, 20, 5]
    statystyki = plt.bar(testy, passRate, color = 'r', label = 'Status=OK')
    plt.legend (handles=[statystyki])
    plt.title("Testy regresji - faza 2.")
    plt.xlabel("Kategorie")
    plt.ylabel("Wyniki")
    plt.yticks([0, 5, 10, 15, 20])
    plt.show()


if __name__=="__main__":
    sys.exit(main(sys.argv))