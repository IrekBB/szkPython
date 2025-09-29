def doTowers(topN, src, inter, dest):
    if topN==1: print(f"Dysk 1 z {src} na {dest}")
    else:
        doTowers(topN-1, src, dest, inter)
        print(f"Dysk {topN} z {src} na {dest}")
        doTowers(topN-1, inter, src, dest)

n = int(input("Podaj liczbę dysków n="))
doTowers(n,'A','B','C')



        
