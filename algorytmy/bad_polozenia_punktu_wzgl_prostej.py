"""
Badanie położenia punktu względem prostej

Dana jest prosta określona równaniem:
y = ax+b
gdzie a i b to liczby rzeczywiste
 
Aby sprawdzić czy punkt P(xp, yp) leży na prostej należy odpowiednio podstawić
jego współrzędne do równania prostej i sprawdzić, czy będzie ono spełnione.
"""
def main(args):
    f = input("Podaj równanie prostej: ")
    x=eval(input("Współrzędna x punktu x = "))
    y=eval(input("Współrzędna y punktu y = "))
    if eval(f)==y:
        print(f"Punt ({x},{y}) należy do prostej y={f}.")
    else:
        print(f"Punt ({x},{y}) nie leży na prostej y={f}.")

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
