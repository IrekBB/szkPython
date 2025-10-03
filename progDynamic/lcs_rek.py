# Wykład 11, In[6]
def lcs_rek(a,b):
    if len(a) == 0 or len(b) == 0:
        return 0
    if a[-1] != b[-1]:
        return max(lcs_rek(a[:-1],b), lcs_rek(a, b[:-1])) # dodatkowe nieefektywności - koiowanie napisów
    return 1 + lcs_rek(a[:-1], b[:-1]) # i tu też

def main(args):
    print (lcs_rek('ALGORYTM','GRAMOTY'))

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
