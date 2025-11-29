import sys
def add(x,y):
    return x + y

arg1 = sys.argv[0]
arg2 = sys.argv[1]
arg3 = sys.argv[2]

print(f"Wynik dodawania: {arg2} + {arg3} =  {add(int(arg2),int(arg3))}")
"""
x,y = arg1, arg2
print(f"Dodawanie: {x}+{y}={add(x,y)}")
"""
