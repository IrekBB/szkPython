import sys
"""
@decorator
def func(args): ...

def func(args): ...
func = decorator(func)

class Person:
@property
def name(self): ... # Rebinds: name = property(name)

class Person:
def name(self): ...
name = property(name)

"""
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self): # name = property(name)
        "name property docs"
        print('fetch...')
        return self._name
    
    @name.setter
    def name(self, value): # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter
    def name(self): # name = name.deleter(name)
        print('remove...')
        del self._name


def main(args):
    # Setter and deleter decorators
    bob = Person('Bob Smith') # bob has a managed attribute
    print(bob.name) # Runs name getter (name 1)
    bob.name = 'Robert Smith' # Runs name setter (name 2)
    print(bob.name)
    del bob.name # Runs name deleter (name 3)
    print('-'*20)
    sue = Person('Sue Jones') # sue inherits property too
    print(sue.name)
    print(Person.name.__doc__) # Or help(Person.name)


if __name__ == "__main__":
    sys.exit(main(sys.argv))