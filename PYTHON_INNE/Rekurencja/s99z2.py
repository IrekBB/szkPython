def euklides(n):
    L=[]
    while n>0:
        r = n % 2
        L.append(r)
        n=n//2
    return L

def odwroc(L, left, right):
    if left<right:
        L[left],L[right] = L[right], L[left]
        odwroc(L,left+1, right-1)
    

def main(args):
    n = int(input("n="))
    L = euklides(n)
    print(L)
    left, right = 0, len(L)-1
    odwroc(L,left, right)
    print (L)
    

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
