""""
Aby utworzyć niestandardowy iterator, należy zbudować obiekt  z nadpisaną
metodą __next__, o ile zdefiniowano uprzednio  metodę specjalną  __iter__,  
zwracającą  instancję iteratora.
"""
class CountDown:
    def __init__(self, step):
        self.step= step
    def __next__(self):
        """Return the next element"""
        if self.step <=0:
            raise StopIteration
        self.step -= 1
        return self.step
    def __iter__(self):
        """Return the iterator itself"""
        return self
     



def main(args):
    for element in CountDown(4):
        print (element)
        
if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))