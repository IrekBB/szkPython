# Pandas - Series (jednowymiarowe tablice danych)


def main(args):
    t1 = [4, 2, 8]      # 0  4; 1  2; 2  8 -> pierwsza wartości 0,1,2  to indeksy
    seria1 = pd.Series(t1)
    print("seria1=\n", seria1)
    print("seria1[1]=\n", seria1[1])
    print("seria1[1,2]=\n", seria1[[1,2]].values)  # values pozwala na zwrócenie wartości bez indeksu
    wycinek=[True, False, True]
    print ("seria1[True,False,True]=", seria1[wycinek].values) # wypisze wartości na pozycjach True

    t2 = [5,'a',"hello"]
    indeksik = ['a','b','c']
    seria2 = pd.Series(t2, index=indeksik)
    print ("seria2=\n", seria2)
    print("seria2['a':'b']=\n",seria2['a':'b'].values)

    limity = {"Miernik1":100.20, "Miernik2":120, "Miernik3":150.5, "Miernik4":115,"Miernik5":125,}
    seria3 = pd.Series(limity)  # Seria utworzona na podstawie słownika Pythona
    print("seria3=\n", seria3)

    wszedzietosamo = pd.Series(5, index =[x for x in range(10)])  # seria dzięsięciu liczb 5
    print ("wszedzietosamo=\n",wszedzietosamo.values)


if __name__=="__main__":
    import sys
    import pandas as pd
    sys.exit(main(sys.argv))