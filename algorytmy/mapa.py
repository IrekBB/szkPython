L= ["AABCDEGHIJKL", "AAAAB","AAAAB","ABC","AABCDEGHIJKL","AABCDEGHIJKL"]

def myfunc(n):
  return len(set(n))




def main(args):
    x = map(myfunc, L)
    m=(max(list(x)))
    ile = 0
    element=str()
    for e in L:
       if len(set(e))==m:
          element = e
          ile+=1
    print (m," ", element," ", ile)     

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv)) 