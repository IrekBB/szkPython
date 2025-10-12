cpt=0

def McCarthy(x):
    global cpt
    cpt=cpt+1
    if x > 100:
        return x-10
    else:
        return McCarthy(McCarthy(x+11))
    
def main(args):
    x = int(input("Podaj x:"))
    print(f"McCarthy({x})={McCarthy(x)}")
    if cpt==1:
        print ("[Funkcja została wywołana raz]")
    else:
        print (f"[Funkcja została wywołana {cpt} razy]")
    print ("Do widzenia!")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
