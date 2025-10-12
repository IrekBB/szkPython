def RecTerm(n):
    if n == 0:
        print ("B", end=" ")
    else:
        print("A", end=" ")
        RecTerm(n-1)    # Wywołanie rekurencyjne procedury P jest zwane terminalnym (ang. end-recursion), 
                        # jeśli nie następuje po nim żadna instrukcja procedury.

def main(args):
    RecTerm(5)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
