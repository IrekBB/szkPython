def odwroc(tablica,lIndex,rIndex):
    if lIndex<rIndex:
        tablica[lIndex], tablica[rIndex] = tablica[rIndex], tablica[lIndex]
        return odwroc(tablica,lIndex+1,rIndex-1)

def main(args):

    tab = [1,2,3,4,5,10,20,40,50]
    #tab = [1,12,14,15,111,112,114,115]
    if len(tab)==0 or len(tab)==1:
        print (tab)
        return
    else:
        odwroc(tab,0,len(tab)-1)

    print(tab)
    return

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
