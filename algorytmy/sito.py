def sito(n):
    tp = [True] * (n+1)
    i=2
    while i*i<= n:
        if (tp[i]==True):
            for k in range(i*i, n+1, i): # oznaczamy wielokrotności jako liczby nie pierwsze
                tp[k]=False
        i = i + 1
    return tp

def main():
    wyniki = sito(100)
    print("\nMetoda SITA Erastotenesa")
    for i in range(2,100):
        if wyniki[i]:
            print(i, end=" ")

if __name__ == '__main__':
    import sys
    sys.exit(main())
    
