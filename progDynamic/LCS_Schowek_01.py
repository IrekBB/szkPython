# LCS ze schowkiem, wersja pierwsza - jeszcze do poprawki
def lcs(a,b, cache={}):    # IN [7]
    n = len(a)
    m = len (b)
    if n==0 or m==0:
        return 0

    if (a,b) not in cache:
        if a[-1] != b[-1]:
                cache[a,b] = max(lcs(a[:-1],b), lcs(a,b[:-1]))
        else:
                cache[a,b] = 1 + lcs(a[:-1], b[:-1])
    return cache[a,b]

def lcs_poprawiona(a,b):   #IN[8]
     cache={}
     def lcs_inner(a,b):
          n = len(a)
          m = len(b)
          if n==0 or m==0:
               return 0
          
          if (n,m) not in cache:
               if a[-1] != b[-1]:
                    cache[n,m]=max(lcs_inner(a[:-1],b), lcs_inner(a,b[:-1]))
               else:
                    cache[n,m] = 1 + lcs_inner(a[:-1],b[:-1])
          return cache[n, m]
     return lcs_inner(a,b)



def main(args):
    print (lcs('ALGORYTMALGORYTMALGORYTM','GRAMOTYGRAMOTYGRAMOTY'))
    print (lcs_poprawiona('ALGORYTMALGORYTMALGORYTM','GRAMOTYGRAMOTYGRAMOTY'))
if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
