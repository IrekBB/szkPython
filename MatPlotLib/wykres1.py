"""
parametry:
marker  - styl punktu danych
ms - rozmiar markera (ang. marker size)
linestyle - styl linii
color - kolor 
linewidth - grubość linii
"""
import matplotlib.pyplot as plt
import numpy as np
import sys

def main(args):
    x = np.linspace(-2, 2, 100)  # Tablica(wektor)  wartości zakresu (-2,2) na osi X; 100 to ilość elemetów
    y1 = -5 / x  # pierwsza funkcja matematyczna hiperbola
    y2 = np.sin(x) * 80 - 50  # druga funkcja matematyczna
    fig = plt.figure(figsize=(10,5))
    plt.plot(x, y1, label = "HIPERBOLA", linestyle = '--')  # Wykres 1
    plt.plot(x, y2, label = '80*sin(x)-50')  # Wykres 2
    plt.legend() # Opis (tzw. legenda)
    plt.grid(alpha = .6, linestyle='-') # Siatka
    # Zastepujemy domyślne wartości wystepujące na osi Y ich własną liczbą, rozkładamy je według
    # naszego zapotrzebowania, co czyni wykres czytelniejszym 
    plt.yticks([-200, -150, -100, 0, 100, 100, 150, 200 ]) # Normalizacja wartości na osi Y
    # Własne etykiety osi
    plt.xlabel('Oś X')
    plt.ylabel('Oś Y')
    plt.title("Wykresy funkcji")
    plt.show()  # Wyswietl wykres na ekranie

if __name__=="__main__":
    sys.exit(main(sys.argv))
