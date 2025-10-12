def main(args):
    print ("* Algorytm sortowania przez wstawianie *")
    tab = t.TabInt(12)
    for element in [40, 2, 1, 6, 18, 20, 29, 32, 233, 34, 39, 41]:
        tab.wstaw(element)
    tab.wstaw(100)  # Zobaczymy komunikat: [BŁĄD] brak miejsca w tablicy dla elementu o wartości 100
    tab.wypisz()
    tab.insertSort()
    tab.wypisz()
    print ("* Algorytm sortowania bąbelkowego *")
    tab1 = t.TabInt(12)
    for element in [40, 2, 1, 6, 18, 20, 29, 32, 233, 34, 39, 41]:
        tab1.wstaw(element)
    tab1.wstaw(100)  # Zobaczymy komunikat: [BŁĄD] brak miejsca w tablicy dla elementu o wartości 100
    tab1.wypisz()
    tab1.bubble()
    tab1.wypisz()       
    print ("* Algorytm sortowania bąbelkowego - ShakerSort  czyli przez wstrząsanie*")
    tab2 = t.TabInt(12)
    for element in [40, 2, 1, 6, 18, 20, 29, 32, 233, 34, 39, 41]:
        tab2.wstaw(element)
    tab2.wstaw(100)  # Zobaczymy komunikat: [BŁĄD] brak miejsca w tablicy dla elementu o wartości 100
    tab2.wypisz()
    tab2.bubble()
    tab2.wypisz()  
    print ("* Algorytm sortowania szybkiego - czyli QuickSort *")
    tab3 = t.TabInt(12)
    for element in [40, 2, 1, 6, 18, 20, 29, 32, 233, 34, 39, 41]:
        tab3.wstaw(element)
    tab3.wstaw(100)  # Zobaczymy komunikat: [BŁĄD] brak miejsca w tablicy dla elementu o wartości 100
    tab3.wypisz()
    tab3.QuickSort(0, len(tab3)-1)
    tab3.wypisz()      

if __name__ == "__main__":
    from MojeTypy import TabInt as t
    import sys
    sys.exit(main(sys.argv)) 