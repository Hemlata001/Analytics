# Optimized Solution
from math import sqrt
def get_divisors(num):
    result = []
    for i in range(1, int(sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            if num//i != i: 
                result.append(num//i)
    result.sort()
    return result

print(get_divisors(36))
