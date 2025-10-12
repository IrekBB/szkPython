"""
k - czarny               r - czerwony
m -  purpurowy           g - zielony
y - żółty                b - niebieski
w - biały                c - niebieskozielony
"""

from matplotlib import pyplot as plt 



def main(args):
    kategorie = ['Samoloty', 'Czołgi', 'Wozy bojowe', 'Helikoptery']
    wyniki = [99, 509, 1556, 123]
    statystyki = plt.bar(kategorie, wyniki, color='k')
    plt.legend(handles=[statystyki])  # The original object which is used to generate an appropriate entry in the legend.
    plt.title("Straty wojenne agresora - 1. kwartał 2022")
    plt.xlabel("Kategorie")
    plt.ylabel("Wyniki")
    plt.show()




if __name__ =="__main__":
    import sys
    sys.exit(main(sys.argv))