def symetria1(x):
    if x==0:
        print ("-", end=" ")
    else:
        print("<", end=" ")
        symetria1(x-1)
        print(">", end=" ")
    
def symetria2(x):
    for i in range(x):
        print("<",end=" ")
    print("-", end=" ")
    for i in range(x):
        print(">", end=" ")

def main(args):
    x = int(input("x="))
    print ("*** Wywołanie rekurencyjne ***")
    symetria1(x)
    print()
    print ("*** Wywołanie iteracyjne ***")
    symetria2(x)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
