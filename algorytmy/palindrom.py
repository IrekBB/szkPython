def is_palindrom(string):
    lista = list(string)
    if lista == lista[::-1]:
        return True
    return False

def isPalindrom(string):
    if len(string) == 1:
        return True
    if len(string) == 2:
        if string[0] == string[1]:
            return True
        return False
    return isPalindrom(string[1:-1]) if string[0] == string[-1] else False


