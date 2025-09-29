import math
def is_prime(n):
    for i in range(2,int(math.sqrt(abs(n)))+1):
        if n%i==0:
            return False
    return True and n>=2


print(is_prime(2))
