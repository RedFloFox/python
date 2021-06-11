def big_fibonacci(n):
    i=0
    fibNum = 1
    while len(str(fibNum)) != n:
        fibNum += i
        i += 1
    return fibNum
