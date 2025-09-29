def main(args):

    L = [
        ["Kowalski",  3.12],
        ["Kasprowicz",  4.40],
        ["Nowak",    6.00],
        ["Kosak",    5.44],
        ["Nasiadka",  5.32],
        ["Nowicki",    3.44],
        ["Kanigowski",  4.00],
        ["Danusiak",  4.00],
        ["Dworznik",  4.20],
        ["Kasprowicz",    3.00],
        ["Kasprowicz",  4.00],
        ["Kasprowicz",  3.10],
        ["Danusiak",  2.00],
        ["Danusiak",  2.14],
        ]
    
    LN = [L[i][0]  for i in range(len(L))]
    zbior = set(LN)
    LN = sorted(list(zbior))
    LC=[]
    for el in LN:
        for i in range(len(L)):
            if  el==L[i][0]:
                LC.append(L[i][1])
            LC = sorted(LC,reverse=True)
        print(el,' ',LC)
        LC.clear()
    
    

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
