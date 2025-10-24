import sys

def do_twice(func):
    def new_func():
        func()
        func()
    return new_func

def f():
    print('!')

def main(args):
    g = do_twice(f)
    g()
    
if __name__=="__main__":
    sys.exit(main(sys.argv))