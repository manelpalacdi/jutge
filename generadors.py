def fibs():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

def roots(x):
    y = x
    while 1:
        yield y
        y = 0.5 * (y + x / y)

def primes():
    p = 2
    foundPrime = False
    while 1: 
        yield p
        foundPrime = False
        while (not foundPrime):
            p += 1
            for i in range(2, p):
                if p % i == 0:
                    break
                if i == p - 1:
                    foundPrime = True

def hammings():
    p = 2
    foundPrime = False
    while 1: 
        yield p
        foundPrime = False
        while (not foundPrime):
            p += 1
            for i in range(2, p):
                if p % i == 0:
                    break
                if i == p - 1:
                    foundPrime = True
            


if __name__ == "__main__":
    g1 = fibs()
    g2 = roots(4)
    g3 = primes()
    print([next(g1) for i in range(10)])
    print([next(g2) for i in range(10)])
    print([next(g3) for i in range(20)])