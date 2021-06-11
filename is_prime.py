def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        multiples = 0
        for x in range(1,9):
            if ((num / x) - int(num/x)) == 0:
                multiples += 1
        if multiples < 3:
            return True
        else:
            return False

print(is_prime(17))
print(is_prime(5))
print(is_prime(12))
print(is_prime(1))
