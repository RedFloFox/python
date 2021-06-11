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

def palindrome_primes():
    palinPrimes = []
    for x in range(10000, 100000):
        if str(x)[::-1] == str(x):
            if is_prime(x) == True:
                palinPrimes.append(x)
    return palinPrimes


print(palindrome_primes())
