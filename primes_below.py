def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        multiples = 0
        for x in range(1,num):
            if ((num / x) - int(num/x)) == 0:
                multiples += 1
        if multiples < 3:
            return True
        else:
            return False


def primes_below(n):
    primesBelow = []
    for x in range(0, n):
        if is_prime(x) == True:
            primesBelow.append(x)
    return primesBelow


print(primes_below(17))
print(primes_below(8))
print(primes_below(2))
