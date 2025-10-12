def post_dw_dod(x, res=0, pos=0):
    if x>0:
        post_dw_dod(x//2, res + ((x%2)*pow(10,pos)),pos+1)
    else:
        print(res, end="")
    
    

def main(args):
    x = int(input("x="))
    post_dw_dod(x, res=0, pos=0)
    

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
