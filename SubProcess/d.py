def dzielenie(x,y):
    return x / y

def main(args):
    arg1 = sys.argv[0]
    arg2 = sys.argv[1]
    arg3 = sys.argv[2]
    
    print (f"Dzielenie: {arg2}/{arg3}={dzielenie(int(arg2),int(arg3))}")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))