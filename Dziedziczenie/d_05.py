# Wywoływanie metod z nadklas
class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
    
    def do_something(self):
        print('obiekt Vehicle coś robi!')

class Car(Vehicle):
    def do_something(self):
        super().do_something()
        print('obiekt Car coś robi!')
        

def main(args):
    car = Car("red", 250)
    car.do_something()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))