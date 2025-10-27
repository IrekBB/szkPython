<<<<<<< HEAD
import sys

def main(args):
    # dekorator "identycznościowy", zwracający nową funkcję, ale równoważną podanej:
    
    def identity(func):
        def new_func(*args, **kwargs):    # rozpakowanie argumentów pozycyjnych i nazwanych omuwimy później
            return func(*args, **kwargs)
        return new_func
    
    @identity
    def f(a, b):
        print(a, b)

    f(10, 20)    

if __name__=="__main__":
=======
import sys

def main(args):
    # dekorator "identycznościowy", zwracający nową funkcję, ale równoważną podanej:
    
    def identity(func):
        def new_func(*args, **kwargs):    # rozpakowanie argumentów pozycyjnych i nazwanych omuwimy później
            return func(*args, **kwargs)
        return new_func
    
    @identity
    def f(a, b):
        print(a, b)

    f(10, 20)    

if __name__=="__main__":
>>>>>>> 04a243ce5a1b07f507b75f71b1dcf09ce156c7db
    main(sys.argv)