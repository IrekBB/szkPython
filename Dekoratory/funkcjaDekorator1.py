<<<<<<< HEAD
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
=======
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
>>>>>>> 04a243ce5a1b07f507b75f71b1dcf09ce156c7db
    sys.exit(main(sys.argv))