def anagram(a,b):
    if len(a) != len(b):  # muszą mieć tą samą długość
        return False
    else:
        if Counter(a) == Counter(b):  # Counter zlicza ilość wystapień 
            return True
        else:
            return False
def main():
    a = input('Anagram: ')
    b = input ('Czy anagram? ')
    return print(anagram(a,b))

if __name__ == '__main__':
    from collections import Counter
    import sys
    sys.exit(main())
